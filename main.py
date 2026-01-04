import os
from flask import Flask
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
from modeles import db, User
from security import login_manager
from routes.public import public_bp
from routes.admin import admin_bp
from services import seed_initial_data

app = Flask(__name__, template_folder='templates', static_folder='static')
app.secret_key = os.environ.get("SESSION_SECRET")
if not app.secret_key:
    raise RuntimeError("SESSION_SECRET environment variable is required")

# Admin credentials from environment variables
ADMIN_USERNAME = os.environ.get("ADMIN_USERNAME")
ADMIN_MAIL = os.environ.get("ADMIN_MAIL")
ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD")

csrf = CSRFProtect(app)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
    "pool_recycle": 300,
    "pool_pre_ping": True,
}
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024

db.init_app(app)
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

app.register_blueprint(public_bp)
app.register_blueprint(admin_bp)

@app.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

with app.app_context():
    db.create_all()
    seed_initial_data()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)