# Shabaka Invest Group - Site Web

## Overview
Site web complet pour Shabaka Invest Group, une société de domiciliation, création et gestion d'entreprises basée à Marrakech. Accompagne les entrepreneurs, investisseurs et dirigeants au Maroc.

## Tech Stack
- **Backend**: Python Flask
- **Database**: PostgreSQL
- **Frontend**: HTML, Tailwind CSS (via CDN), JavaScript
- **Authentication**: Flask-Login

## Project Structure
```
├── main.py                # Point d'entrée Flask
├── templates/            # Templates HTML (public, admin)
├── static/               # Fichiers statiques (uploads, etc)
├── modeles/              # Modèles SQLAlchemy
├── routes/               # Blueprints (public, admin)
├── services/             # Logique métier
├── security/             # Authentification
└── utils/                # Utilitaires
```

## Features
1. **Pages publiques**: Accueil, Services, À Propos, Contact
2. **Admin Panel** (`/admin`): Gestion complète du contenu
   - Services (CRUD)
   - Témoignages
   - Messages de contact
   - SEO par page
   - Bibliothèque médias
   - Paramètres du site

## Design & Couleurs
- **Couleur primaire**: Bleu nuit (#0d1a5e à #5a6cff)
- **Design**: Responsive avec Tailwind CSS
- **Thème**: Moderne et professionnel
- **Police**: Poppins
- **Style**: Traits inclinés, badges de section, cartes avec bordures

## Navigation
- Accueil
- Services
- À Propos
- Contact

## Admin Access
- **URL**: `/admin`
- **Email**: admin@shabakainvest.com
- **Password**: admin123

## Services Proposés
1. Domiciliation d'Entreprise
2. Création & Gestion d'Entreprises
3. Conseil Stratégique & Business Development
4. Communication & Image Professionnelle

## Projets Accompagnés
1. Syndic Shabaka (syndic.shabaka.site)
2. Villa à Vendre Marrakech (villaavendremarrakech.com)
3. Capsule Shabaka (capsule.shabaka.site)
4. AdScreen Shabaka (www.adscreen.shabaka.site)
5. Bellari Propreté Services (www.bellaripropreteservices.com)
6. Bellari Concept (bellariconcept.com)

## Sections de la Page d'Accueil
1. **Hero** - Titre principal avec CTA
2. **À Propos** - Présentation de l'entreprise
3. **Services** - 4 services principaux
4. **Pourquoi nous choisir** - 3 avantages (Support 24/7, Rapidité, Sécurité)
5. **Nos Projets** - 6 projets accompagnés avec liens externes
6. **Témoignages** - Avis clients
7. **Appel à l'action** - Section CTA bleu nuit
8. **Contact** - Formulaire de contact
9. **Blog** - Articles et ressources

## Recent Changes (26 Dec 2025)
- Refonte complète du design inspiré par l'image fournie
- Nouveau hero "Forgez l'avenir de votre entreprise"
- Navigation simplifiée avec bouton "Demander un Devis"
- Ajout section "Pourquoi nous choisir" avec 3 avantages
- Remplacement "Nos projets récents" par "Nos projets" avec 6 URLs réelles
- Ajout de plus de sections et contenu à la page d'accueil
- Traits inclinés style design moderne
- Badges de section avec bordures arrondies
- Cartes de projets interactives avec icônes
