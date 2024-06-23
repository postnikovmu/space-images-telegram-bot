import telegram
import argparse
import os
import time
import random
from dotenv import load_dotenv
from helpers import get_files_list
import logging
import telegram.error as tg_error


def get_settings():
    load_dotenv()
    token = os.environ['TG_BOT_TOKEN']
    chat_id = os.environ['TG_CHANNEL_ID']
    period = float(os.environ.get('POST_PERIOD', '4'))
    bot = telegram.Bot(token=token)
    return bot, chat_id, period


def send_file(bot, chat_id, file_name):
    with open(file_name, 'rb') as file_to_send:
        bot.send_document(chat_id=chat_id, document=file_to_send)


def send_all_files(bot, chat_id, files_list, period):
    for file_name in files_list:
        send_file(bot, chat_id, file_name)
        time.sleep(period)


def main():
    bot, chat_id, default_period = get_settings()

    parser = argparse.ArgumentParser(description='posts images from "image" folder to telegram channel')
    parser.add_argument("period", nargs='?', type=float, default=default_period,
                        help='Period of photo posting, hours (positive float number). Default = 4h.')
    args = parser.parse_args()
    period = args.period * 3600

    files = get_files_list('images')
    if not files:
        logging.error('The directory with images is empty')
        exit(1)

    while True:
        try:
            send_all_files(bot, chat_id, files, period)
            random.shuffle(files)
        except tg_error.NetworkError as e:
            logging.info('There was no internet connection')
            time.sleep(2)


if __name__ == '__main__':
    main()
