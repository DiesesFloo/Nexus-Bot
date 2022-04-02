import sys
sys.path.append("..")

import requests
import json



def get_apod_image():
    """
    Get the Astronomy Picture of the Day from the APOD API.
    """
    output = []

    apod_api_url = "https://api.nasa.gov/planetary/apod"
    apod_api_key = json.load(open('apikeys.json'))['nasa']
    apod_api_url = apod_api_url + "?api_key=" + apod_api_key
    apod_image = requests.get(apod_api_url).json()

    output.append(apod_image['title'])
    output.append(apod_image['explanation'])
    output.append(apod_image['hdurl'])
    output.append(apod_image['copyright'])

    return output


def get_id_of_parameter(parameter: str):
    """
    Returns the ids for the given parameter for the get_apod_image function.
    :param parameter:
    :return: Index of the parameter.
    """
    if parameter == 'title':
        return 0
    elif parameter == 'explanation':
        return 1
    elif parameter == 'url':
        return 2
    elif parameter == 'copyright':
        return 3
    else:
        return None
