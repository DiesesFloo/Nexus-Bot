import requests


def get_iss_location_as_coordinates():
    url = "http://api.open-notify.org/iss-now.json"
    response = requests.get(url)
    response_json = response.json()
    iss_location = response_json["iss_position"]
    output = [iss_location["latitude"], iss_location["longitude"]]

    return output


def get_current_astronauts_on_iss():
    output = []

    url = "http://api.open-notify.org/astros.json"
    response = requests.get(url)
    response_json = response.json()
    people = response_json["people"]

    for person in people:
        output.append(person["name"])

    return output


def get_amount_of_people_on_iss():
    url = "http://api.open-notify.org/astros.json"
    response = requests.get(url)
    response_json = response.json()
    return response_json["number"]


def get_information_about_astronaut(astronaut_name):
    url = "http://api.open-notify.org/astros.json"
    response = requests.get(url)
    response_json = response.json()
    people = response_json["people"]

    for person in people:
        if person["name"] == astronaut_name:
            return person

    return None
