import requests

request = requests.get("https://ll.thespacedevs.com/2.2.0/launch/upcoming/?limit=5")
nasa_data = request.json()['results']
rockets = []
missions = []
types = []
agencies = []
statuses = []
starts = []


for keys in nasa_data:
    rockets.append(keys['rocket']['configuration']['full_name'])
    missions.append(keys['mission']['name'])
    types.append(keys['mission']['type'])
    agencies.append(keys['launch_service_provider']['name'])
    statuses.append(keys['status']['name'])
    starts.append(keys['window_end'])

print(f"Start: {starts[0]}")
print(f"Mission: {missions[0]}")
print(f"Agency: {agencies[0]}")
print(f"Status: {statuses[0]}")
print(f"Type: {types[0]}")
print(f"Rocket: {rockets[0]}")

print("    ")

print(f"Start: {starts[1]}")
print(f"Mission: {missions[1]}")
print(f"Agency: {agencies[1]}")
print(f"Status: {statuses[1]}")
print(f"Type: {types[1]}")
print(f"Rocket: {rockets[1]}")