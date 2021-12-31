import requests 
import json
import os

from dotenv import load_dotenv

load_dotenv()  #created environment variables

key = os.getenv("API_KEY")


def get_options(**kwargs):

    url = 'https://api.tdameritrade.com/v1/marketdata/chains'

    params = {}
    params.update({'apikey': key})

    for arg in kwargs:
        parameter = {arg: kwargs.get(arg)}
        params.update(parameter)

    return requests.get(url, params=params).json()


