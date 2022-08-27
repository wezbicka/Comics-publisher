import os

import requests
from dotenv import load_dotenv


def download_image(image_url, download_path):
    response = requests.get(image_url)
    response.raise_for_status()
    with open(download_path, 'wb') as file:
        file.write(response.content)


def main():
    load_dotenv()
    client_id = os.environ['CLIENT_ID']
    url = "https://xkcd.com/353"
    response = requests.get(f"{url}/info.0.json")
    response.raise_for_status()
    image_url = response.json()["img"]
    comment = response.json()["alt"]
    print(comment)
    download_image(image_url, "картинка.png")


if __name__ == "__main__":
    main()