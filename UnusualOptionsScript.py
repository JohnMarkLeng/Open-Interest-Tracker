# Open Interest above 100 Mil Scanner 

import requests
import json 
import pandas as pd

#read xls data for stock tickers and make into list
file = r'/Users/JohnLeng/Desktop/Stock Lists/MegaLarge_Jan2021.xls'

complete_list = pd.read_excel(file)
all_symbols_list = complete_list["Symbol"].tolist()
print(all_symbols_list)


def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, indent=6)
    print(text)

from GetOptionsData import *

from datetime import datetime, date, timedelta 
startDate = date.today()
endDate = startDate + timedelta(weeks = 30)
print("Start Date:", startDate)
print("End Date:  ", endDate)


#symbol_list = ["AAPL", "NIO", "TSLA", "PLTR", "XPEV", "NVDA", "BABA"]

def OptionsBuyout_Operation(value):
    amount = value[0]['openInterest'] * value[0]['last'] *100        #100 is compensation for last price in cents
    if amount > 20000000:
        print(amount, value[0]['description'])


#value is a list 
def get_values(putExpDateMap): 
        for key, value in putExpDateMap.items():
            if type(value) is dict: 
                get_values(value)
            elif type(value) is list: 
                OptionsBuyout_Operation(value)
            else:
                print("Error: nothing was found for this ticker")
    
for symbol in all_symbols_list: 

    Options_Chain = (get_options(symbol = symbol, includeQuotes = 'TRUE', strikeCount = "500", strategy = 'ANALYTICAL',
            range = 'ALL', fromDate = startDate, toDate = endDate)) #strikeCount = ""
        
    #putexpmap and callExpDateMap are dict
    if 'putExpDateMap' in Options_Chain.keys():
         putExpDateMap = Options_Chain['putExpDateMap']

    if 'callExpDateMap' in Options_Chain.keys():
         callExpDateMap = Options_Chain['callExpDateMap']

    get_values(putExpDateMap)
    get_values(callExpDateMap)



