# app/main.py

from flask import Flask
from app.controllers.homeController import bp as home_bp
from app.controllers.stocksController import bp as stocks_bp
from static_utils import add_static_route
import os

def create_app():
    static_dir = os.path.abspath('./static')
    templates_dir = os.path.abspath('./templates')

#    app = Flask(__name__, static_folder=static_dir, template_folder=templates_dir)
    app = Flask(__name__, static_folder=None)  # Désactive le gestionnaire de fichiers statiques par défaut
   
    # Ajouter la route statique
    app = add_static_route(app)

    # Enregistrer le blueprint
    app.register_blueprint(home_bp)
    app.register_blueprint(stocks_bp)

    return app


