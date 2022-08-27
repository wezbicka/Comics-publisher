import requests


def download_image(image_url, download_path):
    response = requests.get(image_url)
    response.raise_for_status()
    with open(download_path, 'wb') as file:
        file.write(response.content)


def main():
    url = "https://xkcd.com/353"
    response = requests.get(f"{url}/info.0.json")
    response.raise_for_status()
    image_url = response.json()["img"]
    download_image(image_url, "картинка.png")


if __name__ == "__main__":
    main()