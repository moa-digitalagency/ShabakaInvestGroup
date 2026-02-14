from flask import Blueprint, render_template
from config import WHATSAPP_NUMBER, LEAD_MAGNET_URL, SUPPORT_TEXT

errors_bp = Blueprint('errors', __name__)

@errors_bp.app_errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html',
                           whatsapp_number=WHATSAPP_NUMBER,
                           lead_magnet_url=LEAD_MAGNET_URL,
                           support_text=SUPPORT_TEXT), 404

@errors_bp.app_errorhandler(451)
def unavailable_for_legal_reasons(e):
    return render_template('errors/451.html',
                           whatsapp_number=WHATSAPP_NUMBER,
                           lead_magnet_url=LEAD_MAGNET_URL), 451

@errors_bp.app_errorhandler(400)
def bad_request(e):
    return render_template('errors/400.html',
                           whatsapp_number=WHATSAPP_NUMBER,
                           lead_magnet_url=LEAD_MAGNET_URL), 400

@errors_bp.app_errorhandler(403)
def forbidden(e):
    return render_template('errors/403.html',
                           whatsapp_number=WHATSAPP_NUMBER,
                           lead_magnet_url=LEAD_MAGNET_URL), 403
