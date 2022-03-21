import coingecko, tools
import time


if __name__ == '__main__':

    first_time = True
    while True:
        coins = coingecko.trending()
        if first_time:
            first_time = False
            tools.send_message(coins)
        else:
            new_coins = [item for item in old_coins if item not in coins]
            if not new_coins:
                continue
            else:      
                tools.send_message(new_coins)

        old_coins = coins
        time.sleep(300)