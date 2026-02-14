# Shabaka Invest Group - Guide de Déploiement

Ce guide détaille les étapes nécessaires pour installer, configurer et déployer l'application Shabaka Invest Group en production.

## 1. Prérequis

Avant de commencer, assurez-vous de disposer des éléments suivants :
*   **Serveur :** Linux (Ubuntu/Debian recommandé) ou conteneur Docker.
*   **Python :** Version 3.10 ou supérieure.
*   **Base de Données :** PostgreSQL (recommandé pour la prod) ou SQLite (par défaut).
*   **Serveur Web :** Nginx (comme reverse proxy) et Gunicorn (comme serveur WSGI).

---

## 2. Installation

### 2.1 Cloner le projet
```bash
git clone https://github.com/votre-repo/shabaka-invest.git
cd shabaka-invest
```

### 2.2 Créer un environnement virtuel
```bash
python3 -m venv venv
source venv/bin/activate
```

### 2.3 Installer les dépendances
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

## 3. Configuration (Variables d'Environnement)

L'application utilise des variables d'environnement pour sa configuration sensible. Créez un fichier `.env` ou configurez votre hébergeur (Heroku, Render, AWS, etc.).

| Variable | Description | Exemple / Valeur par défaut |
|---|---|---|
| `FLASK_APP` | Point d'entrée de l'app | `main.py` |
| `FLASK_ENV` | Environnement (dev/prod) | `production` |
| `SECRET_KEY` | Clé secrète Flask (Sessions) | `super_secret_string_xyz123` |
| `DATABASE_URL` | URI de connexion BDD | `postgresql://user:pass@localhost:5432/shabaka_db` |
| `ADMIN_USERNAME` | Nom de l'admin par défaut | `Admin Shabaka` |
| `ADMIN_MAIL` | Email de l'admin par défaut | `admin@shabaka.com` |
| `ADMIN_PASSWORD` | Mot de passe admin initial | `ChangeMe123!` |

**Note :** Si `DATABASE_URL` n'est pas défini, l'application utilisera SQLite local (`instance/site.db`).

---

## 4. Initialisation de la Base de Données

Une fois l'environnement configuré, vous devez initialiser la base de données. L'application inclut un script automatique au démarrage (`seed_initial_data` dans `main.py`), mais il est recommandé d'exécuter la commande manuellement lors du premier déploiement pour vérifier les erreurs.

```bash
python init_db.py
```
*Cette commande crée les tables si elles n'existent pas et ajoute l'utilisateur admin par défaut.*

---

## 5. Lancement en Production (Gunicorn)

Ne lancez jamais `python main.py` en production (c'est le serveur de développement Flask). Utilisez **Gunicorn**.

### Commande de lancement
```bash
gunicorn -w 4 -b 0.0.0.0:8000 main:app
```
*   `-w 4` : Nombre de workers (généralement 2-4 x nombre de cœurs CPU).
*   `-b 0.0.0.0:8000` : Bind sur le port 8000.
*   `main:app` : Module `main.py`, instance `app`.

---

## 6. Configuration Nginx (Reverse Proxy)

Configurez Nginx pour rediriger le trafic vers Gunicorn et gérer les fichiers statiques.

Exemple de configuration `/etc/nginx/sites-available/shabaka` :

```nginx
server {
    listen 80;
    server_name shabaka-invest.com www.shabaka-invest.com;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }

    location /static {
        alias /var/www/shabaka-invest/static;
    }
}
```

---

## 7. Maintenance et Mises à jour

Pour mettre à jour l'application :
1.  `git pull origin main`
2.  `pip install -r requirements.txt` (si nouvelles dépendances)
3.  `python init_db.py` (si migrations nécessaires - le script gère l'ajout de colonnes manquantes)
4.  Redémarrer le service Gunicorn : `sudo systemctl restart shabaka`
