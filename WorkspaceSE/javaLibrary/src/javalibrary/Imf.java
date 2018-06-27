package javalibrary;

import java.util.ArrayList;

public class Imf
{
	ArrayList<String> List = new ArrayList<String>();
	public void getIm(String s)
	{
		List.add(s);
	}
	public String putIm(int n)
	{
		return List.get(n);
	}
	public void remove(int n)
	{
		List.remove(n);
	}
	public void change(int n, String s)
	{
		List.set(n, s);
	}
	public String[] getList()
	{
		String[] a = new String[List.size()];
		List.toArray(a);
		return a;
	}
	public int search(String s)
	{
		return List.indexOf(s);
	}

	public static void main(String[] args)
	{
		// TODO Auto-generated method stub

	}

}
