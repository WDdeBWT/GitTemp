package hello;

import java.util.Scanner;

public class Hello
{
	public static void main(String[] args)
	{
		Scanner in = new Scanner(System.in);
		int[][] aaa = new int[3][3];
		//��������
		for (int i=0;i<9;i++)
		{
			int FLAG;
			int x,y;
			do
			{
				FLAG=1;
				System.out.println("��������Ҫ���ӵ��к��У��ÿո�ֿ�");
				x=in.nextInt()-1;
				y=in.nextInt()-1;
				if (x>=0&&x<=2&&y>=0&&y<=2&&aaa[x][y]==0)
				{
					FLAG=0;
					break;
				}
				System.out.println("�����������������");
			}while (FLAG==1);
			if (i%2==0)
			{
				aaa[x][y]=1;
			}
			else
			{
				aaa[x][y]=2;
			}
			//�������
			for (int r=0;r<3;r++)
			{
				for (int j=0;j<3;j++)
				{
					System.out.print(aaa[r][j]+" ");				
				}
				System.out.print("\n");
			}
			int k=0;
			Judge:
			for (int r=0;r<1;r++)
			{
				int FLAG1=0,FLAG2=0;
				//�ж���
				for (int m=0;m<3;m++)
				{
					k=1;
					FLAG1=aaa[m][0];
					if (FLAG1==0)
					{
						k=0;
						break;
					}
					for (int n=0;n<3;n++)
					{
						FLAG2=aaa[m][n];
						if (FLAG1==FLAG2)
						{
							FLAG1=FLAG2;
							continue;
						}
						k=0;
						break;
					}
					if (k==1)
					{
						break Judge;
					}
				}
				//�ж���
				for (int n=0;n<3;n++)
				{
					k=1;
					FLAG1=aaa[0][n];
					if (FLAG1==0)
					{
						k=0;
						break;
					}
					for (int m=0;m<3;m++)
					{
						FLAG2=aaa[m][n];
						if (FLAG1==FLAG2)
						{
							FLAG1=FLAG2;
							continue;
						}
						k=0;
						break;
					}
					if (k==1)
					{
						break Judge;
					}
				}
				//�ж��Խ���
				k=1;
				FLAG1=aaa[0][0];
				for (int m=0;m<3;m++)
				{
					if (FLAG1==0)
					{
						k=0;
						break;
					}
					FLAG2=aaa[m][m];
					if (FLAG1==FLAG2)
					{
						FLAG1=FLAG2;
						continue;
					}
					k=0;
					break;
				}
				if (k==1)
				{
					break Judge;
				}
				//�ж����Խ���
				k=1;
				FLAG1=aaa[0][2];
				for (int m=0;m<3;m++)
				{
					if (FLAG1==0)
					{
						k=0;
						break;
					}
					FLAG2=aaa[m][2-m];
					if (FLAG1==FLAG2)
					{
						FLAG1=FLAG2;
						continue;
					}
					k=0;
					break;
				}
				if (k==1)
				{
					break Judge;
				}
			}
			//������
			if (k==1)
			{
				System.out.println((i%2+1)+"�Ż�ʤ��");
				break;
			}
		}
	}
}








