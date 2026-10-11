import requests


def test_homepage_unavailable():
    url = "https://budu.ru/catalog/0000"
    response = requests.get(url)
    assert (
        response.status_code == 200
    ), f"Страница недоступна, статус: {response.status_code}"
    print("Page not found.")


if __name__ == "__main__":
    test_homepage_unavailable()
