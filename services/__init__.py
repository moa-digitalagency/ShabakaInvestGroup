import os
from modeles import db, Service, Page, Testimonial, ContactSubmission, SiteSettings, SEOSettings, User, HeroSettings
from security import hash_password
from datetime import datetime

class ContentService:
    @staticmethod
    def get_all_services(active_only=True):
        query = Service.query
        if active_only:
            query = query.filter_by(is_active=True)
        return query.order_by(Service.order).all()
    
    @staticmethod
    def get_featured_services():
        return Service.query.filter_by(is_featured=True, is_active=True).order_by(Service.order).all()
    
    @staticmethod
    def get_service_by_slug(slug):
        return Service.query.filter_by(slug=slug, is_active=True).first()

class TestimonialService:
    @staticmethod
    def get_all_testimonials(active_only=True):
        query = Testimonial.query
        if active_only:
            query = query.filter_by(is_active=True)
        return query.order_by(Testimonial.created_at.desc()).all()
    
    @staticmethod
    def get_featured_testimonials():
        return Testimonial.query.filter_by(is_featured=True, is_active=True).limit(6).all()

class ContactService:
    @staticmethod
    def create_submission(data):
        submission = ContactSubmission(
            name=data.get('name'),
            email=data.get('email'),
            phone=data.get('phone'),
            company=data.get('company'),
            service_interest=data.get('service_interest'),
            message=data.get('message')
        )
        db.session.add(submission)
        db.session.commit()
        return submission
    
    @staticmethod
    def get_unread_count():
        return ContactSubmission.query.filter_by(is_read=False).count()

class SettingsService:
    @staticmethod
    def get_settings():
        settings = SiteSettings.query.first()
        if not settings:
            settings = SiteSettings(
                site_name='Shabaka Invest Group',
                email='contact@shabakainvest.com',
                phone='+212 524 000 000',
                address='Marrakech, Maroc'
            )
            db.session.add(settings)
            db.session.commit()
        return settings

class SEOService:
    @staticmethod
    def get_seo_for_page(page_type):
        return SEOSettings.query.filter_by(page_type=page_type).first()

class HeroService:
    @staticmethod
    def get_hero_settings():
        hero = HeroSettings.query.first()
        if not hero:
            hero = HeroSettings()
            db.session.add(hero)
            db.session.commit()
        return hero

def seed_initial_data():
    admin_email = os.environ.get('ADMIN_MAIL', 'admin@shabakainvest.com')
    admin_password = os.environ.get('ADMIN_PASSWORD', 'admin123')
    admin_name = os.environ.get('ADMIN_USERNAME', 'Administrateur')
    
    existing_admin = User.query.filter_by(email=admin_email).first()
    if existing_admin is None:
        if User.query.first() is None:
            admin = User(
                email=admin_email,
                password_hash=hash_password(admin_password),
                name=admin_name,
                role='admin'
            )
            db.session.add(admin)
    
    if SiteSettings.query.first() is None:
        settings = SiteSettings(
            site_name='Shabaka Invest Group',
            email='contact@shabakainvest.com',
            phone='+212 524 000 000',
            address='Avenue Mohammed V, Guéliz, Marrakech 40000, Maroc',
            whatsapp='+212600000000',
            footer_text='Shabaka Invest Group - Votre partenaire de confiance pour la domiciliation et le développement de votre entreprise à Marrakech.'
        )
        db.session.add(settings)
    
    if HeroSettings.query.first() is None:
        hero = HeroSettings()
        db.session.add(hero)
    
    services_data = [
        {
            'name': 'Domiciliation d\'Entreprise',
            'slug': 'domiciliation-entreprise',
            'short_description': 'Adresse professionnelle à Marrakech avec gestion du courrier et justificatifs conformes.',
            'description': '''<h3>Une adresse commerciale prestigieuse à Marrakech</h3>
<p>La domiciliation d'entreprise chez Shabaka Invest Group vous offre une adresse commerciale de prestige au cœur de Marrakech.</p>
<h4>Nos services incluent :</h4>
<ul>
<li>Adresse commerciale officielle</li>
<li>Réception et gestion du courrier</li>
<li>Accueil téléphonique personnalisé</li>
<li>Utilisation de salles de réunion</li>
<li>Accompagnement administratif</li>
</ul>
<p>Idéal pour les entrepreneurs, freelances et sociétés souhaitant établir leur présence à Marrakech sans les coûts d'un bureau permanent.</p>''',
            'icon': 'building',
            'features': 'Adresse commerciale prestigieuse,Réception du courrier,Accueil téléphonique,Salles de réunion,Support administratif,Flexibilité totale',
            'is_featured': True,
            'order': 1
        },
        {
            'name': 'Création d\'Entreprise',
            'slug': 'creation-entreprise',
            'short_description': 'Accompagnement complet pour la création de votre société au Maroc.',
            'description': '''<h3>Créez votre entreprise au Maroc en toute simplicité</h3>
<p>Nous vous accompagnons dans toutes les démarches de création de votre entreprise au Maroc.</p>
<h4>Notre accompagnement comprend :</h4>
<ul>
<li>Choix de la forme juridique adaptée</li>
<li>Rédaction des statuts</li>
<li>Immatriculation au registre du commerce</li>
<li>Obtention du numéro d'identification fiscale</li>
<li>Ouverture du compte bancaire professionnel</li>
</ul>''',
            'icon': 'file-signature',
            'features': 'Choix forme juridique,Rédaction statuts,Immatriculation RC,Numéro fiscal,Compte bancaire,Accompagnement complet',
            'is_featured': True,
            'order': 2
        },
        {
            'name': 'Conseil Stratégique',
            'slug': 'conseil-strategique',
            'short_description': 'Expertise et accompagnement stratégique pour le développement de votre activité.',
            'description': '''<h3>Un accompagnement expert pour votre croissance</h3>
<p>Nos experts vous accompagnent dans toutes les étapes de développement de votre entreprise.</p>
<h4>Nos domaines d'expertise :</h4>
<ul>
<li>Stratégie commerciale</li>
<li>Optimisation fiscale</li>
<li>Gestion financière</li>
<li>Ressources humaines</li>
<li>Développement commercial</li>
</ul>''',
            'icon': 'lightbulb',
            'features': 'Stratégie commerciale,Optimisation fiscale,Gestion financière,Conseil RH,Business development',
            'is_featured': True,
            'order': 3
        },
        {
            'name': 'Marketing et communication',
            'slug': 'marketing-communication',
            'short_description': 'Développement de stratégies marketing pour optimiser la visibilité et la commercialisation de votre entreprise.',
            'description': '''<h3>Amplifiez votre visibilité et commercialisation</h3>
<p>Nous développons des stratégies marketing complètes pour optimiser la visibilité et la commercialisation de votre entreprise.</p>
<h4>Nos domaines d'expertise :</h4>
<ul>
<li>Stratégie marketing globale</li>
<li>Création d'identité visuelle et de marque</li>
<li>Sites web et présence digitale</li>
<li>Stratégie réseaux sociaux et contenu</li>
<li>Supports de communication et print</li>
<li>Campagnes publicitaires et promotion</li>
</ul>''',
            'icon': 'bullhorn',
            'features': 'Stratégie marketing,Identité visuelle,Site web,Réseaux sociaux,Supports digitaux,Gestion de marque',
            'is_featured': True,
            'order': 4
        }
    ]
    for data in services_data:
        existing = Service.query.filter_by(slug=data['slug']).first()
        if existing is None:
            service = Service(**data)
            db.session.add(service)
    
    testimonials_data = [
        {
            'author_name': 'Ahmed Benali',
            'author_company': 'Tech Solutions Maroc',
            'author_position': 'Directeur Général',
            'content': 'Excellent service de domiciliation ! L\'équipe de Shabaka Invest Group est très professionnelle et réactive. Je recommande vivement.',
            'rating': 5,
            'is_featured': True
        },
        {
            'author_name': 'Karim Tazi',
            'author_company': 'Import Export KT',
            'author_position': 'Fondateur',
            'content': 'Grâce à leurs conseils, j\'ai pu créer mon entreprise rapidement et efficacement. Un accompagnement de qualité du début à la fin.',
            'rating': 5,
            'is_featured': True
        },
        {
            'author_name': 'Sophie Martin',
            'author_company': 'Digital Agency',
            'author_position': 'CEO',
            'content': 'Très satisfaite de la qualité du service. L\'équipe est à l\'écoute et répond rapidement à toutes nos demandes.',
            'rating': 5,
            'is_featured': True
        },
        {
            'author_name': 'Mohammed El Fassi',
            'author_company': 'Consulting Pro',
            'author_position': 'Gérant',
            'content': 'Un partenaire de confiance pour notre développement au Maroc. Leur expertise nous a permis de gagner un temps précieux.',
            'rating': 5,
            'is_featured': True
        },
        {
            'author_name': 'Fatima Zahra Alami',
            'author_company': 'Mode & Design',
            'author_position': 'Directrice Artistique',
            'content': 'Service impeccable et équipe très réactive. Ils ont su comprendre nos besoins spécifiques.',
            'rating': 5,
            'is_featured': True
        },
        {
            'author_name': 'Jean-Pierre Dubois',
            'author_company': 'Invest France Maroc',
            'author_position': 'Président',
            'content': 'Shabaka Invest nous a accompagnés dans notre implantation au Maroc. Leur connaissance du marché local est un atout majeur.',
            'rating': 5,
            'is_featured': True
        }
    ]
    for data in testimonials_data:
        existing = Testimonial.query.filter_by(author_name=data['author_name'], author_company=data['author_company']).first()
        if existing is None:
            testimonial = Testimonial(**data)
            db.session.add(testimonial)
    
    hero = HeroSettings.query.first()
    if hero:
        hero.metric1_value = '90%'
        hero.metric1_label = 'de croissance pour clients'
    
    db.session.commit()
