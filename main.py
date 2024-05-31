import requests
from pathlib import Path
import os


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

    download_image(url=image_url, file_name=file_name, dir_name=dir_name)


if __name__ == '__main__':
    main()
    