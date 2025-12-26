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

## Services
1. Domiciliation d'Entreprise
2. Création & Gestion d'Entreprises
3. Conseil Stratégique & Business Development
4. Communication & Image Professionnelle

## Sections Page d'Accueil
1. **Hero** - Image fond, overlays multi-couches, animations
2. **À Propos** - Présentation avec checklist
3. **Solutions complètes** - 2 colonnes de services
4. **Notre Processus** - 4 étapes
5. **Pourquoi nous choisir** - Support, Rapidité, Sécurité
6. **Nos Projets** - 6 projets avec URLs
7. **Témoignages** - Avis clients
8. **CTA** - Section contact bleu nuit
9. **Contact** - Formulaire

## Recent Changes (26 Dec 2025)

### Hero Section Ultra-Stylisé
- **Hauteur adaptative**: `min-h-screen` - 100% hauteur de l'écran
- **Overlays multi-couches** avec opacités variables:
  - Couche 1: Dégradé principal `from-primary-950/95 via-primary-900/85 to-primary-800/70`
  - Couche 2: Dégradé diagonal avec opacité 0.7
  - Couche 3: Effets radiaux complexes (opacité 30%)
  - Couche 4: Grain et texture SVG
  - Couche 5: Ligne accent top dégradée
- **Animations sophistiquées**:
  - Fade-in-up staggered (0.1s à 0.5s)
  - Shimmer sur "entreprise"
  - Pulse animations sur les glow backgrounds
  - Bounce sur scroll indicator
- **Effets visuels modernes**:
  - Texte avec dégradé et shadow
  - Buttons avec backdrop blur et scale hover
  - Stats card avec hover effects
  - Glow animé derrière stats
  - Effets 3D et ombres
- **Layout responsive**: 2 colonnes desktop, 1 colonne mobile
- **Parallax background** avec fixed attachment
