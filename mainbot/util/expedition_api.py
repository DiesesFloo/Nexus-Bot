import requests


def get_latest_expedition():
    """
    Returns the latest expedition as list
    :return:
    """
    output = []
    url = "https://ll.thespacedevs.com/2.2.0/expedition/?ordering=-start&limit=1"
    response = requests.get(url)
    expedition_data = response.json()["results"]
    for expedition in expedition_data:
        output.append(expedition["name"])
        output.append(expedition["start"])
        output.append(expedition["end"])
        output.append(expedition['spacestation']["status"]["name"])
        output.append(expedition['spacestation']["image_url"])


def get_id_of_parameter(parameter):
    """
    Returns the ids for the given parameter for the get_latest_expedition function
    :param parameter:
    :return:
    """
    if parameter == "name":
        return 0
    elif parameter == "start":
        return 1
    elif parameter == "end":
        return 2
    elif parameter == "status":
        return 3
    elif parameter == "image_url":
        return 4
    else:
        return None
