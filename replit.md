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
- **Texte**: Tout en blanc pur avec text-shadows
- **Overlays**: 6 couches (noir/40 + dégradés + radiaux + texture + accent)

## Services
1. Domiciliation d'Entreprise
2. Création & Gestion d'Entreprises
3. Conseil Stratégique & Business Development
4. Communication & Image Professionnelle

## Sections Page d'Accueil
1. **Hero** - Image fond, 6 overlays multi-couches, animations, texte blanc
2. **À Propos** - Présentation avec checklist
3. **Solutions complètes** - 2 colonnes de services
4. **Notre Processus** - 4 étapes (Consultation, Analyse, Exécution, Suivi)
5. **Pourquoi nous choisir** - Support, Rapidité, Sécurité
6. **Nos Projets** - 6 projets avec URLs
7. **Témoignages** - Avis clients
8. **CTA** - Section contact bleu nuit
9. **Contact** - Formulaire

## Recent Changes (26 Dec 2025)

### Hero Section Ultra-Premium
- **Hauteur adaptative**: `min-h-screen` - 100% hauteur de l'écran
- **6 Overlays multi-couches** avec opacités variables:
  - Couche 0: Noir pur `bg-black/40` (assombrit la photo)
  - Couche 1: Dégradé principal `from-primary-950/95 via-primary-900/85 to-primary-800/70`
  - Couche 2: Dégradé diagonal avec opacité 0.7
  - Couche 3: Effets radiaux complexes (opacité 30%)
  - Couche 4: Grain et texture SVG
  - Couche 5: Ligne accent top dégradée
- **Texte 100% blanc:**
  - Badge blanc avec border-white/60
  - Tous les éléments textes en text-white
  - Text-shadows multiples pour profondeur et lisibilité
- **Animations sophistiquées**:
  - Fade-in-up staggered (0.1s à 0.5s)
  - Shimmer sur "entreprise"
  - Pulse animations sur les glow backgrounds
  - Bounce sur scroll indicator
- **Effets visuels premium**:
  - Texte avec dégradé et multi-shadows
  - Buttons avec gradients et scale hover
  - Stats card avec backdrop blur et glow animé
  - Icons circulaires colorées
  - Effets 3D et ombres
- **Layout responsive**: 2 colonnes desktop, 1 colonne mobile
- **Parallax background** avec fixed attachment
- **Centrage parfait**: Espaces égaux gauche/droite dans le container

### Admin Panel - Hero Customization
- **HeroSettings Model**: Stocke badge_text, title_main, title_highlight, subtitle, background_image, btn1/btn2 config, et 3 métriques
- **Route /admin/hero**: Interface complète pour personnaliser tous les éléments du hero
- **Données dynamiques**: Le hero utilise les données de la base de données avec fallback defaults
- **WhatsApp Integration**: Bouton "Devis Gratuit" lié à WhatsApp avec numéro configurable dans les paramètres du site (site_settings.whatsapp)

### Admin Panel - Gestion des Projets (CRUD)
- **Project Model**: title, slug, description, image (upload), link, category, client_name, is_featured, is_active, order
- **Routes**: /admin/projects (liste), /admin/projects/new (créer), /admin/projects/<id>/edit (modifier), /admin/projects/<id>/delete (supprimer)
- **Upload d'images**: Images stockées dans static/uploads/projects/

### Admin Panel - Paramètres du Site Avancés
- **Réseaux sociaux**: Facebook, LinkedIn, Instagram, Twitter, YouTube - tous configurables et affichés dynamiquement dans le footer
- **Coordonnées**: Email, téléphone, adresse, WhatsApp
- **SEO Avancé**: 
  - Code personnalisé dans le `<head>` (Google Tag Manager, Pixel Facebook, etc.)
  - Code personnalisé avant `</body>` (chatbots, scripts de tracking)
- **Footer dynamique**: Les icônes des réseaux sociaux s'affichent uniquement si configurés
