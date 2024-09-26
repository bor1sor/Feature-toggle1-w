import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# URL главной страницы
url = "https://budu.ru/catalog"


# Проверка доступности страницы с помощью requests
def check_page_availability(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Страница доступна: {url}")
            return True
        else:
            print(f"Страница недоступна: {url}, статус: {response.status_code}")
            return False
    except requests.RequestException as e:
        print(f"Ошибка при доступе к {url}: {e}")
        return False


# Функция для автоматизации действий на веб-странице с помощью Selenium
def automate_web_interaction(url):
    # Настройка драйвера (например, Chrome)
    driver = (
        webdriver.Chrome()
    )  # Убедитесь, что ChromeDriver установлен и доступен в PATH
    driver.get(url)

    # Ждем, чтобы страница загрузилась
    time.sleep(2)

    # Делаем скриншот главной страницы
    driver.save_screenshot("main_page_screenshot.png")
    print("Скриншот главной страницы сохранен как 'main_page_screenshot.png'.")

    # Закрываем драйвер
    driver.quit()


if __name__ == "__main__":
    if check_page_availability(url):
        automate_web_interaction(url)
