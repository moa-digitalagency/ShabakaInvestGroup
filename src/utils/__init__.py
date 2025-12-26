import os
import uuid
from werkzeug.utils import secure_filename
from PIL import Image

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp', 'svg'}
UPLOAD_FOLDER = 'static/uploads'

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def save_uploaded_file(file, category='general'):
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        unique_filename = f"{uuid.uuid4().hex}_{filename}"
        category_folder = os.path.join(UPLOAD_FOLDER, category)
        os.makedirs(category_folder, exist_ok=True)
        filepath = os.path.join(category_folder, unique_filename)
        file.save(filepath)
        return filepath
    return None

def get_placeholder_image(category='office'):
    placeholders = {
        'office': 'https://images.unsplash.com/photo-1497366216548-37526070297c?w=800',
        'team': 'https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=800',
        'cleaning': 'https://images.unsplash.com/photo-1581578731548-c64695cc6952?w=800',
        'construction': 'https://images.unsplash.com/photo-1504307651254-35680f356dfd?w=800',
        'building': 'https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?w=800',
        'meeting': 'https://images.unsplash.com/photo-1542744173-8e7e53415bb0?w=800',
        'consulting': 'https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=800',
    }
    return placeholders.get(category, placeholders['office'])

def slugify(text):
    import re
    text = text.lower().strip()
    text = re.sub(r'[àáâãäå]', 'a', text)
    text = re.sub(r'[èéêë]', 'e', text)
    text = re.sub(r'[ìíîï]', 'i', text)
    text = re.sub(r'[òóôõö]', 'o', text)
    text = re.sub(r'[ùúûü]', 'u', text)
    text = re.sub(r'[ç]', 'c', text)
    text = re.sub(r'[^a-z0-9\s-]', '', text)
    text = re.sub(r'[\s_]+', '-', text)
    text = re.sub(r'-+', '-', text)
    return text.strip('-')
