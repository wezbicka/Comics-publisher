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


def get_photo_url(token, group_id):
    """Returns the server address for uploading a photo to a user's or community's wall."""
    url = "https://api.vk.com/method/photos.getWallUploadServer"
    params = {
        'access_token': token,
        "group_id": group_id,
        'v': 5.131,
    }
    response = requests.post(url, params=params)
    response.raise_for_status()
    print(response.content)


def download_image(image_url, download_path):
    response = requests.get(image_url)
    response.raise_for_status()
    with open(download_path, 'wb') as file:
        file.write(response.content)


def main():
    load_dotenv()
    client_id = os.environ['CLIENT_ID']
    vk_token = os.environ['ACCESS_TOKEN']
    group_id = 215590113
    # url = "https://xkcd.com/353"
    # response = requests.get(f"{url}/info.0.json")
    # response.raise_for_status()
    # image_url = response.json()["img"]
    # comment = response.json()["alt"]
    # print(comment)
    # download_image(image_url, "картинка.png")
    get_photo_url(vk_token, group_id)
    get_groups(vk_token)


if __name__ == "__main__":
    main()
