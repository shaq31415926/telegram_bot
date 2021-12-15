import os

import requests
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

YOUR_TOKEN = os.getenv("TELEGRAM_TOKEN")


def get_content():
    """Access the API and get the image URL"""
    contents = requests.get('https://cataas.com//cat')
    # contents = requests.get('https://cataas.com//cat/gif')
    return contents.content


def start(update, context):
    """The command the bot carries out when starting the bot"""
    print("reached bop")
    content = get_content()
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=content)
    # context.bot.send_video(chat_id=update.effective_chat.id, video=content)


def main():
    """Run the Program
    
    Every time you enter the command /start the bot will return a random image of a cat
    """
    updater = Updater(YOUR_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
