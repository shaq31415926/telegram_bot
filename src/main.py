import requests
import re
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url


def bop(update, context):
    print("reached bop")
    url = get_url()
    context.bot.send_photo(chat_id=update.effective_chat.id, photo = url)


def main():
    updater = Updater('1685425164:AAEgCJeeN61T-S0UJUH7lchizjC_ft-5tuc', use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

