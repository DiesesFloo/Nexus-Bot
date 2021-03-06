import requests


def get_next_launch():
    """
    Returns the next launch in form of a list.
    :return: List of information about the next launch.
    """
    output = []

    request = requests.get("https://ll.thespacedevs.com/2.2.0/launch/upcoming/?limit=1")
    launch_data = request.json()['results']

    for keys in launch_data:
        output.append(keys['rocket']['configuration']['full_name'])
        if keys['mission'] == None:
            output.append("N/A")
            output.append("N/A")
            output.append("N/A")
        else:
            output.append(keys['mission']['name'])
            output.append(keys['mission']['type'])
            output.append(keys['mission']['description'])

        output.append(keys['launch_service_provider']['name'])
        output.append(keys['status']['name'])
        output.append(keys['window_end'])
        output.append(keys['image'])

        output.append(keys['pad']['name'])
        output.append(keys['pad']['location']['map_image'])
        output.append(keys['pad']['location']['name'])

    return output


def get_id_of_parameter(parameter:str):
    """
    Returns the ids for the given parameter for the get_next_launch function.
    :param parameter:
    :return: Index of the parameter.
    """
    if parameter == "rocket":
        return 0
    elif parameter == "mission":
        return 1
    elif parameter == "type":
        return 2
    elif parameter == "description":
        return 3
    elif parameter == "agency":
        return 4
    elif parameter == "status":
        return 5
    elif parameter == "date":
        return 6
    elif parameter == "image":
        return 7
    elif parameter == "pad_name":
        return 8
    elif parameter == "pad_map":
        return 9
    elif parameter == "pad_location":
        return 10
    else:
        return None
