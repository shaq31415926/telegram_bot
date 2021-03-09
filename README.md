# Build your first bot in Telegram with Python in only 10 minutes

## Steps:
1. Do you have the Desktop Version of Telegram? If yes, move to step 2 otherwise download Telegram.

2. Create a new bot in BotFather. Go to [BotFather](https://telegram.me/BotFather)

* Go to the BotFather, then create new bot by sending the `/newbot` command. 
* Follow the steps until you get the **username** and **token** for your bot.
* You can go to your bot by accessing this URL: https://telegram.me/YOUR_BOT_USERNAME.

3. Open up a Python Integrated Development Environment of your choice.

For the pupose of the workshop you could also sign up for a Cloud IDE: https://codeanywhere.com/

4. If you are using codeanywhere, create a new connection, give it a funky name and select one of the Python stacks. Otherwise skip this step.

5. Open the terminal to clone the repo and go into the cloned directory:

* `git clone https://github.com/shaq31415926/telegram_bot.git`

* `cd telegram_bot`

6. Install the requirements in the terminal.

`pip install -r requirements.txt`

7. Update the variable YOUR_TOKEN with **your Telegram token**.

* dog_bot.py <- Script to create a simple bot which generates random dog images
* simple_bot.py <- Script to create a simple bot which repeats what you enter
* ai_bot.py <- Script to create an intelligent bot which is learning to answer your questions.


8. Run the program in the terminal.

* `TELEGRAM_TOKEN=<YOUR TOKEN> python dog_bot.py`

* `TELEGRAM_TOKEN=<YOUR TOKEN> python simple_bot.py`

* `TELEGRAM_TOKEN=<YOUR TOKEN> python ai_bot.py`

9. Open your Telegram Bot, and enter the ```/start``` command

### Docker

You could also replace steps 6 to 8 with this, if you prefer to use Docker.

```bash 
docker build -t telegram_bot .
docker run -e TELEGRAM_TOKEN=<YOUR TOKEN> telegram_bot
```


