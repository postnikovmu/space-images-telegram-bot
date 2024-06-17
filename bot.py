import telegram
import os
from dotenv import load_dotenv


def main():
    load_dotenv()
    token = os.environ['TG_BOT_TOKEN']
    chat_id = os.environ['TG_CHANNEL_ID']
    bot = telegram.Bot(token=token)
    bot.send_message(text='Hi from Alec!', chat_id=chat_id)


if __name__ == '__main__':
    main()

