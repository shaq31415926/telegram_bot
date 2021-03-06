# import libraries
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

YOUR_TOKEN = 'INSERT_YOUR_TOKEN'


# Processing commands
def start(update, context):
    """When the user enters start the following message will appear"""
    context.bot.sendMessage(chat_id=update.message.chat_id, text='Hello, how are you')


def bot_response(update, context):
    """When the user types a message the bot will give the following response"""
    response = 'Got your message: ' + update.message.text
    context.bot.sendMessage(chat_id=update.message.chat_id, text=response)


def main():
    """Run the Program
    
    A very simple bot that echoes the message the user inputs
    """
    # Create the Updater and pass it your bot's token.
    updater = Updater(YOUR_TOKEN, use_context=True)
    # Get the dispatcher to register handlers
    dp = updater.dispatcher
    # Add handlers to the dispatch
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(MessageHandler(Filters.text, bot_response))
    # Getting Started for Updates
    updater.start_polling()
    # Stop the bot if Ctrl + C was pressed
    updater.idle()


if __name__ == '__main__':
    main()
