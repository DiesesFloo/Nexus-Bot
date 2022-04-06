import requests


def get_id_of_main_profile(name: str):
    if user_exists(name):
        request = requests.get(f"https://sky.shiiyu.moe/api/v2/profile/{name}")
        data = request.json()
        user_id = ""

        for x in data['profiles']:
            if data['profiles'][x]['current']:
                user_id = data['profiles'][x]['profile_id']

        return user_id
    else:
        return "N/A"


def get_purse_of_main_profile(name: str):
    if user_exists(name):
        user_id = get_id_of_main_profile(name)

        request = requests.get(f"https://sky.shiiyu.moe/api/v2/coins/{name}")
        data = request.json()

        purse = data['profiles'][user_id]['purse']
        purse = round(purse, 2)

        return purse
    else:
        return "N/A"


def get_head_of_user(name: str):
    if user_exists(name):
        url = f"https://cravatar.eu/avatar/{name}/600.png"
        return url
    else:
        return "https://cravatar.eu/avatar/BaldAndDepressed/600.png"


def user_exists(name: str):
    profile_request = requests.get(f"https://sky.shiiyu.moe/api/v2/profile/{name}")
    profile_return_code = profile_request.status_code

    coins_request = requests.get(f"https://sky.shiiyu.moe/api/v2/coins/{name}")
    coins_return_code = coins_request.status_code

    if profile_return_code == 200:
        print("Profile exists")
        if coins_return_code == 200:
            print("Coins and Profile found")
            return True
        else:
            return False
    else:
        return False


def user_has_bank_activated(name: str, profile: str):
    coins_request = requests.get(f"https://sky.shiiyu.moe/api/v2/coins/{name}/{profile}")
    coins_return_code = coins_request.status_code
    if coins_return_code == 200:
        coins_data = coins_request.json()
        if "bank" in coins_data:
            return True
        else:
            return False
    else:
        return False



