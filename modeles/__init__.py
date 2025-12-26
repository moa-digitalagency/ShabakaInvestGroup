from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from datetime import datetime

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(20), default='admin')
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    last_login = db.Column(db.DateTime)

class Page(db.Model):
    __tablename__ = 'pages'
    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(100), unique=True, nullable=False)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text)
    hero_title = db.Column(db.String(300))
    hero_subtitle = db.Column(db.Text)
    hero_image = db.Column(db.String(500))
    is_published = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    seo_settings = db.relationship('SEOSettings', backref='page', uselist=False, cascade='all, delete-orphan')

class Service(db.Model):
    __tablename__ = 'services'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    slug = db.Column(db.String(100), unique=True, nullable=False)
    short_description = db.Column(db.String(300))
    description = db.Column(db.Text)
    icon = db.Column(db.String(50))
    image = db.Column(db.String(500))
    features = db.Column(db.Text)
    is_featured = db.Column(db.Boolean, default=False)
    order = db.Column(db.Integer, default=0)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class Testimonial(db.Model):
    __tablename__ = 'testimonials'
    id = db.Column(db.Integer, primary_key=True)
    author_name = db.Column(db.String(100), nullable=False)
    author_company = db.Column(db.String(150))
    author_position = db.Column(db.String(100))
    author_image = db.Column(db.String(500))
    content = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer, default=5)
    is_featured = db.Column(db.Boolean, default=False)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class MediaAsset(db.Model):
    __tablename__ = 'media_assets'
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(255), nullable=False)
    original_filename = db.Column(db.String(255))
    file_path = db.Column(db.String(500), nullable=False)
    alt_text = db.Column(db.String(300))
    category = db.Column(db.String(50))
    file_size = db.Column(db.Integer)
    mime_type = db.Column(db.String(100))
    uploaded_at = db.Column(db.DateTime, default=datetime.utcnow)

class SEOSettings(db.Model):
    __tablename__ = 'seo_settings'
    id = db.Column(db.Integer, primary_key=True)
    page_id = db.Column(db.Integer, db.ForeignKey('pages.id'), nullable=True)
    page_type = db.Column(db.String(50))
    meta_title = db.Column(db.String(70))
    meta_description = db.Column(db.String(160))
    keywords = db.Column(db.String(300))
    og_title = db.Column(db.String(100))
    og_description = db.Column(db.String(200))
    og_image = db.Column(db.String(500))
    canonical_url = db.Column(db.String(500))
    robots = db.Column(db.String(50), default='index, follow')
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class ContactSubmission(db.Model):
    __tablename__ = 'contact_submissions'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(30))
    company = db.Column(db.String(150))
    service_interest = db.Column(db.String(100))
    message = db.Column(db.Text, nullable=False)
    is_read = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class SiteSettings(db.Model):
    __tablename__ = 'site_settings'
    id = db.Column(db.Integer, primary_key=True)
    site_name = db.Column(db.String(150), default='Shabaka Invest Group')
    logo = db.Column(db.String(500))
    favicon = db.Column(db.String(500))
    email = db.Column(db.String(120))
    phone = db.Column(db.String(30))
    address = db.Column(db.Text)
    facebook = db.Column(db.String(300))
    linkedin = db.Column(db.String(300))
    instagram = db.Column(db.String(300))
    whatsapp = db.Column(db.String(30))
    footer_text = db.Column(db.Text)
    google_analytics = db.Column(db.String(50))
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class HeroSettings(db.Model):
    __tablename__ = 'hero_settings'
    id = db.Column(db.Integer, primary_key=True)
    badge_text = db.Column(db.String(100), default='Bienvenue chez Shabaka Invest')
    title_main = db.Column(db.String(200), default="Forgez l'avenir de votre")
    title_highlight = db.Column(db.String(100), default='entreprise')
    subtitle = db.Column(db.Text, default='Votre partenaire de confiance à Marrakech pour la domiciliation, création et gestion d\'entreprises au Maroc')
    background_image = db.Column(db.String(500), default='https://images.unsplash.com/photo-1552664730-d307ca884978?w=1600')
    btn1_text = db.Column(db.String(50), default='Nos Services')
    btn1_icon = db.Column(db.String(50), default='fa-lightning-bolt')
    btn1_link = db.Column(db.String(200), default='/services')
    btn2_text = db.Column(db.String(50), default='Devis Gratuit')
    btn2_icon = db.Column(db.String(50), default='fa-arrow-right')
    btn2_is_whatsapp = db.Column(db.Boolean, default=True)
    metric1_value = db.Column(db.String(20), default='500+')
    metric1_label = db.Column(db.String(50), default='Entreprises créées')
    metric1_icon = db.Column(db.String(50), default='fa-chart-line')
    metric2_value = db.Column(db.String(20), default='15+')
    metric2_label = db.Column(db.String(50), default="Ans d'expérience")
    metric2_icon = db.Column(db.String(50), default='fa-trophy')
    metric3_value = db.Column(db.String(20), default='100%')
    metric3_label = db.Column(db.String(50), default='Satisfaction')
    metric3_icon = db.Column(db.String(50), default='fa-star')
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
