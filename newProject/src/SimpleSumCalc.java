import java.util.Scanner;

public class SimpleSumCalc {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Введите целое положительное число: ");
        int n = scanner.nextInt();

        int sum = 0;

        for (int i = 1; i <= n; i++) {
            sum += i;
        }

        System.out.println("Сумма чисел от 1 до " + n + ": " + sum);
    }
}