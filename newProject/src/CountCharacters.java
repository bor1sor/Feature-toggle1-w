import java.util.Scanner;

public class CountCharacters {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Введите вашу строку: ");
        String input = scanner.nextLine();

        System.out.println("Количество символов в строке: " + input.length());

        scanner.close();

    }

}
