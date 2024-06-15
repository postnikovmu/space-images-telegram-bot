import requests
from helpers import download_image, get_nasa_token, get_link_image_extension


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


if __name__ == '__main__':
    nasa_token = get_nasa_token()
    fetch_nasa_images(count=2, token=nasa_token)
