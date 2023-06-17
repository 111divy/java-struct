
import java.util.Scanner;
public class Problem1week1{
    public static void main(String[] args){
        Scanner in = new Scanner(System.in);
        int a = in.nextInt();
        int b = in.nextInt();
        String ans = (a%b == 0 || b%a == 0)? "Multiples" : "No Multiples";
        System.out.println(ans);
    }
}