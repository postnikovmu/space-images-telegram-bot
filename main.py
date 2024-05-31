import requests


def download_image(url, file_name):
    response = requests.get(url)
    with open(file_name, 'wb') as file:
        file.write(response.content)


def main():
    image_url = 'https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg'
    file_name = 'image.jpg'

    download_image(image_url, file_name)


if __name__ == '__main__':
    main()
    