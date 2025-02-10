from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    # Открываем сайт
    driver.get("https://www.saucedemo.com/v1/")

    # Ожидаем, пока элементы загрузятся
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "user-name"))
    )

    # Находим поля для ввода логина и пароля
    username_field = driver.find_element(By.ID, "user-name")
    password_field = driver.find_element(By.ID, "password")

    # Вводим логин и пароль
    username_field.send_keys("standard_user")
    password_field.send_keys("secret_sauce")

    # Находим кнопку для входа и нажимаем на нее
    login_button = driver.find_element(By.XPATH, "//input[@value='LOGIN']")
    login_button.click()

    # Ожидаем, пока загрузится следующая страница
    WebDriverWait(driver, 10).until(EC.title_contains("Swag Labs"))

    # Проверяем, что авторизация прошла успешно
    print("Авторизация успешна! Заголовок страницы:", driver.title)

finally:
    # Закрываем браузер
    driver.quit()
