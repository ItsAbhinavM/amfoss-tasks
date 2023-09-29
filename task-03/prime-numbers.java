import java.util.Scanner;

public class PrimeInRange {
    public static void main(String[] args) {
        int start = 2;
        int flag = 0;
        int end;
        
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the maximum number: ");
        end = scanner.nextInt();
        
        for (int number = start; number <= end; number++) {
            for (int divisor = 2; divisor < number; divisor++) {
                if (number % divisor == 0) {
                    flag = 1;
                    break;
                }
            }
            if (flag == 0) {
                System.out.print(number + " ");
            }
            flag = 0;
        }
    }
}
