import coingecko, tools
import time, requests


if __name__ == '__main__':
    first_time = True
    n = 0
    while True:
        try:
            coins = coingecko.trending()
        except requests.exceptions.ConnectionError:
            time.sleep(300)
            continue

        if first_time:
            first_time = False
            tools.send_message(coins)
        else:
            new_coins = [item for item in old_coins if item not in coins]
            
            if not new_coins:
                time.sleep(300)
                continue
            else:
                n += 1
                for new_coin in new_coins:
                    try:
                        datos = coingecko.data(new_coin[0])
                        tools.sparkline(datos[6])
                        tools.send_chart(f'{new_coin[1]}\nPrice: {datos[0]} U$S\n#: {datos[1]}\nTipo: {datos[2][0]}\nSentiment: {datos[3]}%\n1hr: {datos[4]}%\n24hs: {datos[5]}%')
                        print(f'Mensaje enviado: {n}')
                    except:
                        print('Error en datos')
                        continue
        old_coins = coins
        time.sleep(300)


# datos = coingecko.data('ethereum')
# tools.sparkline(datos[5])
# tools.send_chart(f'ethereum\nTipo: {datos[0][0]}\nSentiment: {datos[1]}%\nPrice: {datos[2]}\n1hr: {datos[3]}%\n24hs: {datos[4]}%')