import requests
from pathlib import Path
from urllib.parse import urlsplit, unquote
from os.path import split, splitext
import os
from dotenv import load_dotenv


def download_image(url, file_name, dir_name, extension='.jpg', token=None):
    full_file_name = file_name + extension
    Path(dir_name).mkdir(parents=True, exist_ok=True)
    file_path = os.path.join(dir_name, full_file_name)
    if token:
        params = {
            'api_key': token,
        }
        response = requests.get(url, params=params)
    else:
        response = requests.get(url)
    response.raise_for_status()
    with open(file_path, 'wb') as file:
        file.write(response.content)


def get_link_image_extension(link):
    splitted_result = urlsplit(link)
    unquoted_result = unquote(splitted_result.path)
    extension = splitext(split(unquoted_result)[-1])[-1]
    return extension


def get_nasa_token():
    load_dotenv()
    token = os.environ['NASA_TOKEN']
    return token


def get_files_list(folder):
    files = []
    for root, dirs, files in os.walk(folder):
        for file in files:
            files.append(os.path.join(root, file))
    return files
