import requests
from selenium import webdriver
from selenium.common.exceptions import WebDriverException


def test_website_availability():
    url = "https://shop.budu.ru/444"

    # Проверка доступности сайта с использованием библиотеки Requests
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("Тест с Requests: Успех! Сайт доступен.")
        else:
            print(f"Тест с Requests: Неуспех! Код статуса: {response.status_code}")
            return
    except requests.RequestException as e:
        print(f"Тест с Requests: Неуспех! Ошибка: {e}")
        return

    # Проверка доступности сайта с использованием библиотеки Selenium
    try:
        driver = webdriver.Chrome()  # Убедитесь, что у вас установлен ChromeDriver
        driver.get(url)
        if "404" not in driver.title:
            print("Тест с Selenium: Успех! Сайт доступен.")
        else:
            print("Тест с Selenium: Неуспех! Страница не найдена (404).")
    except WebDriverException as e:
        print(f"Тест с Selenium: Неуспех! Ошибка: {e}")
    finally:
        driver.quit()


if __name__ == "__main__":
    test_website_availability()
