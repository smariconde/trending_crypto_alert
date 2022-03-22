from unicodedata import category
import requests
import pandas as pd
from pycoingecko import CoinGeckoAPI


cg = CoinGeckoAPI()

def trending():
    try:
        js = cg.get_search_trending()
        symbols = []
        n = 0
        for symbol in js['coins']:
            datos = [js['coins'][n]['item']["id"], js['coins'][n]['item']['symbol']]
            symbols.append(datos)
            n += 1
    except:
        raise
        
    return symbols

def data(coin_id):
    js = cg.get_coin_by_id(coin_id)
    try:
        category = js["categories"]
        sentiment = js["sentiment_votes_up_percentage"]
        price = js["market_data"]["current_price"]['usd']
        price_1h = js["market_data"]["price_change_percentage_1h_in_currency"]['usd']
        price_24hs = js["market_data"]["price_change_percentage_24h"]
    except:
        category = '-'
        sentiment = '-'
        price = '-'
        price_1h = '-'
        price_24hs = '-'
    
    return category, sentiment, price, price_1h, price_24hs


#print(trending())
#data('fantom')
