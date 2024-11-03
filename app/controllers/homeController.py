# app/controllers/homeController.py

from flask import Blueprint, render_template
from app.services.homeService import HomeService

bp = Blueprint('home', __name__, 
               template_folder='../../templates',
               static_folder='../../static',
               static_url_path='/static')

@bp.route('/')
def index():
    message = HomeService.get_processed_welcome_message()
    return render_template('index.html', message=message)

