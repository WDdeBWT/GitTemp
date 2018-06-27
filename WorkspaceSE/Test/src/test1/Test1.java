package test1;

import java.util.Scanner;

public class Test1
{
	
	public static void main(String[] args)
	{
		// TODO Auto-generated method stub
		Test101 t1 = new Test101();
		Test101 t2 = new Test101();
		Test101 t3 = new Test101();
		t1.get(2);
		System.out.println(t1.put());
		t2 = t1;
		t3 = t2;
		t3.get(3);
		System.out.println(t3.put());
		System.out.println(t2.put());
		System.out.println(t1.put());
	}

}
