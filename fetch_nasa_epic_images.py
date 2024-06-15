import requests
import datetime
from helpers import download_image, get_nasa_token


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


if __name__ == '__main__':
    nasa_token = get_nasa_token()
    fetch_nasa_epic_images(token=nasa_token, date='2019-05-30')
