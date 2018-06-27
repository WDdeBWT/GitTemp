package cdSys;

public class Item
{
	private String name;
	private String year;
	private String playingTime;
	
	public Item(String name, String year, String playingTime)
	{
		super();
		this.name = name;
		this.year = year;
		this.playingTime = playingTime;
	}
	
	protected void print()
	{
		System.out.print(name+" "+year+" "+playingTime+" ");
	}
	
	public static void main(String[] args)
	{
		// TODO Auto-generated method stub
		
	}

}
