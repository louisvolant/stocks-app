from app.main import create_app
from app.services.stocksService import StocksService

# README
# execute with
# python3 -m venv myenv
# source myenv/bin/activate # on MacOS
# source myenv/Scripts/activate # on Windows
# pip install -r requirements.txt
# python3 run.py
# Once finished, simply desactivate the virtual environment using "deactivate"


app = create_app()

if __name__ == '__main__':
    #StocksService.fetch_cac40_data()
    app.run(debug=True, port=8080)
