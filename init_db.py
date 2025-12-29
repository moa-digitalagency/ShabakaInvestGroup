#!/usr/bin/env python3
"""
Script d'initialisation de la base de données pour Shabaka Invest Group
Utilisez ce script pour initialiser le schéma et les données par défaut lors d'un déploiement.

Usage:
    python init_db.py

Ce script va:
1. Créer toutes les tables de la base de données
2. Créer un administrateur par défaut
3. Ajouter les paramètres du site par défaut
4. Ajouter les services par défaut
5. Ajouter les témoignages par défaut
6. Configurer le hero section par défaut
"""

import os
import sys

os.environ.setdefault('DATABASE_URL', os.getenv('DATABASE_URL', ''))

from main import app
from modeles import db, User, Service, Testimonial, SiteSettings, HeroSettings, SEOSettings, Project
from security import hash_password

def init_database():
    """Initialise le schéma de la base de données."""
    with app.app_context():
        print("Création des tables de la base de données...")
        db.create_all()
        print("Tables créées avec succès!")

def seed_admin_user():
    """Crée l'utilisateur administrateur par défaut."""
    with app.app_context():
        if User.query.first() is None:
            admin = User(
                email='admin@shabakainvest.com',
                password_hash=hash_password('admin123'),
                name='Administrateur',
                role='admin'
            )
            db.session.add(admin)
            db.session.commit()
            print("Administrateur créé: admin@shabakainvest.com / admin123")
            print("IMPORTANT: Changez ce mot de passe après la première connexion!")
        else:
            print("Administrateur existe déjà.")

def seed_site_settings():
    """Configure les paramètres du site par défaut."""
    with app.app_context():
        if SiteSettings.query.first() is None:
            settings = SiteSettings(
                site_name='Shabaka Invest Group',
                email='contact@shabakainvest.com',
                phone='+212 524 000 000',
                address='Avenue Mohammed V, Guéliz, Marrakech 40000, Maroc',
                whatsapp='+212600000000',
                facebook='https://facebook.com/shabakainvest',
                linkedin='https://linkedin.com/company/shabakainvest',
                instagram='https://instagram.com/shabakainvest',
                footer_text='Shabaka Invest Group - Votre partenaire de confiance pour la domiciliation et le développement de votre entreprise à Marrakech.'
            )
            db.session.add(settings)
            db.session.commit()
            print("Paramètres du site créés.")
        else:
            print("Paramètres du site existent déjà.")

def seed_hero_settings():
    """Configure le hero section par défaut (met à jour si existe déjà)."""
    with app.app_context():
        hero = HeroSettings.query.first()
        if hero is None:
            hero = HeroSettings(
                badge_text='Bienvenue chez Shabaka Invest',
                title_main="Forgez l'avenir de votre",
                title_highlight='entreprise',
                subtitle='Votre partenaire de confiance à Marrakech pour la domiciliation, création et gestion d\'entreprises au Maroc',
                background_image='https://images.unsplash.com/photo-1552664730-d307ca884978?w=1600',
                btn1_text='Nos Services',
                btn1_link='/services',
                btn2_text='Devis Gratuit',
                btn2_is_whatsapp=True,
                metric1_value='90%',
                metric1_label='de croissance pour clients',
                metric2_value='15+',
                metric2_label="Ans d'expérience",
                metric3_value='100%',
                metric3_label='Satisfaction'
            )
            db.session.add(hero)
            db.session.commit()
            print("Hero section configurée.")
        else:
            hero.metric1_value = '90%'
            hero.metric1_label = 'de croissance pour clients'
            db.session.commit()
            print("Hero section mise à jour.")

def seed_services():
    """Ajoute les services par défaut (ajoute les manquants si certains existent déjà)."""
    with app.app_context():
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
        
        added_count = 0
        for data in services_data:
            existing = Service.query.filter_by(slug=data['slug']).first()
            if existing is None:
                service = Service(**data)
                db.session.add(service)
                added_count += 1
                print(f"  + Service ajouté: {data['name']}")
        
        if added_count > 0:
            db.session.commit()
            print(f"{added_count} nouveau(x) service(s) ajouté(s).")
        else:
            print("Tous les services existent déjà.")

def seed_testimonials():
    """Ajoute les témoignages par défaut (ajoute les manquants)."""
    with app.app_context():
        testimonials_data = [
            {
                'author_name': 'Ahmed Benali',
                'author_company': 'Tech Solutions Maroc',
                'author_position': 'Directeur Général',
                'content': 'Excellent service de domiciliation ! L\'équipe de Shabaka Invest Group est très professionnelle et réactive. Je recommande vivement pour tout entrepreneur souhaitant s\'installer à Marrakech.',
                'rating': 5,
                'is_featured': True
            },
            {
                'author_name': 'Karim Tazi',
                'author_company': 'Import Export KT',
                'author_position': 'Fondateur',
                'content': 'Grâce à leurs conseils, j\'ai pu créer mon entreprise rapidement et efficacement. Un accompagnement de qualité du début à la fin. Merci à toute l\'équipe !',
                'rating': 5,
                'is_featured': True
            },
            {
                'author_name': 'Sophie Martin',
                'author_company': 'Digital Agency',
                'author_position': 'CEO',
                'content': 'Très satisfaite de la qualité du service. L\'équipe est à l\'écoute et répond rapidement à toutes nos demandes. Une vraie valeur ajoutée pour notre entreprise.',
                'rating': 5,
                'is_featured': True
            },
            {
                'author_name': 'Mohammed El Fassi',
                'author_company': 'Consulting Pro',
                'author_position': 'Gérant',
                'content': 'Un partenaire de confiance pour notre développement au Maroc. Leur expertise nous a permis de gagner un temps précieux dans nos démarches administratives.',
                'rating': 5,
                'is_featured': True
            },
            {
                'author_name': 'Fatima Zahra Alami',
                'author_company': 'Mode & Design',
                'author_position': 'Directrice Artistique',
                'content': 'Service impeccable et équipe très réactive. Ils ont su comprendre nos besoins spécifiques et nous proposer des solutions adaptées.',
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
        
        added_count = 0
        for data in testimonials_data:
            existing = Testimonial.query.filter_by(author_name=data['author_name'], author_company=data['author_company']).first()
            if existing is None:
                testimonial = Testimonial(**data)
                db.session.add(testimonial)
                added_count += 1
        
        if added_count > 0:
            db.session.commit()
            print(f"{added_count} nouveau(x) témoignage(s) ajouté(s).")
        else:
            print("Tous les témoignages existent déjà.")

def seed_seo_settings():
    """Configure le SEO par défaut pour les pages principales."""
    with app.app_context():
        pages = ['home', 'services', 'about', 'contact']
        for page in pages:
            if SEOSettings.query.filter_by(page_type=page).first() is None:
                seo = SEOSettings(
                    page_type=page,
                    meta_title=f'Shabaka Invest Group - {page.capitalize()}',
                    meta_description='Shabaka Invest Group - Domiciliation et création d\'entreprises à Marrakech. Votre partenaire de confiance au Maroc.',
                    keywords='domiciliation, marrakech, entreprise, création, maroc, conseil'
                )
                db.session.add(seo)
        db.session.commit()
        print("SEO configuré pour les pages principales.")

def seed_sample_projects():
    """Ajoute des projets exemples."""
    with app.app_context():
        if Project.query.first() is None:
            projects_data = [
                {
                    'title': 'Création Société Import-Export',
                    'slug': 'creation-societe-import-export',
                    'description': 'Accompagnement complet pour la création d\'une société d\'import-export avec domiciliation et conseil juridique.',
                    'category': 'Création d\'entreprise',
                    'client_name': 'Client confidentiel',
                    'is_featured': True,
                    'order': 1
                },
                {
                    'title': 'Domiciliation Startup Tech',
                    'slug': 'domiciliation-startup-tech',
                    'description': 'Mise en place d\'une domiciliation prestigieuse pour une startup technologique internationale.',
                    'category': 'Domiciliation',
                    'client_name': 'TechStart SARL',
                    'is_featured': True,
                    'order': 2
                }
            ]
            for data in projects_data:
                project = Project(**data)
                db.session.add(project)
            db.session.commit()
            print(f"{len(projects_data)} projets exemples créés.")
        else:
            print("Projets existent déjà.")

def run_all():
    """Exécute toutes les initialisations."""
    print("=" * 50)
    print("INITIALISATION BASE DE DONNÉES SHABAKA INVEST")
    print("=" * 50)
    print()
    
    init_database()
    print()
    
    seed_admin_user()
    seed_site_settings()
    seed_hero_settings()
    seed_services()
    seed_testimonials()
    seed_seo_settings()
    seed_sample_projects()
    
    print()
    print("=" * 50)
    print("INITIALISATION TERMINÉE AVEC SUCCÈS!")
    print("=" * 50)
    print()
    print("Accès administrateur:")
    print("  Email: admin@shabakainvest.com")
    print("  Mot de passe: admin123")
    print()
    print("IMPORTANT: Changez le mot de passe après la première connexion!")

if __name__ == '__main__':
    run_all()
