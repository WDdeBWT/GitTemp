package hme;

import java.io.IOException;
import java.util.HashMap;

public class HME
{
	private HashMap[] Gra = new HashMap[5];
	private HashMap<Integer, HashMap<String, Integer>> Stu = new  HashMap<Integer, HashMap<String, Integer>>();
	
	HME()
	{
		for (int i=0; i<5; i++)
		{
			Gra[i] = new HashMap<String, Integer>();
			Gra[i].put("No:"+i, i);
			Stu.put(i, Gra[i]);
		}
	}
	public void gGet(String s, int n, int index)
	{
		Gra[index].put(s, n);
	}

	public static void main(String[] args)
	{
		// TODO Auto-generated method stub
		HME hme = new HME();
		int n;
		System.out.println(hme.Stu);
		byte[] b1 = new byte[1024];
		try
		{
			int len = System.in.read(b1);
			String s = new String(b1, 0, len);
			hme.gGet(s, 213, 2);
		} catch (IOException e)
		{
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		System.out.println(hme.Stu);
		System.out.println("------------");
	}

}











//