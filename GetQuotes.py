import requests
import json


key = 'OWBDRKYAEFZN2AW5DJ6SBCIOIODQBQSZ'

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


def get_quotes(**kwargs):

    url = 'https://api.tdameritrade.com/v1/marketdata/quotes'

    params = {}

    params.update({'apikey': key})

    symbol_list = []

    for sym in kwargs.get('symbol'):
        symbol_list.append(sym)

    params.update({'symbol': symbol_list})

    return requests.get(url, params=params).json()


#The command to use this function: 
jprint(get_quotes(symbol =['AAPL', 'TSLA', 'NVAX', 'AMD']))


#function for open high low and close that uses get_quotes function
def get_ohlc(**kwargs):
    data = get_quotes(symbol = kwargs.get('symbol'))
    for symbol in kwargs.get('symbol'):
        print(symbol)
        print("open price:", data[symbol]['openPrice'], " high price:", data[symbol]['highPrice'], 
        " low price:", data[symbol]['lowPrice']," close price:", data[symbol]['closePrice'])

get_ohlc(symbol= ['AAPL','TSLA','NVAX','AMD'])