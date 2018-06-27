package javalibrary;

import java.util.Scanner;

public class Lib
{
	static String[] a = new String[20];
	static String[] b = new String[20];
	static String[] c = new String[20];
	static String[] d = new String[20];
	Imf[] Im = new Imf[4];

	Lib()
	{
		for (int i=0; i<4; i++)
		{
			Im[i] = new Imf();
		}
	}
	public void getBook()
	{
		Scanner in = new Scanner(System.in);
		System.out.println("请输入书名");
		Im[0].getIm(in.nextLine());
		System.out.println("请输入作者");
		Im[1].getIm(in.nextLine());
		System.out.println("请输入价格");
		Im[2].getIm(in.nextLine());
		System.out.println("请输入出版社");
		Im[3].getIm(in.nextLine());
		System.out.println("............");
	}
	public void putBookList()
	{
		a=Im[0].getList();
		b=Im[1].getList();
		c=Im[2].getList();
		d=Im[3].getList();
		for (int i=0; i<Im[0].List.size(); i++)
		{
			System.out.println("第"+(i+1)+"本书");
			System.out.println("书名:"+a[i]);
			System.out.println("作者:"+b[i]);
			System.out.println("价格:"+c[i]);
			System.out.println("出版:"+d[i]);
			System.out.println("............");
		}
	}
	public void putBook(int n)
	{
		System.out.println("第"+(n+1)+"本书");
		System.out.println("书名:"+Im[0].putIm(n));
		System.out.println("作者:"+Im[1].putIm(n));
		System.out.println("价格:"+Im[2].putIm(n));
		System.out.println("出版:"+Im[3].putIm(n));
		System.out.println("............");
	}
	public int searchBook(String s)
	{
		int n;
		n=Im[0].search(s);
		if (n==-1)
		{
			System.out.println("未找到该书目信息");
			System.out.println("............");
		}
		else
		{
			putBook(n);
		}
		return n;
	}
	public void changeBook(String s)
	{
		Scanner in = new Scanner(System.in);
		int n;
		n=searchBook(s);
		System.out.println("请按要求输入修改后的信息");
		System.out.println("请输入书名");
		Im[0].change(n, in.nextLine());
		System.out.println("请输入作者");
		Im[1].change(n, in.nextLine());
		System.out.println("请输入价格");
		Im[2].change(n, in.nextLine());
		System.out.println("请输入出版社");
		Im[3].change(n, in.nextLine());
		System.out.println("信息已保存");
		System.out.println("............");
	}
	public void removeBook()
	{
		Scanner in = new Scanner(System.in);
		int n;
		System.out.println("请输入需要删除的书目序号");
		n=in.nextInt()-1;
		in.nextLine();
		if (n<Im[0].List.size())
		{
			Im[0].remove(n);
			Im[1].remove(n);
			Im[2].remove(n);
			Im[3].remove(n);
			System.out.println("删除成功");
			System.out.println("............");
		}
		else
		{
			System.out.println("删除失败，超出清单范围");
			System.out.println("............");
		}
	}

	public static void main(String[] args)
	{
		// TODO Auto-generated method stub
		Scanner in = new Scanner(System.in);
		Lib Li = new Lib();
		System.out.println("欢迎使用图书管理系统");
		System.out.println("............");
		for (int flag=0; ; )
		{
			System.out.println("功能选择");
			System.out.println("(1)输入新书   (2)打印清单   (3)按书名查找");
			System.out.println("(4)更新信息   (5)删除书目   (6)离开本程序");
			System.out.print("请输入对应数字:");
			flag=in.nextInt();
			in.nextLine();
			System.out.println("............");
			switch (flag)
			{
			case 1:
				Li.getBook();
				break;
			case 2:
				Li.putBookList();
				break;
			case 3:
			{
				String s;
				System.out.print("请输入要查找的书目的书名:");
				s=in.nextLine();
				System.out.println("............");
				Li.searchBook(s);
			}
				break;
			case 4:
			{
				String s;
				System.out.print("请输入要更新的书目的书名:");
				s=in.nextLine();
				System.out.println("............");
				Li.changeBook(s);
			}
				break;
			case 5:
				Li.removeBook();
				break;
			case 6:
				System.out.println("数据已清空，欢迎您下次使用本程序");
				System.out.println("............");
				System.out.println("............");
				System.out.println("............");
				break;
			default:
				System.out.println("输入错误，请重新输入");
				break;
			}
			if (flag==6)
				break;
		}
		
	}

}










//