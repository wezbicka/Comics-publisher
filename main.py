import os
import random

import requests
from dotenv import load_dotenv


def get_upload_url(token, group_id, version):
    """Returns the server address for uploading
    a photo to a user's or community's wall."""
    url = "https://api.vk.com/method/photos.getWallUploadServer"
    params = {
        'access_token': token,
        "group_id": group_id,
        'v': version,
    }
    response = requests.post(url, params=params)
    response.raise_for_status()
    return response.json()['response']['upload_url']


def upload_photo_to_server(upload_url, file_name):
    with open(file_name, 'rb') as file:
        files = {
            'photo': file,
        }
        response = requests.post(upload_url, files=files)
    response.raise_for_status()
    return response.json()


def save_photo_to_album(token, group_id, args, version):
    url = "https://api.vk.com/method/photos.saveWallPhoto"
    params = {
        'access_token': token,
        "group_id": group_id,
        "photo": args['photo'],
        "server": args['server'],
        "hash": args['hash'],
        "v": version,
    }
    response = requests.post(url, params=params)
    response.raise_for_status()
    save_comic = response.json()['response'][0]
    return save_comic['id'], save_comic['owner_id']


def post_photo_to_wall(token, group_id, media_id, owner_id, text, version):
    url = "https://api.vk.com/method/wall.post"
    params = {
        'access_token': token,
        'owner_id': f'-{group_id}',
        'from_group': 1,
        'message': text,
        'attachments': f'photo{owner_id}_{media_id}',
        'v': version,
    }
    response = requests.post(url, params=params)
    response.raise_for_status()
    return response.json()


def get_last_comic_index():
    url = 'https://xkcd.com/info.0.json'
    response = requests.get(url)
    response.raise_for_status()
    return response.json()['num']


def get_comic(comic_number):
    url = f"https://xkcd.com/{comic_number}/info.0.json"
    response = requests.get(url)
    response.raise_for_status()
    image_url = response.json()["img"]
    comment = response.json()["alt"]
    return image_url, comment


def download_image(image_url, download_path):
    response = requests.get(image_url)
    response.raise_for_status()
    with open(download_path, 'wb') as file:
        file.write(response.content)


def main():
    load_dotenv()
    file_path = "file.png"
    version = 5.131
    vk_token = os.environ['VK_ACCESS_TOKEN']
    group_id = os.getenv('VK_GROUP_ID')
    comics_amount = get_last_comic_index()
    comic_number = random.randint(0, comics_amount)
    image_url, comment = get_comic(comic_number)
    download_image(image_url, file_path)
    upload_url = get_upload_url(vk_token, group_id, version)
    server_response = upload_photo_to_server(upload_url, file_path)
    media_id, owner_id = save_photo_to_album(
        vk_token,
        group_id,
        server_response,
        version,
    )
    post_photo_to_wall(
        vk_token,
        group_id,
        media_id,
        owner_id,
        comment,
        version,
    )
    if os.path.isfile(file_path):
        os.remove(file_path)


if __name__ == "__main__":
    main()
