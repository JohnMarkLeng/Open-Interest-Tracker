import requests 
import json
import os


from dotenv import load_dotenv

load_dotenv()  #created environment variables

key = os.getenv("API_KEY")

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


def get_price_history(**kwargs): 

    url = 'https://api.tdameritrade.com/v1/marketdata/{}/pricehistory'.format(kwargs.get('symbol'))

    params1 = {}
    params1.update({'apikey' : key})

    for arg in kwargs:
        parameter = {arg: kwargs.get(arg)}
        params1.update(parameter)

    return requests.get(url, params = params1).json()



jprint(get_price_history(symbol='AAPL', period =1, periodType = 'day', frequencyType = 'minute'))