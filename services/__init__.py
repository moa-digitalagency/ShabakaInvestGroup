from modeles import db, Service, Page, Testimonial, ContactSubmission, SiteSettings, SEOSettings, User
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

def seed_initial_data():
    if User.query.first() is None:
        admin = User(
            email='admin@shabakainvest.com',
            password_hash=hash_password('admin123'),
            name='Administrateur',
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
    
    if Service.query.first() is None:
        services_data = [
            {
                'name': 'Domiciliation d\'Entreprise',
                'slug': 'domiciliation-entreprise',
                'short_description': 'Obtenez une adresse commerciale prestigieuse à Marrakech pour votre entreprise.',
                'description': '''La domiciliation d'entreprise chez Shabaka Invest Group vous offre une adresse commerciale de prestige au cœur de Marrakech.

Nos services incluent : adresse commerciale officielle, réception et gestion du courrier, accueil téléphonique personnalisé, utilisation de salles de réunion, et accompagnement administratif.

Idéal pour les entrepreneurs, freelances et sociétés souhaitant établir leur présence à Marrakech sans les coûts d'un bureau permanent.''',
                'icon': 'building',
                'features': 'Adresse commerciale prestigieuse,Réception du courrier,Accueil téléphonique,Salles de réunion,Support administratif,Flexibilité totale',
                'is_featured': True,
                'order': 1
            },
            {
                'name': 'Conseils aux Entreprises',
                'slug': 'conseils-entreprise',
                'short_description': 'Expertise et accompagnement stratégique pour le développement de votre activité.',
                'description': '''Nos experts vous accompagnent dans toutes les étapes de développement de votre entreprise.

Nous offrons des conseils en : création d'entreprise, stratégie commerciale, optimisation fiscale, gestion financière, ressources humaines, et développement commercial.

Avec notre connaissance approfondie du marché marocain, nous vous aidons à prendre les meilleures décisions pour votre business.''',
                'icon': 'lightbulb',
                'features': 'Création d\'entreprise,Stratégie commerciale,Optimisation fiscale,Gestion financière,Conseil RH,Développement commercial',
                'is_featured': True,
                'order': 2
            },
            {
                'name': 'Gestion de Projet',
                'slug': 'gestion-projet',
                'short_description': 'Pilotage complet de vos projets de construction et rénovation.',
                'description': '''Notre service de gestion de projet assure le suivi complet de vos projets immobiliers et de construction.

Nous gérons : la planification, la coordination des intervenants, le suivi des délais et budgets, le contrôle qualité.

De la conception à la livraison, nous sommes votre interlocuteur unique pour des projets réussis.''',
                'icon': 'clipboard-list',
                'features': 'Planification complète,Coordination des équipes,Suivi budgétaire,Contrôle qualité,Livraison clé en main',
                'is_featured': True,
                'order': 3
            }
        ]
        for data in services_data:
            service = Service(**data)
            db.session.add(service)
    
    if Testimonial.query.first() is None:
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
            }
        ]
        for data in testimonials_data:
            testimonial = Testimonial(**data)
            db.session.add(testimonial)
    
    db.session.commit()
