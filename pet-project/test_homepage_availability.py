import requests


def test_homepage_availability():
    url = "https://shop.budu.ru/"
    response = requests.get(url)
    assert (
        response.status_code == 200
    ), f"Страница недоступна, статус: {response.status_code}"
    print("Главная страница доступна.")


if __name__ == "__main__":
    test_homepage_availability()
