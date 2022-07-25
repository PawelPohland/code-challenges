import java.util.ArrayList;

public class j001 {
    public static void main(String[] args) {
        j001 me = new j001();
        String numbers = me.getNumbers(2000, 3200);

        System.out.println(numbers);
    }

    public String getNumbers(int startNum, int endNum) {
        ArrayList<Integer> numbers = new ArrayList<>();

        for (int number = startNum; number <= endNum; number++) {
            if (number % 7 == 0 && number % 5 != 0) {
                numbers.add(number);
            }
        }

        StringBuilder sb = new StringBuilder();
        for (Integer number: numbers) {
            if (sb.length() != 0) {
                sb.append(", ");
            }
            sb.append(number.toString());
        }

        return sb.toString();
    }
}
