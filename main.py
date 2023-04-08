import os

import requests
from dotenv import load_dotenv


def get_groups(token):
    url = "https://api.vk.com/method/groups.get"
    params = {
        'access_token': token,
        'filter': "admin",
        'v': 5.131,
    }
    response = requests.post(url, params=params)
    response.raise_for_status()
    print(response.json())


def download_image(image_url, download_path):
    response = requests.get(image_url)
    response.raise_for_status()
    with open(download_path, 'wb') as file:
        file.write(response.content)


def main():
    load_dotenv()
    client_id = os.environ['CLIENT_ID']
    vk_token = os.environ['ACCESS_TOKEN']
    url = "https://xkcd.com/353"
    response = requests.get(f"{url}/info.0.json")
    response.raise_for_status()
    image_url = response.json()["img"]
    comment = response.json()["alt"]
    print(comment)
    download_image(image_url, "картинка.png")
    get_groups(vk_token)


if __name__ == "__main__":
    main()
