from helpers import get_nasa_token
from fetch_spacex_images import fetch_spacex_last_launch
from fetch_nasa_images import fetch_nasa_images
from fetch_nasa_epic_images import fetch_nasa_epic_images
import argparse


def main():
    parser = argparse.ArgumentParser(description="downloads images to '.images' folder")

    parser.add_argument("id", nargs='?', default='latest', help='id of specific launch from SpaceX' )
    parser.add_argument("count", nargs='?', default=0, help="pass the count to download photos from NASA")
    parser.add_argument("date", nargs='?', default='', help="pass the argument (YYYY-MM-DD) to download photos "
                                                            "for specific date from NASA Epic")
    args = parser.parse_args()

    nasa_token = get_nasa_token()
    fetch_spacex_last_launch(args.id)  # Example '5eb87d47ffd86e000604b38a'
    fetch_nasa_images(token=nasa_token, count=args.count)  # Example count=2
    fetch_nasa_epic_images(token=nasa_token, date=args.date)  # Example date='2019-05-30'


if __name__ == '__main__':
    main()
