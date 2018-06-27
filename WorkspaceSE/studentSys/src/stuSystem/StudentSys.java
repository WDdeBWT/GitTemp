package stuSystem;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.util.Scanner;

public class StudentSys
{
	Imf[] Im = new Imf[3];
	
	StudentSys()
	{
		for (int i=0; i<3; i++)
		{
			Im[i] = new Imf();
		}
	}
	public void putStu()
	{
		Scanner in = new Scanner(System.in);
		String s;
		System.out.println("请输入学生姓名");
		s=in.nextLine();
		System.out.println("请输入学生班级");
		Im[0].putIm(s, "Class :"+in.nextLine());
		System.out.println("请输入学生学号");
		Im[1].putIm(s, "ID NO.:"+in.nextLine());
		System.out.println("请输入学生成绩");
		Im[2].putIm(s, "Grade :"+in.nextLine());
		System.out.println("信息已保存");
		System.out.println("------------");
	}
	public int getStu()
	{
		Scanner in = new Scanner(System.in);
		String s;
		System.out.println("请输入查找的学生的姓名");
		System.out.print("Name  :");
		s=in.nextLine();
		if (!Im[0].hMap.containsKey(s))
		{
			System.out.println("未找到该同学信息");
			System.out.println("------------");
			return -1;
		}
		for (int i=0; i<3;i++)
		{
			System.out.println(Im[i].getIm(s));
		}
		System.out.println("------------");
		return 0;
	}
	public void getList()
	{
		for (String s : Im[0].hMap.keySet())
		{
			System.out.println("Name  :"+s);
			for (int i=0;i<3;i++)
			{
				System.out.println(Im[i].getIm(s));
			}
			System.out.println("------------");
		}
		System.out.println("------------");
	}
	public int changeStu()
	{
		Scanner in = new Scanner(System.in);
		String s;
		System.out.println("请输入要更新的学生的姓名");
		s=in.nextLine();
		if (!Im[0].hMap.containsKey(s))
		{
			System.out.println("未找到该同学信息");
			System.out.println("------------");
			return -1;
		}
		System.out.println("请输入学生班级");
		Im[0].putIm(s, "Class :"+in.nextLine());
		System.out.println("请输入学生学号");
		Im[1].putIm(s, "ID NO.:"+in.nextLine());
		System.out.println("请输入学生成绩");
		Im[2].putIm(s, "Grade :"+in.nextLine());
		System.out.println("信息已更新");
		System.out.println("------------");
		return 0;
	}
	public int removeStu()
	{
		Scanner in = new Scanner(System.in);
		String s;
		System.out.println("请输入要删除的学生的姓名");
		s=in.nextLine();
		if (!Im[0].hMap.containsKey(s))
		{
			System.out.println("未找到该同学信息");
			System.out.println("------------");
			return -1;
		}
		for (int i=0; i<3; i++)
		{
			Im[i].hMap.remove(s);
		}
		System.out.println("删除成功");
		System.out.println("------------");
		return 0;
	}
	public void readTxt()
	{
		try
		{
			BufferedReader in = new BufferedReader(
					new InputStreamReader(
							new FileInputStream("Imformation.txt")));
			String line="";
			String name="";
			while ((line=in.readLine())!=null)
			{
				for (int i=0; i<4; i++)
				{
					switch (i)
					{
					case 0:
						name=line;
						break;
					case 1:
						line=in.readLine();
						Im[0].putIm(name, line);
						break;
					case 2:
						line=in.readLine();
						Im[1].putIm(name, line);
						break;
					case 3:
						line=in.readLine();
						Im[2].putIm(name, line);
						break;
					}
				}
			}
		} catch (FileNotFoundException e)
		{
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
	public void saveTxt()
	{
		try
		{
			PrintWriter out = new PrintWriter(
					new BufferedWriter(
							new OutputStreamWriter(
									new FileOutputStream("Imformation.txt"))));
			for (String s : Im[0].hMap.keySet())
			{
				out.println(s);
				for (int i=0;i<3;i++)
				{
					out.println(Im[i].getIm(s));
				}
			}
			out.close();
		} catch (FileNotFoundException e)
		{
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

	public static void main(String[] args)
	{
		// TODO Auto-generated method stub
		Scanner in = new Scanner(System.in);
		StudentSys Stu = new StudentSys();
		System.out.println("欢迎使用学籍管理系统");
		System.out.println("------------");
		Stu.readTxt();
		for (int flag=0; ; )
		{
			System.out.println("功能选择");
			System.out.println("(1)输入信息   (2)打印清单   (3)按姓名查找");
			System.out.println("(4)更新信息   (5)删除信息   (6)离开本程序");
			System.out.print("请输入对应数字:");
			flag=in.nextInt();
			in.nextLine();
			System.out.println("------------");
			switch (flag)
			{
			case 1:
				Stu.putStu();
				break;
			case 2:
				Stu.getList();
				break;
			case 3:
				Stu.getStu();
				break;
			case 4:
				Stu.changeStu();
				break;
			case 5:
				Stu.removeStu();
				break;
			case 6:
				System.out.println("数据已清空，欢迎您下次使用本程序");
				System.out.println("------------");
				System.out.println("------------");
				System.out.println("------------");
				break;
			default:
				System.out.println("输入错误，请重新输入");
				break;
			}
			if (flag==6)
			{
				Stu.saveTxt();
				break;
			}
		}
	}

}









