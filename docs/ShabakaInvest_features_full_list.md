# Shabaka Invest Group - Features Full List

Ce document recense de manière exhaustive l'ensemble des fonctionnalités de la plateforme Shabaka Invest Group, couvrant l'interface publique, l'interface d'administration et les comportements techniques spécifiques.

## 1. Interface Publique (Frontend)

L'interface publique est accessible à tous les visiteurs et présente les services de l'entreprise.

### 1.1 Page d'Accueil (`/`)
*   **Héro Dynamique (Hero Section) :**
    *   Affichage d'un titre principal, sous-titre et badge configurables depuis l'admin.
    *   Image de fond personnalisable via URL ou upload.
    *   Deux boutons d'action (CTA) configurables (texte, icône, lien/action).
    *   **Intégration WhatsApp :** Le bouton secondaire peut être configuré pour ouvrir directement une modale de contact WhatsApp.
    *   **Métriques Clés (KPIs) :** Affichage de 3 indicateurs de performance (ex: "500+ Entreprises créées") avec icônes et labels modifiables.
*   **Services en Vedette :**
    *   Affichage automatique des services marqués comme `is_featured` dans l'admin.
    *   Présentation sous forme de cartes avec icône, titre et courte description.
*   **Témoignages (Testimonials) :**
    *   Carrousel ou grille affichant les témoignages clients validés (`is_featured`).
    *   Affiche le nom, l'entreprise, le poste, la note (étoiles) et le contenu.
*   **SEO Automatisé :**
    *   Balises Meta Title et Description injectées dynamiquement depuis la configuration SEO globale pour la page 'home'.

### 1.2 Catalogue des Services (`/services`)
*   **Liste Complète :**
    *   Affichage de tous les services actifs, triés par ordre défini dans l'admin (`order`).
    *   Chaque carte de service inclut un lien "En savoir plus" vers la page de détail.
*   **Détail d'un Service (`/services/<slug>`) :**
    *   Page dédiée générée dynamiquement via le `slug` du service.
    *   Affichage de l'image de couverture du service.
    *   Description complète (Rich Text).
    *   Liste des fonctionnalités spécifiques (si définies).
    *   Fil d'ariane (Breadcrumb) automatique.
    *   SEO spécifique généré à partir du titre et de la description courte du service si non surchargé.

### 1.3 Pages Spécialisées (Hardcoded Routing)
Certaines URLs sont routées spécifiquement pour des raisons de SEO ou de marketing, mais chargent du contenu dynamique :
*   **Domiciliation (`/domiciliation`) :** Charge le contenu du service dont le slug est `domiciliation-entreprise`.
*   **Conseils (`/conseils`) :** Charge le contenu du service dont le slug est `conseils-entreprise`.
*   **À Propos (`/a-propos`) :** Page statique présentant l'entreprise, avec SEO configurable.

### 1.4 Module de Contact (`/contact`)
*   **Formulaire de Contact :**
    *   Champs : Nom, Email, Téléphone, Entreprise, Service intéressé, Message.
    *   **Validation Client :** HTML5 attributes (`required`, `type="email"`).
    *   **Validation Serveur :** Vérification de la présence des champs obligatoires (Nom, Email, Message).
    *   **Traitement :**
        *   Enregistrement en base de données (`ContactSubmission`).
        *   Statut initial défini à "Non lu".
        *   Feedback utilisateur via message Flash (Succès ou Erreur).
    *   **Sécurité :** Protection CSRF via `Flask-WTF`.

### 1.5 Intégrations & Utilitaires
*   **Modale de Devis WhatsApp (Global) :**
    *   Accessible depuis la navigation (bouton "Demander un Devis") et le Hero.
    *   Formulaire simplifié (Nom, Tél, Service, Message).
    *   **Redirection Intelligente :** Génère une URL `wa.me` pré-remplie avec le message formaté, incluant les détails saisis.
    *   Ouverture dans un nouvel onglet pour ne pas perdre le visiteur.
*   **Sitemap XML (`/sitemap.xml`) :**
    *   Génération dynamique listant toutes les pages statiques et tous les services actifs.
    *   Mise à jour automatique des dates de modification (`lastmod`).
    *   Priorités et fréquences de changement configurées par type de page.
*   **Robots.txt (`/robots.txt`) :**
    *   Génération dynamique.
    *   Bloque l'accès au dossier `/admin` et aux uploads statiques pour les robots.
    *   Autorise explicitement les bots IA majeurs (GPTBot, Claude, etc.) tout en bloquant les scrapers agressifs (Ahrefs, Semrush, MJ12bot).
*   **Mentions Légales (`/mentions-legales`) :** Page statique obligatoire.

---

## 2. Interface d'Administration (Backend)

Accessible via `/admin/login`, sécurisée par authentification session.

### 2.1 Authentification & Sécurité
*   **Login :** Email/Mot de passe.
*   **Hachage :** Mots de passe stockés sous forme de hash (implémentation `werkzeug.security`).
*   **Protection :**
    *   Déconnexion automatique après expiration de session.
    *   Protection CSRF sur tous les formulaires POST.
    *   Décorateur `@admin_required` sur toutes les routes sensibles.
*   **Profil Admin :** Modification du nom, email et mot de passe de l'administrateur connecté.

### 2.2 Tableau de Bord (Dashboard)
*   **Vue d'ensemble :**
    *   Compteurs en temps réel : Nombre de services, témoignages, messages reçus, messages non lus.
    *   Liste des 5 derniers messages de contact reçus avec lien direct vers le détail.

### 2.3 Gestion des Services (CRUD)
*   **Création/Édition :**
    *   Nom (génère automatiquement le slug).
    *   Description courte (pour les cartes) et longue (pour la page détail).
    *   Icône (classe FontAwesome).
    *   Upload d'image (stockée dans `static/uploads/services/`).
    *   **Attributs :** `is_featured` (mettre en avant sur l'accueil), `is_active` (publier/dépublier), `order` (tri).
*   **Suppression :** Suppression définitive du service et de son image associée.

### 2.4 Gestion des Témoignages
*   **Champs :** Auteur, Entreprise, Poste, Contenu, Note (1-5).
*   **Upload Photo :** Gestion de l'avatar du client.
*   **Modération :**
    *   `is_featured` : Afficher sur la page d'accueil.
    *   `is_active` : Afficher sur la page témoignages.

### 2.5 Gestion des Messages (CRM Léger)
*   **Liste :** Vue tabulaire des messages reçus, triés par date (plus récents en premier).
*   **Lecture :**
    *   Vue détaillée du message.
    *   **Marquage automatique :** Un message passe de "Non lu" à "Lu" à l'ouverture.
*   **Suppression :** Possibilité de supprimer les messages traités ou spam.

### 2.6 Gestion des Médias (Media Library)
*   **Upload Centralisé :** Interface pour uploader des fichiers (images, documents) indépendamment des contenus.
*   **Catégorisation :** Possibilité de taguer les fichiers (ex: 'general', 'seo', 'hero').
*   **Visualisation :** Aperçu des images, lien direct vers le fichier.
*   **Nettoyage :** Suppression des fichiers du serveur et de la base de données.

### 2.7 Configuration du Site (Settings)
*   **Informations Générales :** Nom du site, Email de contact, Téléphone, Adresse.
*   **Réseaux Sociaux :** Liens Facebook, LinkedIn, Instagram, Twitter, YouTube (les icônes n'apparaissent que si le lien est rempli).
*   **Branding :** Upload du Logo et du Favicon.
*   **Scripts Personnalisés :**
    *   Injection de code dans le `<head>` (ex: Google Analytics, Pixel FB).
    *   Injection de code dans le `<footer>` (ex: Scripts de chat tiers).
*   **Numéro WhatsApp :** Configuration du numéro utilisé pour la modale de devis.

### 2.8 Gestion SEO Avancée
*   **Éditeur Meta Tags :** Pour chaque page type (Home, Services, Contact, etc.), configuration de :
    *   Meta Title.
    *   Meta Description.
    *   Keywords.
    *   Canonical URL.
    *   Robots Tag (index/noindex).
*   **Open Graph :** Configuration du titre, description et image pour le partage social (Facebook/LinkedIn).

### 2.9 Gestion du Hero (Page d'Accueil)
*   Interface dédiée pour modifier tous les éléments textuels et visuels de la section Hero sans toucher au code.
*   Supporte l'upload d'image ou l'utilisation d'une URL externe pour le fond.

### 2.10 Gestion des Projets (Portfolio)
*   CRUD complet pour présenter les réalisations (Case Studies).
*   Champs : Titre, Client, Catégorie, Lien externe, Image, Description.

---

## 3. Spécificités Techniques

### 3.1 Gestion des Fichiers
*   **Upload :** Les fichiers sont renommés et sécurisés (`utils.save_uploaded_file`) pour éviter les conflits et les noms de fichiers dangereux.
*   **Stockage :** Dossier `static/uploads/` organisé par sous-dossiers (`services`, `testimonials`, `branding`, etc.).

### 3.2 Base de Données
*   **ORM :** Utilisation de SQLAlchemy.
*   **Migrations :** Système de "Seed" (`seed_initial_data`) qui peuple la base avec des données par défaut si elle est vide (Admin par défaut, pages SEO de base).
*   **Modèles :** Relations `One-to-One` pour les paramètres SEO par page.

### 3.3 Frontend
*   **Framework CSS :** Tailwind CSS (chargé via CDN pour la flexibilité).
*   **Design System :** Palette de couleurs `primary` (Bleu nuit/Indigo) et `accent` (Vert/Lime).
*   **Polices :** Google Fonts (Poppins).
*   **Icônes :** FontAwesome 6 (CDN).
*   **Responsive :** Menu mobile burger, grilles adaptatives (Grid/Flex).
