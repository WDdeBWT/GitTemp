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
		System.out.println("����������");
		Na=in.nextLine();
		System.out.println("����������");
		Au=in.nextLine();
		System.out.println("������۸�");
		Pr=in.nextInt();
		in.nextLine();
		System.out.println("�����������");
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
			System.out.println("��������Ҫʵ�ֵĹ���");
			System.out.println("���������밴1����ӡ�嵥�밴2�������������밴3");
			System.out.println("������Ϣ�밴4��ɾ����Ŀ�밴5���뿪�������밴6");
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
					System.out.println("������Ҫ���ҵ�����");
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
						System.out.println("δ���ҵ�������Ϣ");
					}
				}
				break;
			case 4:
				{
					int j=0;
					String s = "";
					System.out.println("��������Ҫ���µ���Ŀ����");
					s = in.nextLine();
					for (int i=0; i<n; i++)
					{
						if (Li[i].bk.search(s) == 1&&Li[i].bk.checkRemove()==1)
						{
							j=1;
							System.out.println("��������º����Ϣ");
							Li[i].getIm();
						}
					}
					if (j==0)
					{
						System.out.println("δ���ҵ�������Ϣ");
					}
				}
				break;
			case 5:
				{
					int j=0;
					String s = "";
					System.out.println("��������Ҫɾ������Ŀ����");
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
						System.out.println("δ���ҵ�������Ϣ");
					}
				}
				break;
			case 6:
				break;
			default:
				System.out.println("�����������������");
			}
		} while(flag1!=6);
	}

}




















///