import requests
import os

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
headers = {
    "X-RapidAPI-Key": os.environ.get('RAPID_API_KEY'),
    "X-RapidAPI-Host": "twelve-data1.p.rapidapi.com"
}

def get_market_data():
    response = requests.get(url, headers=headers, params=querystring)
    return response.json()
