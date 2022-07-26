import java.util.Scanner;

public class j002 {
    public static void main(String[] args) {
        System.out.print("Enter a number: ");
        Scanner scanner = new Scanner(System.in);
        
        int number = scanner.nextInt();

        scanner.close();

        System.out.println(number + "! = " + factorial1(number));
        System.out.println(number + "! = " + factorial2(number));
    }

    public static int factorial1(int number) {
        int result = 1;

        for (int i = 1; i <= number; i++) {
            result *= i;
        }

        return result;
    }

    public static int factorial2(int number) {
        if (number <= 1) {
            return 1;
        }

        return factorial2(number - 1) * number;
    }
}