package hello;
import java.util.*;

public class ExceptionDemo 
{
    public static void main(String[] args)
    {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a interger:");

        try
        {
            int number = scanner.nextInt();
            System.out.println("The number entered is:"+number);
        }
        catch (Exception e)
        {
            e.printStackTrace();
            System.out.println("��Ϊû�а�������ʽ���룬���򱨴���ֹ");
        }
    }
}