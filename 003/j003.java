import java.util.Dictionary;
import java.util.Hashtable;
import java.util.Enumeration;
import java.util.Scanner;

public class j003 {
    public static void main(String[] args) {
        System.out.print("Enter a number: ");

        Scanner sc = new Scanner(System.in);
        int maxkey = sc.nextInt();
        sc.close();

        Dictionary<Integer, Integer> dictionary = genDictionary(maxkey);
        printDictionary(dictionary);
    }

    public static Dictionary<Integer, Integer> genDictionary(int maxkey) {
        Dictionary<Integer, Integer> dictionary = new Hashtable<Integer, Integer>();

        for (int k = 1; k <= maxkey; k++) {
            dictionary.put(k, k * k);
        }

        return dictionary;
    }
    
    public static void printDictionary(Dictionary<Integer, Integer> dictionary) {
        int index = dictionary.size();
        int[] values = new int[index];

        Enumeration<Integer> eKeys = dictionary.keys();

        int key;
        while (eKeys.hasMoreElements()) {
            key = eKeys.nextElement();
            values[--index] = dictionary.get(key);
        }

        StringBuilder sb = new StringBuilder();
        sb.append("{");

        for (int i = 0; i < values.length; i++) {
            sb.append((i + 1) + ": " + values[i] + (i != values.length - 1 ? ", " : ""));
        }

        sb.append("}");
        System.out.println(sb.toString());
    }
}