# Shabaka Invest Group - Site Web

## Overview
Site web complet pour Shabaka Invest Group, une société de domiciliation et conseils d'entreprise basée à Marrakech. Le site met particulièrement en avant le service de nettoyage de chantier.

## Tech Stack
- **Backend**: Python Flask
- **Database**: PostgreSQL
- **Frontend**: HTML, Tailwind CSS (via CDN), JavaScript
- **Authentication**: Flask-Login

## Project Structure
```
├── main.py                 # Point d'entrée Flask
├── src/
│   ├── modeles/           # Modèles SQLAlchemy (User, Service, Testimonial, etc.)
│   ├── routes/            # Blueprints (public, admin)
│   ├── services/          # Logique métier
│   ├── security/          # Authentification et sécurité
│   └── utils/             # Utilitaires (upload, slugify)
├── templates/
│   ├── base.html          # Template de base
│   ├── public/            # Pages publiques
│   └── admin/             # Panel d'administration
└── static/
    └── uploads/           # Fichiers uploadés
```

## Features
1. **Pages publiques**: Accueil, Services, Nettoyage Chantier, Domiciliation, Conseils, Contact, À Propos, Témoignages
2. **Admin Panel** (`/admin`): Gestion complète du contenu
   - Services (CRUD)
   - Témoignages
   - Messages de contact
   - SEO par page
   - Paramètres du site
   - Bibliothèque médias

## Admin Access
- **URL**: `/admin`
- **Email**: admin@shabakainvest.com
- **Password**: admin123

## Database Models
- User, Service, Testimonial, ContactSubmission, SiteSettings, SEOSettings, MediaAsset, Page

## Running the App
```bash
python main.py
```
The app runs on port 5000.

## Recent Changes
- Initial creation: December 2024
- Full CMS with admin panel
- SEO management per page
- Responsive design with Tailwind CSS
