package main;

import java.util.Scanner;

public class Library
{
	static int n=0;
	Book bk = new Book();
	public void getIm()
	{
		//Get information(Name,Auther,Price,Publish
		Scanner in = new Scanner(System.in);
		String Na;
		String Au;
		int Pr;
		String Pu;
		System.out.println("请输入书名");
		Na=in.nextLine();
		System.out.println("请输入作者");
		Au=in.nextLine();
		System.out.println("请输入价格");
		Pr=in.nextInt();
		in.nextLine();
		System.out.println("请输入出版社");
		Pu=in.nextLine();
		bk.mainGet(Na, Au, Pr, Pu);
	}
	public int putIm()
	{
		int m;
		m = bk.checkRemove();
		if (m==1)
		{
			bk.mainPut();
		}
		return m;
	}
	
	public static void main(String[] args)
	{
		// TODO Auto-generated method stub
		Scanner in = new Scanner(System.in);
		Library[] Li = new Library[10];
		for (int i=0; i<10; i++)
		{
			Li[i] = new Library();
		}
		int flag1=0;
		do
		{
			flag1=0;
			System.out.println("请输入需要实现的功能");
			System.out.println("输入新书请按1，打印清单请按2，按书名查找请按3");
			System.out.println("更新信息请按4，删除书目请按5，离开本程序请按6");
			flag1=in.nextInt();
			in.nextLine();
			switch (flag1)
			{
			case 1:
				Li[n].getIm();
				n++;
				break;
			case 2:
				for (int i=0; i<n; i++)
				{
					System.out.println("----------------");
					Li[i].putIm();
					System.out.println("----------------");
				}
				break;
			case 3:
				{
					int j=0;
					String s = "";
					System.out.println("请输入要查找的书名");
					s = in.nextLine();
					for (int i=0; i<n; i++)
					{
						if (Li[i].bk.search(s) == 1)
						{
							j=Li[i].putIm();
						}
					}
					if (j==0)
					{
						System.out.println("未查找到此书信息");
					}
				}
				break;
			case 4:
				{
					int j=0;
					String s = "";
					System.out.println("请输入需要更新的书目名称");
					s = in.nextLine();
					for (int i=0; i<n; i++)
					{
						if (Li[i].bk.search(s) == 1&&Li[i].bk.checkRemove()==1)
						{
							j=1;
							System.out.println("请输入更新后的信息");
							Li[i].getIm();
						}
					}
					if (j==0)
					{
						System.out.println("未查找到此书信息");
					}
				}
				break;
			case 5:
				{
					int j=0;
					String s = "";
					System.out.println("请输入需要删除的书目名称");
					s = in.nextLine();
					for (int i=0; i<n; i++)
					{
						if (Li[i].bk.search(s) == 1&&Li[i].bk.checkRemove()==1)
						{
							j=1;
							Li[i].bk.remove();
						}
					}
					if (j==0)
					{
						System.out.println("未查找到此书信息");
					}
				}
				break;
			case 6:
				break;
			default:
				System.out.println("输入错误，请重新输入");
			}
		} while(flag1!=6);
	}

}




















///