import requests, time
from pycoingecko import CoinGeckoAPI


cg = CoinGeckoAPI()

def trending():

    js = cg.get_search_trending()
    symbols = []
    n = 0
    for symbol in js['coins']:
        datos = [js['coins'][n]['item']["id"], js['coins'][n]['item']['symbol']]
        symbols.append(datos)
        n += 1
        
    return symbols

def data(coin_id):
    js = cg.get_coin_by_id(coin_id, sparkline=True)

    try:
        category = js["categories"]
        sentiment = js["sentiment_votes_up_percentage"]
        market_cap = js["market_cap_rank"]
        price = js["market_data"]["current_price"]['usd']
        price_1h = round(js["market_data"]["price_change_percentage_1h_in_currency"]['usd'], 2)
        price_24hs = round(js["market_data"]["price_change_percentage_24h"], 2)
        chart = js["market_data"]["sparkline_7d"]["price"]
    except:
        category = '-'
        sentiment = '-'
        price = '-'
        price_1h = '-'
        price_24hs = '-'
        chart = '-'
    
    return price, market_cap, category, sentiment, price_1h, price_24hs, chart


#print(trending())
#data('fantom')
