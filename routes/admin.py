from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user
from modeles import db, User, Service, Testimonial, ContactSubmission, SiteSettings, SEOSettings, MediaAsset
from security import verify_password, hash_password, admin_required
from services import ContactService, SettingsService
from utils import save_uploaded_file, slugify
from datetime import datetime
import os

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

@admin_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('admin.dashboard'))
    
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        
        if user and verify_password(user.password_hash, password):
            user.last_login = datetime.utcnow()
            db.session.commit()
            login_user(user)
            flash('Connexion réussie !', 'success')
            return redirect(url_for('admin.dashboard'))
        else:
            flash('Email ou mot de passe incorrect.', 'danger')
    
    return render_template('admin/login.html')

@admin_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Vous avez été déconnecté.', 'info')
    return redirect(url_for('public.home'))

@admin_bp.route('/')
@login_required
@admin_required
def dashboard():
    stats = {
        'services': Service.query.count(),
        'testimonials': Testimonial.query.count(),
        'contacts': ContactSubmission.query.count(),
        'unread_contacts': ContactService.get_unread_count()
    }
    recent_contacts = ContactSubmission.query.order_by(ContactSubmission.created_at.desc()).limit(5).all()
    return render_template('admin/dashboard.html', stats=stats, recent_contacts=recent_contacts)

@admin_bp.route('/services')
@login_required
@admin_required
def services_list():
    services = Service.query.order_by(Service.order).all()
    return render_template('admin/services_list.html', services=services)

@admin_bp.route('/services/new', methods=['GET', 'POST'])
@login_required
@admin_required
def service_create():
    if request.method == 'POST':
        new_slug = slugify(request.form.get('name'))
        existing = Service.query.filter_by(slug=new_slug).first()
        if existing:
            flash('Un service avec ce nom existe déjà.', 'danger')
            return render_template('admin/service_form.html', service=None)
        
        service = Service(
            name=request.form.get('name'),
            slug=new_slug,
            short_description=request.form.get('short_description'),
            description=request.form.get('description'),
            icon=request.form.get('icon'),
            features=request.form.get('features'),
            is_featured=request.form.get('is_featured') == 'on',
            order=int(request.form.get('order', 0))
        )
        
        if 'image' in request.files:
            file = request.files['image']
            if file.filename:
                filepath = save_uploaded_file(file, 'services')
                if filepath:
                    service.image = '/' + filepath
        
        db.session.add(service)
        db.session.commit()
        flash('Service créé avec succès !', 'success')
        return redirect(url_for('admin.services_list'))
    
    return render_template('admin/service_form.html', service=None)

@admin_bp.route('/services/<int:id>/edit', methods=['GET', 'POST'])
@login_required
@admin_required
def service_edit(id):
    service = Service.query.get_or_404(id)
    
    if request.method == 'POST':
        new_slug = slugify(request.form.get('name'))
        existing = Service.query.filter(Service.slug == new_slug, Service.id != id).first()
        if existing:
            flash('Un service avec ce nom existe déjà.', 'danger')
            return render_template('admin/service_form.html', service=service)
        
        service.name = request.form.get('name')
        service.slug = new_slug
        service.short_description = request.form.get('short_description')
        service.description = request.form.get('description')
        service.icon = request.form.get('icon')
        service.features = request.form.get('features')
        service.is_featured = request.form.get('is_featured') == 'on'
        service.is_active = request.form.get('is_active') == 'on'
        service.order = int(request.form.get('order', 0))
        
        if 'image' in request.files:
            file = request.files['image']
            if file.filename:
                filepath = save_uploaded_file(file, 'services')
                if filepath:
                    service.image = '/' + filepath
        
        db.session.commit()
        flash('Service mis à jour avec succès !', 'success')
        return redirect(url_for('admin.services_list'))
    
    return render_template('admin/service_form.html', service=service)

@admin_bp.route('/services/<int:id>/delete', methods=['POST'])
@login_required
@admin_required
def service_delete(id):
    service = Service.query.get_or_404(id)
    db.session.delete(service)
    db.session.commit()
    flash('Service supprimé.', 'success')
    return redirect(url_for('admin.services_list'))

@admin_bp.route('/testimonials')
@login_required
@admin_required
def testimonials_list():
    testimonials = Testimonial.query.order_by(Testimonial.created_at.desc()).all()
    return render_template('admin/testimonials_list.html', testimonials=testimonials)

@admin_bp.route('/testimonials/new', methods=['GET', 'POST'])
@login_required
@admin_required
def testimonial_create():
    if request.method == 'POST':
        testimonial = Testimonial(
            author_name=request.form.get('author_name'),
            author_company=request.form.get('author_company'),
            author_position=request.form.get('author_position'),
            content=request.form.get('content'),
            rating=int(request.form.get('rating', 5)),
            is_featured=request.form.get('is_featured') == 'on'
        )
        
        if 'author_image' in request.files:
            file = request.files['author_image']
            if file.filename:
                filepath = save_uploaded_file(file, 'testimonials')
                if filepath:
                    testimonial.author_image = '/' + filepath
        
        db.session.add(testimonial)
        db.session.commit()
        flash('Témoignage créé avec succès !', 'success')
        return redirect(url_for('admin.testimonials_list'))
    
    return render_template('admin/testimonial_form.html', testimonial=None)

@admin_bp.route('/testimonials/<int:id>/edit', methods=['GET', 'POST'])
@login_required
@admin_required
def testimonial_edit(id):
    testimonial = Testimonial.query.get_or_404(id)
    
    if request.method == 'POST':
        testimonial.author_name = request.form.get('author_name')
        testimonial.author_company = request.form.get('author_company')
        testimonial.author_position = request.form.get('author_position')
        testimonial.content = request.form.get('content')
        testimonial.rating = int(request.form.get('rating', 5))
        testimonial.is_featured = request.form.get('is_featured') == 'on'
        testimonial.is_active = request.form.get('is_active') == 'on'
        
        if 'author_image' in request.files:
            file = request.files['author_image']
            if file.filename:
                filepath = save_uploaded_file(file, 'testimonials')
                if filepath:
                    testimonial.author_image = '/' + filepath
        
        db.session.commit()
        flash('Témoignage mis à jour !', 'success')
        return redirect(url_for('admin.testimonials_list'))
    
    return render_template('admin/testimonial_form.html', testimonial=testimonial)

@admin_bp.route('/testimonials/<int:id>/delete', methods=['POST'])
@login_required
@admin_required
def testimonial_delete(id):
    testimonial = Testimonial.query.get_or_404(id)
    db.session.delete(testimonial)
    db.session.commit()
    flash('Témoignage supprimé.', 'success')
    return redirect(url_for('admin.testimonials_list'))

@admin_bp.route('/contacts')
@login_required
@admin_required
def contacts_list():
    contacts = ContactSubmission.query.order_by(ContactSubmission.created_at.desc()).all()
    return render_template('admin/contacts_list.html', contacts=contacts)

@admin_bp.route('/contacts/<int:id>')
@login_required
@admin_required
def contact_view(id):
    contact = ContactSubmission.query.get_or_404(id)
    if not contact.is_read:
        contact.is_read = True
        db.session.commit()
    return render_template('admin/contact_view.html', contact=contact)

@admin_bp.route('/contacts/<int:id>/delete', methods=['POST'])
@login_required
@admin_required
def contact_delete(id):
    contact = ContactSubmission.query.get_or_404(id)
    db.session.delete(contact)
    db.session.commit()
    flash('Message supprimé.', 'success')
    return redirect(url_for('admin.contacts_list'))

@admin_bp.route('/settings', methods=['GET', 'POST'])
@login_required
@admin_required
def settings():
    site_settings = SettingsService.get_settings()
    
    if request.method == 'POST':
        site_settings.site_name = request.form.get('site_name')
        site_settings.email = request.form.get('email')
        site_settings.phone = request.form.get('phone')
        site_settings.address = request.form.get('address')
        site_settings.facebook = request.form.get('facebook')
        site_settings.linkedin = request.form.get('linkedin')
        site_settings.instagram = request.form.get('instagram')
        site_settings.whatsapp = request.form.get('whatsapp')
        site_settings.footer_text = request.form.get('footer_text')
        site_settings.google_analytics = request.form.get('google_analytics')
        
        if 'logo' in request.files:
            file = request.files['logo']
            if file.filename:
                filepath = save_uploaded_file(file, 'branding')
                if filepath:
                    site_settings.logo = '/' + filepath
        
        db.session.commit()
        flash('Paramètres mis à jour !', 'success')
        return redirect(url_for('admin.settings'))
    
    return render_template('admin/settings.html', settings=site_settings)

@admin_bp.route('/seo')
@login_required
@admin_required
def seo_list():
    seo_settings = SEOSettings.query.all()
    pages = ['home', 'services', 'cleaning', 'domiciliation', 'consulting', 'about', 'contact', 'testimonials']
    return render_template('admin/seo_list.html', seo_settings=seo_settings, pages=pages)

@admin_bp.route('/seo/<page_type>', methods=['GET', 'POST'])
@login_required
@admin_required
def seo_edit(page_type):
    seo = SEOSettings.query.filter_by(page_type=page_type).first()
    
    if request.method == 'POST':
        if not seo:
            seo = SEOSettings(page_type=page_type)
            db.session.add(seo)
        
        seo.meta_title = request.form.get('meta_title')
        seo.meta_description = request.form.get('meta_description')
        seo.keywords = request.form.get('keywords')
        seo.og_title = request.form.get('og_title')
        seo.og_description = request.form.get('og_description')
        seo.canonical_url = request.form.get('canonical_url')
        seo.robots = request.form.get('robots', 'index, follow')
        
        if 'og_image' in request.files:
            file = request.files['og_image']
            if file.filename:
                filepath = save_uploaded_file(file, 'seo')
                if filepath:
                    seo.og_image = '/' + filepath
        
        db.session.commit()
        flash('SEO mis à jour !', 'success')
        return redirect(url_for('admin.seo_list'))
    
    return render_template('admin/seo_form.html', seo=seo, page_type=page_type)

@admin_bp.route('/media')
@login_required
@admin_required
def media_list():
    media = MediaAsset.query.order_by(MediaAsset.uploaded_at.desc()).all()
    return render_template('admin/media_list.html', media=media)

@admin_bp.route('/media/upload', methods=['POST'])
@login_required
@admin_required
def media_upload():
    if 'file' not in request.files:
        flash('Aucun fichier sélectionné.', 'danger')
        return redirect(url_for('admin.media_list'))
    
    file = request.files['file']
    if file.filename:
        category = request.form.get('category', 'general')
        filepath = save_uploaded_file(file, category)
        if filepath:
            media = MediaAsset(
                filename=os.path.basename(filepath),
                original_filename=file.filename,
                file_path='/' + filepath,
                alt_text=request.form.get('alt_text', ''),
                category=category
            )
            db.session.add(media)
            db.session.commit()
            flash('Fichier uploadé avec succès !', 'success')
        else:
            flash('Type de fichier non autorisé.', 'danger')
    
    return redirect(url_for('admin.media_list'))

@admin_bp.route('/media/<int:id>/delete', methods=['POST'])
@login_required
@admin_required
def media_delete(id):
    media = MediaAsset.query.get_or_404(id)
    db.session.delete(media)
    db.session.commit()
    flash('Fichier supprimé.', 'success')
    return redirect(url_for('admin.media_list'))

@admin_bp.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    if request.method == 'POST':
        current_user.name = request.form.get('name')
        current_user.email = request.form.get('email')
        
        new_password = request.form.get('new_password')
        if new_password:
            current_password = request.form.get('current_password')
            if verify_password(current_user.password_hash, current_password):
                current_user.password_hash = hash_password(new_password)
                flash('Mot de passe mis à jour !', 'success')
            else:
                flash('Mot de passe actuel incorrect.', 'danger')
                return redirect(url_for('admin.profile'))
        
        db.session.commit()
        flash('Profil mis à jour !', 'success')
        return redirect(url_for('admin.profile'))
    
    return render_template('admin/profile.html')
