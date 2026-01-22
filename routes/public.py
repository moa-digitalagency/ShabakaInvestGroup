from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify, Response, make_response
from modeles import db, Service, Testimonial, ContactSubmission, SiteSettings
from services import ContentService, TestimonialService, ContactService, SettingsService, SEOService, HeroService
from datetime import datetime

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

@public_bp.route('/sitemap.xml')
def sitemap():
    """Génère un sitemap XML dynamique pour les moteurs de recherche."""
    pages = []
    base_url = request.url_root.rstrip('/')
    now = datetime.utcnow().strftime('%Y-%m-%d')
    
    static_pages = [
        {'loc': '/', 'priority': '1.0', 'changefreq': 'weekly'},
        {'loc': '/services', 'priority': '0.9', 'changefreq': 'weekly'},
        {'loc': '/domiciliation', 'priority': '0.8', 'changefreq': 'monthly'},
        {'loc': '/conseils', 'priority': '0.8', 'changefreq': 'monthly'},
        {'loc': '/a-propos', 'priority': '0.7', 'changefreq': 'monthly'},
        {'loc': '/contact', 'priority': '0.8', 'changefreq': 'monthly'},
        {'loc': '/temoignages', 'priority': '0.6', 'changefreq': 'weekly'},
    ]
    
    for page in static_pages:
        pages.append({
            'loc': base_url + page['loc'],
            'lastmod': now,
            'changefreq': page['changefreq'],
            'priority': page['priority']
        })
    
    services = ContentService.get_all_services()
    for service in services:
        if service.is_active:
            pages.append({
                'loc': f"{base_url}/services/{service.slug}",
                'lastmod': service.updated_at.strftime('%Y-%m-%d') if service.updated_at else now,
                'changefreq': 'monthly',
                'priority': '0.7'
            })
    
    xml_content = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml_content += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    
    for page in pages:
        xml_content += '  <url>\n'
        xml_content += f'    <loc>{page["loc"]}</loc>\n'
        xml_content += f'    <lastmod>{page["lastmod"]}</lastmod>\n'
        xml_content += f'    <changefreq>{page["changefreq"]}</changefreq>\n'
        xml_content += f'    <priority>{page["priority"]}</priority>\n'
        xml_content += '  </url>\n'
    
    xml_content += '</urlset>'
    
    response = make_response(xml_content)
    response.headers['Content-Type'] = 'application/xml'
    return response

@public_bp.route('/robots.txt')
def robots():
    """Génère le fichier robots.txt pour contrôler l'indexation."""
    base_url = request.url_root.rstrip('/')
    
    robots_content = """# Robots.txt pour Shabaka Invest Group
# https://www.robotstxt.org/

# Autoriser tous les robots standards
User-agent: *
Allow: /
Disallow: /admin/
Disallow: /admin
Disallow: /static/uploads/
Disallow: /*?*

# Autoriser les robots IA pour l'indexation
User-agent: GPTBot
Allow: /

User-agent: ChatGPT-User
Allow: /

User-agent: Google-Extended
Allow: /

User-agent: anthropic-ai
Allow: /

User-agent: Claude-Web
Allow: /

User-agent: CCBot
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: Bytespider
Allow: /

User-agent: cohere-ai
Allow: /

# Bloquer les scrapers agressifs
User-agent: AhrefsBot
Disallow: /

User-agent: SemrushBot
Disallow: /

User-agent: MJ12bot
Disallow: /

User-agent: DotBot
Disallow: /

# Sitemap
Sitemap: {base_url}/sitemap.xml
""".format(base_url=base_url)
    
    response = make_response(robots_content)
    response.headers['Content-Type'] = 'text/plain'
    return response
