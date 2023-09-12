import requests


def get_random_quote():
    url = "https://api.quotable.io/random"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data["content"]
    else:
        return "Failed to fetch a quote"
