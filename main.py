import requests
from pathlib import Path
import os


def get_spacex_links(launch_id='latest'):
    response = requests.get(f"https://api.spacexdata.com/v5/launches/{launch_id}")
    response.raise_for_status()
    return response.json()['links']['flickr']['original']


def download_image(url, file_name, dir_name):
    Path(dir_name).mkdir(parents=True, exist_ok=True)
    file_path = os.path.join(dir_name, file_name)
    response = requests.get(url)
    with open(file_path, 'wb') as file:
        file.write(response.content)


def fetch_spacex_last_launch(launch_id='latest'):
    dir_name = './images'

    spacex_links = get_spacex_links(launch_id)
    for link_number, link in enumerate(spacex_links):
        file_name = 'spacex_image_' + str(link_number) + '.jpg'
        download_image(link, file_name, dir_name)
        print( link_number, link)


def main():
    fetch_spacex_last_launch('5eb87d47ffd86e000604b38a')


if __name__ == '__main__':
    main()
    