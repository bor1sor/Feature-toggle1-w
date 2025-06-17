import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;

public class SuperTest {
    public static void main(String[] args) {
        // Не устанавливаем путь к драйверу явно
        ChromeOptions options = new ChromeOptions();
        options.addArguments("--remote-debugging-port=9222"); // Дополнительно (необязательно)

        try (WebDriver driver = new ChromeDriver(options)) { // Авто-закрытие драйвера
            driver.get("https://budu.ru");

            // Просто проверяем, загрузилась ли страница
            System.out.println("Страница загружена! Текущий URL: " + driver.getCurrentUrl());
        }
    }
}