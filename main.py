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


def main():
    image_url = 'https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg'
    file_name = 'image.jpg'
    dir_name = './images'

    # download_image(url=image_url, file_name=file_name, dir_name=dir_name)

    print(get_spacex_links('5eb87d47ffd86e000604b38a'))


if __name__ == '__main__':
    main()
    