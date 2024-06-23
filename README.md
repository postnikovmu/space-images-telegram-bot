# space-images-telegram-bot
telegram bot for publishing images of space

## Getting Started
Run appropriate script
```
python fetch_spacex_images.py
python fetch_nasa_images.py
python fetch_nasa_epic_images.py '2019-05-30'
python post_images_with_bot.py 0.0001
```

### Prerequisites
1. Crete a bot in telegram using https://t.me/BotFather.
2. Create a channel in telegram.
3. Add your bot to your channel as administrator.
4. Create environment variables in "your_project_folder\.env" file:
   NASA_TOKEN=  <- generate your "API Key" on https://api.nasa.gov/
   TG_BOT_TOKEN= <- token for your telegram bot
   TG_CHANNEL_ID= <- id of your tg channel
   
   optional:
   POST_PERIOD= <- default period of posting images, hours. Default value = 4. 
   
5. Python3 should be already installed.
   Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```
   -> packages, listed in requirements should be successfully installed. 

### Usage
1. "fetch_spacex_images.py" downloads the latest image of SpaceX launch to .images folder. 
   You may pass the argument "id" to download photos of specific launch, example: '5eb87d47ffd86e000604b38a'

2. "fetch_nasa_images.py" downloads image of current date to ".images" folder
   from https://apod.nasa.gov/apod/astropix.html.
   You may pass the argument count to download certain number of the photos.

3. "fetch_nasa_epic_images.py" downloads image of current date to ".images" folder
   from https://epic.gsfc.nasa.gov/
   You may pass the argument date (YYYY-MM-DD) to download photos from specific date.

4. "post_images_with_bot.py" posts images from ".images" folder to "TG_CHANNEL_ID"
   telegram channel every "POST_PERIOD" hours. When all images were posted, it starts posting the same
   images again in random sequence.
   You may change the period of posting by passing an argument "period" in hours.
