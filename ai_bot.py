# import libraries
import re
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity, linear_kernel
import nltk
import wikipedia as wk
import warnings
from src.text_processing import Normalize

warnings.filterwarnings("ignore")

YOUR_TOKEN = 'INSERT_YOUR_TOKEN'


# Processing commands
def start(update, context):
    """When the user enters start the following message will appear"""
    
    context.bot.sendMessage(chat_id=update.message.chat_id,
                            text='Hello! My Name is ChatterBot and I am your very own AI Bot. What would you like to know?')


# read the input data
def tokenize_input_data():
    """Tokenizes the raw data"""
    
    data = open('data/UN.txt', 'r', errors='ignore')
    raw = data.read()
    raw = raw.lower()  #
    sent_tokens = nltk.sent_tokenize(raw)

    return sent_tokens


def generate_response(user_response):
    """Reads the user input and prepares the output"""
    
    robo_response = ''
    sent_tokens = tokenize_input_data()
    sent_tokens.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=Normalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    # vals = cosine_similarity(tfidf[-1], tfidf)
    vals = linear_kernel(tfidf[-1], tfidf)
    idx = vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if (req_tfidf == 0) or "tell me about" in user_response:
        print("Checking Wikipedia")
        if user_response:
            robo_response = wikipedia_data(user_response)
            return robo_response
    else:
        robo_response = robo_response + sent_tokens[idx]
        return robo_response  # wikipedia search


def wikipedia_data(input):
    """Accesses and parse data from Wikipedia"""
    
    reg_ex = re.search('tell me about (.*)', input)
    try:
        if reg_ex:
            topic = reg_ex.group(1)
            wiki = wk.summary(topic, sentences=3)
            return wiki
    except Exception as e:
        print("No content has been found")


def bot_response(update, context):
    """When the user types a message the bot will give a response based on the user's input"""
    
    user_response = update.message.text
    user_response = user_response.lower()
    if user_response not in ['bye', 'shutdown', 'exit', 'quit']:
        if user_response == 'thanks' or user_response == 'thank you':
            print("You are welcome :)")
        else:
            response = generate_response(user_response)
    else:
        print("Bye!!!")
    context.bot.sendMessage(chat_id=update.message.chat_id, text=response)


def main():
    """Run the Program
    
    An Intelligent Bot that learns from the input data (data/UN.txt) and also queries wikipedia
    
    """
    
    updater = Updater(YOUR_TOKEN, use_context=True)
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

# References
# https://www.kdnuggets.com/2019/12/build-intelligent-chatbot.html
#
