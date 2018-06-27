package cdSys;

public class CD extends Item
{
	private String singer;
	
	public CD(String name, String year, String playingTime, String singer)
	{
		super(name, year, playingTime);
		// TODO Auto-generated constructor stub
		this.singer = singer;
	}
	
	public void print()
	{
		System.out.print("CD:");
		super.print();
		System.out.println(singer);
	}

	public static void main(String[] args)
	{
		// TODO Auto-generated method stub
		
	}

}
