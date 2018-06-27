package cdSys;

import java.util.ArrayList;

public class cdSys
{
	
	ArrayList<Item> Li = new ArrayList<Item>();
	
	private void add(Item item)
	{
		Li.add(item);
	}
	
	public void list()
	{
		for (Item item : Li)
		{
			item.print();
		}
	}
	
	public static void main(String[] args)
	{
		// TODO Auto-generated method stub
		cdSys a = new cdSys();
		a.add(new CD("a", "b", "c", "d"));
		a.add(new CD("w", "x", "y", "z"));
		a.add(new DVD("aaa", "bbb", "ccc", "ddd"));
		a.list();
	}

}
