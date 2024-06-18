import telegram
import os
from dotenv import load_dotenv
from helpers import get_files_list


def get_bot_and_chat():
    load_dotenv()
    token = os.environ['TG_BOT_TOKEN']
    chat_id = os.environ['TG_CHANNEL_ID']
    bot = telegram.Bot(token=token)
    return bot, chat_id


def send_message(bot, chat_id, text):
    bot.send_message(text=text, chat_id=chat_id)


def send_file(bot, chat_id, file_name):
    with open(file_name, 'rb') as file_to_send:
        bot.send_document(chat_id=chat_id, document=file_to_send)


def main():
    bot, chat_id = get_bot_and_chat()
    # send_message(bot, chat_id, 'Hello')
    files_list = get_files_list('./images')
    if files_list:
        send_file(bot, chat_id, files_list[0])


if __name__ == '__main__':
    main()
