import requests 
import json

key = 'OWBDRKYAEFZN2AW5DJ6SBCIOIODQBQSZ'


def get_options(**kwargs):

    url = 'https://api.tdameritrade.com/v1/marketdata/chains'

    params = {}
    params.update({'apikey': key})

    for arg in kwargs:
        parameter = {arg: kwargs.get(arg)}
        params.update(parameter)

    return requests.get(url, params=params).json()


