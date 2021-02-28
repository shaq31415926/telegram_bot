import requests
import re
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

YOUR_TOKEN = 'TO_INSERT'


def get_url():
    """Access the API and get the image URL"""
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    return url


def start(update, context):
    """Send the image"""
    print("reached bop")
    url = get_url()
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=url)


def main():
    """Run the Program"""
    updater = Updater(YOUR_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
