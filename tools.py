import telegram
from keys import *
import matplotlib
import matplotlib.pyplot as plt

def send_message(text):
    bot = telegram.Bot(token=TELEGRAM_TOKEN)
    bot.sendMessage(chat_id = CHAT_ID, text = text)

def send_chart(caption):
    bot = telegram.Bot(token=TELEGRAM_TOKEN)
    bot.sendPhoto(chat_id= CHAT_ID, photo= open('chart.png', 'rb'), caption= caption)

def sparkline(prices):
    
    plt.rcParams["figure.figsize"] = (21,5)
    plt.xticks([])
    plt.yticks([])
    plt.box(False)
    plt.plot(prices, linewidth=4, color='darkmagenta')
    
    # plt.show()
    plt.savefig('chart.png', bbox_inches='tight')
