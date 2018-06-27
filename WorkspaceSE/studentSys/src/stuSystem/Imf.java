package stuSystem;

import java.util.HashMap;

public class Imf
{
	HashMap<String,String> hMap = new HashMap<String,String>(); 
	
	public void putIm(String s, String w)
	{
		hMap.put(s, w);
	}
	public String getIm(String s)
	{
		return hMap.get(s);
	}
	public void removeIm(String s)
	{
		hMap.remove(s);
	}
	
	public static void main(String[] args)
	{
		// TODO Auto-generated method stub
		Imf Im = new Imf();
		Im.putIm("sad", "dasjewl");
		Im.putIm("sadw", "asdkl");
		Im.putIm("sasaddw", "asdqwqwkl");
		String r = Im.getIm("sad");
		System.out.println(r);
		for (String t : Im.hMap.keySet())
		{
			System.out.println(Im.getIm(t));
		}
	}
}









//