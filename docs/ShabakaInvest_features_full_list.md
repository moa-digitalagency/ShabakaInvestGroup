[ 🇫🇷 Français ](ShabakaInvest_features_full_list.md) | [ 🇬🇧 English ](ShabakaInvest_features_full_list_en.md)

# Bible des Fonctionnalités - Shabaka Invest Group

Ce document recense de manière exhaustive toutes les fonctionnalités techniques et métier implémentées dans le projet **Shabaka Invest Group**. Il sert de référence absolue pour les développeurs et chefs de projet.

---

## 1. Administration & Back-Office
L'interface d'administration est sécurisée et accessible via `/admin`.

### A. Dashboard (`/admin/`)
- **Statistiques en temps réel :** Nombre de services, témoignages, contacts totaux et non lus.
- **Activité récente :** Affichage des 5 derniers messages de contact reçus.
- **Navigation latérale :** Accès rapide à tous les modules de gestion.

### B. Gestion des Services (CRUD)
- **Liste :** Vue tabulaire avec possibilité de tri (drag & drop via champ `order`).
- **Création/Édition :**
  - Nom du service.
  - Slug généré automatiquement (modifiables).
  - Description courte (pour les cartes) et longue (HTML autorisé).
  - Icône (FontAwesome).
  - Image de couverture (Upload avec gestion de chemin).
  - Liste de fonctionnalités (liste à puces).
  - Statut : Actif/Inactif, Mis en avant (Featured).
- **Suppression :** Action irréversible avec confirmation.

### C. Gestion des Témoignages
- **Champs :** Nom auteur, Entreprise, Poste, Photo, Contenu, Note (1-5 étoiles).
- **Options :** Mise en avant sur la page d'accueil.

### D. Gestion des Contacts (CRM Léger)
- **Réception :** Stockage en base de données de toutes les soumissions de formulaire.
- **Suivi :** Marquage automatique "Lu/Non lu" à l'ouverture.
- **Détails :** Vue complète du message, informations de contact et service d'intérêt.

### E. Configuration Globale (`/admin/settings`)
- **Identité du site :** Nom, Logo, Favicon.
- **Coordonnées :** Email, Téléphone, Adresse, WhatsApp (support).
- **Réseaux Sociaux :** Liens Facebook, LinkedIn, Instagram, Twitter, YouTube.
- **Scripts Tiers :** Injection de code dans `<head>` et `<footer>` (Google Analytics, Pixel).

### F. Médiathèque
- **Upload :** Chargement de fichiers images/PDF.
- **Organisation :** Catégorisation automatique (services, testimonials, general).
- **Gestion :** Suppression de fichiers physiques et entrées BDD.

### G. Gestion SEO Avancée (`/admin/seo`)
- **Par Page :** Configuration méta-titre, description, mots-clés pour chaque type de page (Home, Services, Contact, etc.).
- **Open Graph :** Titre, Description et Image pour le partage social.
- **Robots & Canonical :** Configuration fine par page.

---

## 2. Front-Office (Public)

### A. Page d'Accueil Dynamique
- **Hero Section :** Titre, sous-titre, CTA et image de fond configurables.
- **Services en Vedette :** Affichage automatique des services marqués "Featured".
- **Témoignages :** Carrousel des avis clients validés.
- **Métriques :** Affichage de chiffres clés (Clients, Années, Satisfaction).

### B. Pages de Contenu
- **Services :** Liste complète et pages de détail (`/services/<slug>`).
- **Pages Statiques :** A propos, Mentions Légales.
- **Landing Pages Spéciales :** Domiciliation, Conseils (avec templates dédiés).

### C. Formulaire de Contact
- **Validation :** Champs obligatoires (Nom, Email, Message).
- **Feedback :** Messages flash (Succès/Erreur).
- **Sécurité :** Protection CSRF intégrée.

### D. Optimisation Technique (SEO)
- **Sitemap XML :** Génération dynamique à `/sitemap.xml` incluant toutes les pages de services actives.
- **Robots.txt :** Génération dynamique à `/robots.txt` excluant l'admin et les uploads.
- **Metadatas :** Injection dynamique des titres/descriptions depuis la BDD.

---

## 3. Sécurité & Infrastructure

### A. Authentification
- **Framework :** Flask-Login.
- **Modèle User :** Gestion des administrateurs avec hachage de mot de passe sécurisé.
- **Protection Routes :** Décorateur `@login_required` et `@admin_required` sur tout le back-office.

### B. Protection des Données
- **CSRF :** Protection globale via `Flask-WTF` sur tous les formulaires POST.
- **Uploads :** Renommage sécurisé des fichiers (UUID/Timestamp) pour éviter les collisions et exécutions malveillantes.
- **Entêtes HTTP :** Cache-Control strict pour éviter la mise en cache des pages admin.

### C. Base de Données
- **ORM :** SQLAlchemy.
- **Migrations :** Script `init_db.py` avec introspection pour mises à jour de schéma sans perte de données.
- **Initialisation :** Seed automatique des données par défaut si la base est vide.
