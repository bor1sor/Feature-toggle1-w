package ru.budu.autotests;

import org.junit.jupiter.api.AfterAll;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;

@DisplayName("Простое автоматизированное тестирование")
class SimpleTest {

    private static WebDriver driver;

    @BeforeAll
    static void setupClass() {
        // Укажите путь к вашему chromedriver.exe здесь!
        System.setProperty("webdriver.chrome.driver", "/path/to/chromedriver");
        driver = new ChromeDriver();
    }

    @Test
    @DisplayName("Проверка наличия заголовка на главной странице Budu.ru")
    void checkMainPageTitle() {
        // Открываем главную страницу
        driver.get("https://budu.ru");

        // Проверяем наличие элемента с определенным текстом
        String titleElementText = driver.findElement(By.tagName("h1")).getText();
        if (!titleElementText.contains("Буду")) {
            throw new AssertionError("Заголовок отсутствует или неверный.");
        }
    }

    @AfterAll
    static void teardownClass() {
        if (driver != null) {
            driver.quit();
        }
    }
}