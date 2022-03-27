import requests


def get_iss_location_as_coordinates():
    """
    Returns the current location of the ISS as coordinates
    :return: List of coordinates (lat, long)
    """
    url = "http://api.open-notify.org/iss-now.json"
    response = requests.get(url)
    response_json = response.json()
    iss_location = response_json["iss_position"]
    output = [iss_location["latitude"], iss_location["longitude"]]

    return output


def get_current_astronauts_on_iss():
    """
    Returns a list of the current astronauts on the ISS
    :return: List of astronauts
    """
    output = []

    url = "http://api.open-notify.org/astros.json"
    response = requests.get(url)
    response_json = response.json()
    people = response_json["people"]

    for person in people:
        output.append(person["name"])

    return output


def get_amount_of_people_on_iss():
    """
    Returns the amount of people on the ISS
    :return: Amount of people on the ISS
    """
    url = "http://api.open-notify.org/astros.json"
    response = requests.get(url)
    response_json = response.json()
    return response_json["number"]

