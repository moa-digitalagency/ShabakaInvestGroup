from functools import wraps
from flask import redirect, url_for, flash, session
from flask_login import LoginManager, current_user
from werkzeug.security import generate_password_hash, check_password_hash

login_manager = LoginManager()
login_manager.login_view = 'admin.login'
login_manager.login_message = 'Veuillez vous connecter pour accéder à cette page.'
login_manager.login_message_category = 'warning'

def hash_password(password):
    return generate_password_hash(password, method='pbkdf2:sha256')

def verify_password(password_hash, password):
    return check_password_hash(password_hash, password)

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated:
            flash('Veuillez vous connecter.', 'warning')
            return redirect(url_for('admin.login'))
        if current_user.role != 'admin':
            flash('Accès non autorisé.', 'danger')
            return redirect(url_for('public.home'))
        return f(*args, **kwargs)
    return decorated_function
