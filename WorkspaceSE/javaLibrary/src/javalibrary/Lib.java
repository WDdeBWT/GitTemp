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
		System.out.println("����������");
		Im[0].getIm(in.nextLine());
		System.out.println("����������");
		Im[1].getIm(in.nextLine());
		System.out.println("������۸�");
		Im[2].getIm(in.nextLine());
		System.out.println("�����������");
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
			System.out.println("��"+(i+1)+"����");
			System.out.println("����:"+a[i]);
			System.out.println("����:"+b[i]);
			System.out.println("�۸�:"+c[i]);
			System.out.println("����:"+d[i]);
			System.out.println("............");
		}
	}
	public void putBook(int n)
	{
		System.out.println("��"+(n+1)+"����");
		System.out.println("����:"+Im[0].putIm(n));
		System.out.println("����:"+Im[1].putIm(n));
		System.out.println("�۸�:"+Im[2].putIm(n));
		System.out.println("����:"+Im[3].putIm(n));
		System.out.println("............");
	}
	public int searchBook(String s)
	{
		int n;
		n=Im[0].search(s);
		if (n==-1)
		{
			System.out.println("δ�ҵ�����Ŀ��Ϣ");
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
		System.out.println("�밴Ҫ�������޸ĺ����Ϣ");
		System.out.println("����������");
		Im[0].change(n, in.nextLine());
		System.out.println("����������");
		Im[1].change(n, in.nextLine());
		System.out.println("������۸�");
		Im[2].change(n, in.nextLine());
		System.out.println("�����������");
		Im[3].change(n, in.nextLine());
		System.out.println("��Ϣ�ѱ���");
		System.out.println("............");
	}
	public void removeBook()
	{
		Scanner in = new Scanner(System.in);
		int n;
		System.out.println("��������Ҫɾ������Ŀ���");
		n=in.nextInt()-1;
		in.nextLine();
		if (n<Im[0].List.size())
		{
			Im[0].remove(n);
			Im[1].remove(n);
			Im[2].remove(n);
			Im[3].remove(n);
			System.out.println("ɾ���ɹ�");
			System.out.println("............");
		}
		else
		{
			System.out.println("ɾ��ʧ�ܣ������嵥��Χ");
			System.out.println("............");
		}
	}

	public static void main(String[] args)
	{
		// TODO Auto-generated method stub
		Scanner in = new Scanner(System.in);
		Lib Li = new Lib();
		System.out.println("��ӭʹ��ͼ�����ϵͳ");
		System.out.println("............");
		for (int flag=0; ; )
		{
			System.out.println("����ѡ��");
			System.out.println("(1)��������   (2)��ӡ�嵥   (3)����������");
			System.out.println("(4)������Ϣ   (5)ɾ����Ŀ   (6)�뿪������");
			System.out.print("�������Ӧ����:");
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
				System.out.print("������Ҫ���ҵ���Ŀ������:");
				s=in.nextLine();
				System.out.println("............");
				Li.searchBook(s);
			}
				break;
			case 4:
			{
				String s;
				System.out.print("������Ҫ���µ���Ŀ������:");
				s=in.nextLine();
				System.out.println("............");
				Li.changeBook(s);
			}
				break;
			case 5:
				Li.removeBook();
				break;
			case 6:
				System.out.println("��������գ���ӭ���´�ʹ�ñ�����");
				System.out.println("............");
				System.out.println("............");
				System.out.println("............");
				break;
			default:
				System.out.println("�����������������");
				break;
			}
			if (flag==6)
				break;
		}
		
	}

}










//