from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from modeles import db, Service, Testimonial, ContactSubmission, SiteSettings
from services import ContentService, TestimonialService, ContactService, SettingsService, SEOService, HeroService

public_bp = Blueprint('public', __name__)

@public_bp.context_processor
def inject_settings():
    settings = SettingsService.get_settings()
    services = ContentService.get_all_services()
    return dict(site_settings=settings, all_services=services)

@public_bp.route('/')
def home():
    featured_services = ContentService.get_featured_services()
    testimonials = TestimonialService.get_featured_testimonials()
    seo = SEOService.get_seo_for_page('home')
    hero = HeroService.get_hero_settings()
    return render_template('public/home.html', 
                         featured_services=featured_services,
                         testimonials=testimonials,
                         seo=seo,
                         hero=hero)

@public_bp.route('/services')
def services():
    all_services = ContentService.get_all_services()
    seo = SEOService.get_seo_for_page('services')
    return render_template('public/services.html', services=all_services, seo=seo)

@public_bp.route('/services/<slug>')
def service_detail(slug):
    service = ContentService.get_service_by_slug(slug)
    if not service:
        flash('Service non trouvé.', 'warning')
        return redirect(url_for('public.services'))
    return render_template('public/service_detail.html', service=service)

@public_bp.route('/domiciliation')
def domiciliation():
    service = ContentService.get_service_by_slug('domiciliation-entreprise')
    seo = SEOService.get_seo_for_page('domiciliation')
    return render_template('public/domiciliation.html', service=service, seo=seo)

@public_bp.route('/conseils')
def consulting():
    service = ContentService.get_service_by_slug('conseils-entreprise')
    seo = SEOService.get_seo_for_page('consulting')
    return render_template('public/consulting.html', service=service, seo=seo)

@public_bp.route('/a-propos')
def about():
    seo = SEOService.get_seo_for_page('about')
    return render_template('public/about.html', seo=seo)

@public_bp.route('/contact', methods=['GET', 'POST'])
def contact():
    services = ContentService.get_all_services()
    seo = SEOService.get_seo_for_page('contact')
    
    if request.method == 'POST':
        data = {
            'name': request.form.get('name'),
            'email': request.form.get('email'),
            'phone': request.form.get('phone'),
            'company': request.form.get('company'),
            'service_interest': request.form.get('service_interest'),
            'message': request.form.get('message')
        }
        
        if not data['name'] or not data['email'] or not data['message']:
            flash('Veuillez remplir tous les champs obligatoires.', 'danger')
        else:
            ContactService.create_submission(data)
            flash('Votre message a été envoyé avec succès ! Nous vous répondrons dans les plus brefs délais.', 'success')
            return redirect(url_for('public.contact'))
    
    return render_template('public/contact.html', services=services, seo=seo)

@public_bp.route('/temoignages')
def testimonials():
    all_testimonials = TestimonialService.get_all_testimonials()
    seo = SEOService.get_seo_for_page('testimonials')
    return render_template('public/testimonials.html', testimonials=all_testimonials, seo=seo)

@public_bp.route('/mentions-legales')
def legal():
    return render_template('public/legal.html')
