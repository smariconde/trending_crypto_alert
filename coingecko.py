import requests
import pandas as pd

main_url = 'https://api.coingecko.com/api/v3'

def trending():
    url = main_url + '/search/trending'
    try:
        r = requests.get(url)
        js = r.json()
        symbols = []
        n = 0
        for symbol in js['coins']:
            datos = (js['coins'][n]['item']["id"], js['coins'][n]['item']['symbol'])
            symbols.append(datos)
            n += 1

    except:
        print(f'\nRespuesta del request: {r}\n')
        raise
        
    return symbols

def data(id):
    url = main_url + '/coins/'+ id + '?tickers=false&market_data=false&community_data=false&developer_data=false&sparkline=false'
    r = requests.get(url)
    js = r.json()
    print(url)
    return js


#print(trending())
#print(data('fantom'))
