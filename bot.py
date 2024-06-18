import telegram
import os
from dotenv import load_dotenv


def get_bot_and_chat():
    load_dotenv()
    token = os.environ['TG_BOT_TOKEN']
    chat_id = os.environ['TG_CHANNEL_ID']
    bot = telegram.Bot(token=token)
    return bot, chat_id


def bot_send_message(bot, chat_id, text):
    bot.send_message(text=text, chat_id=chat_id)


def main():
    bot, chat_id = get_bot_and_chat()
    bot_send_message(bot, chat_id, 'Hello')


if __name__ == '__main__':
    main()

