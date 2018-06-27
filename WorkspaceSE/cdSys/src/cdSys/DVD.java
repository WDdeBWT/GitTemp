package cdSys;

public class DVD extends Item
{
	
	private String actor;
	
	public DVD(String name, String year, String playingTime, String actor)
	{
		super(name, year, playingTime);
		// TODO Auto-generated constructor stub
		this.actor = actor;
	}
	
	public void print()
	{
		System.out.print("CD:");
		super.print();
		System.out.println(actor);
	}
	
	public static void main(String[] args)
	{
		// TODO Auto-generated method stub
		
	}

}
