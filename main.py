import requests
from pathlib import Path
from urllib.parse import urlsplit, unquote
from os.path import split, splitext
import os
import datetime
from dotenv import load_dotenv


def get_spacex_links(launch_id='latest'):
    response = requests.get(f"https://api.spacexdata.com/v5/launches/{launch_id}")
    response.raise_for_status()
    return response.json()['links']['flickr']['original']


def download_image(url, file_name, dir_name, extension='.jpg', token=''):
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


def fetch_spacex_last_launch(launch_id='latest'):
    spacex_links = get_spacex_links(launch_id)
    for link_number, link in enumerate(spacex_links):
        file_name = 'spacex_image_' + str(link_number)
        download_image(link, file_name, './images', '.jpg')
        print(link_number, link)


def get_link_image_extension(link):
    splitted_result = urlsplit(link)
    unquoted_result = unquote(splitted_result.path)
    extension = splitext(split(unquoted_result)[-1])[-1]
    return extension


def fetch_nasa_images(token, count):
    params = {
        'api_key': token,
    }
    if count:
        params.update({'count': count})
    response = requests.get("https://api.nasa.gov/planetary/apod", params=params)
    response.raise_for_status()
    response_data = response.json()
    nasa_links = []
    if count:
        for row in response_data:
            nasa_links.append(row['url'])
    else:
        nasa_links.append(response_data['url'])
    for link_number, link in enumerate(nasa_links):
        file_name = 'nasa_image_' + str(link_number)
        download_image(link, file_name, './images', get_link_image_extension(link))
        print(link_number, link)


def get_nasa_token():
    load_dotenv()
    token = os.environ['NASA_TOKEN']
    return token


def fetch_nasa_epic_images(token, date):
    params = {
        'api_key': token,
    }
    response = requests.get(f"https://api.nasa.gov/EPIC/api/natural/date/{date}", params=params)
    response.raise_for_status()
    response_data = response.json()
    nasa_links = []
    for row in response_data:
        image_name = row.get('image')
        image_item_date = row.get('date')
        image_datetime = datetime.datetime.strptime(image_item_date, '%Y-%m-%d %H:%M:%S')
        image_date = image_datetime.date()
        str_image_date = image_date.strftime('%Y/%m/%d')
        nasa_link = f"https://api.nasa.gov/EPIC/archive/natural/{str_image_date}/png/{image_name}.png"
        nasa_links.append(nasa_link)

    for link_number, link in enumerate(nasa_links):
        file_name = 'nasa_epic_image_' + str(link_number)
        download_image(link, file_name, './images', '.png', token=token)
        print(link_number, link)


def main():
    nasa_token = get_nasa_token()
    # fetch_spacex_last_launch('5eb87d47ffd86e000604b38a')
    # fetch_nasa_images(count=2, token=nasa_token)
    fetch_nasa_epic_images(token=nasa_token, date='2019-05-30')


if __name__ == '__main__':
    main()
