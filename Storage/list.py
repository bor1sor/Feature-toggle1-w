import requests


def test_website_availability():
    url = "https://shop.budu.ru/"
    response = requests.get(url)
    assert (
        response.status_code == 404
    ), f"Failed to access {url}, Status code: {response.status_code}"


if __name__ == "__main__":
    test_website_availability()
