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

## Design
- **Couleur primaire**: Bleu nuit (#0d1a5e à #5a6cff)
- **Design**: Responsive avec Tailwind CSS
- **Police**: Poppins
- **Hero**: Image de fond, overlay dégradé, hauteur adaptative (min-h-screen)

## Services
1. Domiciliation d'Entreprise
2. Création & Gestion d'Entreprises
3. Conseil Stratégique & Business Development
4. Communication & Image Professionnelle

## Sections Page d'Accueil
1. **Hero** - Image de fond avec overlay dégradé variable, hauteur plein écran
2. **À Propos** - Présentation avec checklist
3. **Solutions complètes** - 2 colonnes de services
4. **Notre Processus** - 4 étapes (Consultation, Analyse, Exécution, Suivi)
5. **Pourquoi nous choisir** - Support, Rapidité, Sécurité
6. **Nos Projets** - 6 projets avec URLs
7. **Témoignages** - Avis clients
8. **CTA** - Section contact bleu nuit
9. **Contact** - Formulaire

## Recent Changes (26 Dec 2025)
- Hero entièrement redesigné avec style moderne
- Overlay dégradé multi-couches (opacités variables)
- Hauteur adaptative à l'écran (min-h-screen)
- Gradient text sur "entreprise"
- Animations fade-in et hover effects
- Stats card avec backdrop blur sur mobile
- Effets visuels: radial gradients, pulse animations
- Section Blog supprimée
- Contenu simplifié et focalisé
