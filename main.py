from operator import ne
import coingecko, tools
import time


if __name__ == '__main__':
    first_time = True
    while True:
        coins = coingecko.trending()
        # print(coins)
        if first_time:
            first_time = False
            tools.send_message(coins)
        else:
            new_coins = [item for item in old_coins if item not in coins]
            # print(new_coins)
            if not new_coins:
                time.sleep(300)
                continue
            else:
                for new_coin in new_coins:
                    try:
                        datos = coingecko.data(new_coin[0])
                        tools.send_message(f'{new_coin[1]}\nTipo: {datos[0][0]}\nSentiment: {datos[1]}%\nPrice: {datos[2]}\n1hr: {datos[3]}%\n24hs: {datos[4]}%')
                    except:
                        continue
        old_coins = coins
        time.sleep(300)