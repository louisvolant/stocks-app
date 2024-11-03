# stocks-app
Small app to show stocks

## Requirements

1. First install the required packages

Python3, logging, argparse, requests, datetime

````
python3 -m venv myenv
source myenv/bin/activate // on MacOS
source myenv/Scripts/activate // on Windows
pip install -r requirements.txt
````

2. Api Key

You also need to have a API key working from Stocks Apps

Once you have it, put it into your env variables :
````
export STOCKS_APP_SECRET_KEY = '000000000000000000000000'
````

## How to execute

Go in the same folder than the python script

````
$ python3 run.py 
````