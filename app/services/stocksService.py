# app/services/stocksService.py

import requests
import csv
import pickle
import os
import functools
from datetime import datetime, timedelta
from apscheduler.schedulers.background import BackgroundScheduler
from app.data.asset import Asset

# Cache global pour stocker les données de LISTING_STATUS
LISTING_STATUS_CACHE = {
    'assets': None,
    'last_updated': None
}

class StocksService:

    scheduler = BackgroundScheduler()
    scheduler.start()

    def schedule_task(interval):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                scheduler.add_job(
                    func,
                    'interval',
                    minutes=interval,
                    id=func.__name__,
                    replace_existing=True
                )
                return func(*args, **kwargs)
            return wrapper
        return decorator

    @schedule_task(interval=1)
    def fetch_cac40_data():
        API_KEY = os.getenv("STOCKS_APP_SECRET_KEY")
        url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=^FCHI&apikey='+API_KEY
        response = requests.get(url)
        data = response.json()
        
        # Traitement des données ici
        print(data)  # Pour l'exemple, nous affichons simplement les données

    def get_listing_status(force_refresh=False):
        global LISTING_STATUS_CACHE

        API_KEY = os.getenv("STOCKS_APP_SECRET_KEY")
        url = f'https://www.alphavantage.co/query?function=LISTING_STATUS&apikey='+API_KEY

        # Effectuer la requête GET
        response = requests.get(url)

        # Vérifier si la requête a réussi
        if LISTING_STATUS_CACHE['assets'] is None or force_refresh:
            
            if response.status_code == 200:
                response = requests.get(url)
                assets = parse_csv_assets(response)
            else:
                print(f"Erreur lors de la récupération des données: {response.status_code}")

            LISTING_STATUS_CACHE['assets'] = assets
            LISTING_STATUS_CACHE['last_updated'] = datetime.now()
            
            return assets

        else:
            return LISTING_STATUS_CACHE['assets']

def parse_csv_assets(response):
    # Télécharger le fichier CSV
    response.raise_for_status()  # Vérifier si la requête a réussi

    # Lire le contenu CSV
    csv_data = response.text

    # Parser le fichier CSV
    assets = []
    csv_reader = csv.DictReader(csv_data.splitlines())
    for row in csv_reader:
        asset = Asset(
            name=row['name'],
            exchange=row['exchange'],
            assetType=row['assetType'],
            ipoDate=row['ipoDate'],
            delistingDate=row['delistingDate'],
            status=row['status']
        )
        assets.append(asset)

    return assets