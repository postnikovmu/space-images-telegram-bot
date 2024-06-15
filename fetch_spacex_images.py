import requests
from helpers import download_image, get_nasa_token


def get_spacex_links(launch_id='latest'):
    response = requests.get(f"https://api.spacexdata.com/v5/launches/{launch_id}")
    response.raise_for_status()
    return response.json()['links']['flickr']['original']


def fetch_spacex_last_launch(launch_id='latest'):
    spacex_links = get_spacex_links(launch_id)
    for link_number, link in enumerate(spacex_links):
        file_name = 'spacex_image_' + str(link_number)
        download_image(link, file_name, './images', '.jpg')
        print(link_number, link)


if __name__ == '__main__':
    nasa_token = get_nasa_token()
    fetch_spacex_last_launch('5eb87d47ffd86e000604b38a')
