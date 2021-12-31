
import requests
import json 

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, indent=6)
    print(text)

from GetOptionsData import *

from datetime import datetime, date, timedelta 
startDate = date.today()
endDate = startDate + timedelta(weeks = 2)
print("Start Date:", startDate)
print("End Date:  ", endDate)


symbol_list = ["AAPL"]



for symbol in symbol_list: 

    Options_Chain = (get_options(symbol = symbol, includeQuotes = 'TRUE', strikeCount = "2", strategy = 'ANALYTICAL',
            range = 'ALL', fromDate = startDate, toDate = endDate))
        
    jprint(Options_Chain)


print(type(Options_Chain))



