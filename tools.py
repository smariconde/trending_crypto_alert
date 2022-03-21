import telegram
from keys import *

def send_message(text):
    bot = telegram.Bot(token=TELEGRAM_TOKEN)
    bot.sendMessage(chat_id = CHAT_ID, text = text)