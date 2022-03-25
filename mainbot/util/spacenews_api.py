import requests


def get_latest_news():
    output = []

    request = requests.get("https://api.spaceflightnewsapi.net/v3/articles/?_limit=1")
    news_data = request.json()

    for keys in news_data:
        output.append(keys['title'])
        output.append(keys['url'])
        output.append(keys['imageUrl'])
        output.append(keys['summary'])
        output.append(keys['publishedAt'])

    return output


def get_id_of_parameter(parameter: str):
    if parameter == "title":
        return 0
    elif parameter == "url":
        return 1
    elif parameter == "image":
        return 2
    elif parameter == "summary":
        return 3
    elif parameter == "publish_date":
        return 4
    else:
        return None
