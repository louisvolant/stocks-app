# app/controllers/stocksController.py

from flask import Blueprint, render_template, jsonify
from app.services.stocksService import StocksService
from app.data.asset import Asset

bp = Blueprint('stocks', __name__, 
               template_folder='../../templates',
               static_folder='../../static',
               static_url_path='/static')

@bp.route('/stocks')
def index():
    stocks_data = StocksService.get_listing_status()
    print(f"Il y a actuellement : {len(stocks_data)} éléments à afficher")
    print(stocks_data)
    return render_template('stocks.html', assets=stocks_data)

