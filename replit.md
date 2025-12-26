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

## Couleurs & Design
- **Couleur primaire**: Bleu nuit (#0d1a5e à #5a6cff)
- **Design**: Responsive avec Tailwind CSS
- **Thème**: Moderne et professionnel

## Admin Access
- **URL**: `/admin`
- **Email**: admin@shabakainvest.com
- **Password**: admin123

## Services Proposés
1. Domiciliation d'Entreprise
2. Création & Gestion d'Entreprises
3. Conseil Stratégique & Business Development
4. Communication & Image Professionnelle

## Navigation
- Accueil
- Services
- À Propos
- Contact

## Recent Changes (26 Dec 2025)
- Refonte complète du design et contenu
- Nouveau hero "Forgez l'avenir de votre entreprise"
- Navigation simplifiée (4 pages principales)
- Nouveaux services : Domiciliation, Création, Conseil, Communication
- Section projets accompagnés sur la page d'accueil
- Témoignages clients mis à jour
- Section "Pourquoi nous choisir"
- Footer modernisé
- Couleur bleu nuit conservée
