from helpers import get_nasa_token
from fetch_spacex_images import fetch_spacex_last_launch
from fetch_nasa_images import fetch_nasa_images
from fetch_nasa_epic_images import fetch_nasa_epic_images


def main():
    nasa_token = get_nasa_token()
    fetch_spacex_last_launch('5eb87d47ffd86e000604b38a')
    fetch_nasa_images(count=2, token=nasa_token)
    fetch_nasa_epic_images(token=nasa_token, date='2019-05-30')


if __name__ == '__main__':
    main()
