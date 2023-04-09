import os

import requests
from dotenv import load_dotenv


def get_groups(token, version):
    url = "https://api.vk.com/method/groups.get"
    params = {
        'access_token': token,
        'filter': "admin",
        'v': version,
    }
    response = requests.post(url, params=params)
    response.raise_for_status()
    return response.json()['response']


def get_upload_url(token, group_id, version):
    """Returns the server address for uploading a photo to a user's or community's wall."""
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
    server_answer = response.json()
    return (
        server_answer['photo'],
        server_answer['server'],
        server_answer['hash'],
    )


def save_photo_to_album(token, group_id, photo, server, hash, version):
    url = "https://api.vk.com/method/photos.saveWallPhoto"
    params = {
        'access_token': token,
        "group_id": group_id,
        "photo": photo,
        "server": server,
        "hash": hash,
        "v": version,
    }
    response = requests.post(url, params=params)
    response.raise_for_status()
    return response.json()


def download_image(image_url, download_path):
    response = requests.get(image_url)
    response.raise_for_status()
    with open(download_path, 'wb') as file:
        file.write(response.content)


def main():
    load_dotenv()
    version = 5.131
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
    print(get_groups(vk_token, version))
    upload_url = get_upload_url(vk_token, group_id, version)
    photo, server, hash = upload_photo_to_server(upload_url, "картинка.png")
    print(save_photo_to_album(vk_token, group_id, photo, server, hash, version))


if __name__ == "__main__":
    main()
