import requests
import random


def get_random_image_from_mars_rover():
    """
    Returns a random image from the Mars Rover API.
    :return:
    """
    url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key=DEMO_KEY'
    response = requests.get(url)
    response_json = response.json()
    photo_url = response_json['photos'][random.randint(0, len(response_json['photos']) - 1)]['img_src']
    return photo_url
