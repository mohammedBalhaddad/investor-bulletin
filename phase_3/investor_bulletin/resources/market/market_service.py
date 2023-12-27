import requests
import os

from sqlalchemy import null

""" Market Service """
"""_summary_
this file to write any business logic for the Market
"""

url = "https://twelve-data1.p.rapidapi.com/price"
querystring = {
    "symbol":"AAPL,MSFT,GOOG,AMZN,META",
    "format":"json",
    "outputsize":"30"
}


def get_market_data():
    response = requests.get(url, headers={
        "X-RapidAPI-Key": os.environ.get('RAPID_API_KEY'),
        "X-RapidAPI-Host": "twelve-data1.p.rapidapi.com"
    }, params=querystring)
    print(response.status_code)
    response_json = response.json()
    if 'code' in response_json:
        return null ;
    else:
        return response_json
