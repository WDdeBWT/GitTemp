package main;

import java.util.Scanner;

public class Book
{
	private String name="";
	private String auther="";
	private double price=0;
	private String pub="";
	private int flag=1;
	//Get//
	public void getName(String s)
	{
		name=s;
	}
	public void getAuther(String s)
	{
		auther=s;
	}
	public void getPrice(int n)
	{
		price=n;
	}
	public void getPub(String s)
	{
		pub=s;
	}
	//Put//
	public String putName()
	{
		return name;
	}
	public String putAuther()
	{
		return auther;
	}
	public double putPrice()
	{
		return price;
	}
	public String putPub()
	{
		return pub;
	}
	//mainGet//
	public void mainGet(String a, String b, int c, String d)
	{
		this.getName(a);
		this.getAuther(b);
		this.getPrice(c);
		this.getPub(d);
		
	}
	//mainPut//
	public void mainPut()
	{
		System.out.println("����:"+this.putName());
		System.out.println("����:"+this.putAuther());
		System.out.println("�۸�:"+this.putPrice());
		System.out.println("����:"+this.putPub());
	}
	//remove//
	public void remove()
	{
		flag=0;
		System.out.println("ɾ���ɹ�");
	}
	//checkRemove//
	public int checkRemove()
	{
		return flag;
	}
	//search//
	public int search(String s)
	{
		if (s.equals(name))
			return 1;
		else
			return 0;
	}

	public static void main(String[] args)
	{
		// TODO Auto-generated method stub
		Book a = new Book();
		Scanner in = new Scanner(System.in);
		a.getName(in.nextLine());
		a.getAuther(in.nextLine());
		a.getPrice(in.nextInt());
		in.nextLine();
		a.getPub(in.nextLine());
		a.mainPut();
	}

}









