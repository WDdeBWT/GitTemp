package castleTest;

import java.util.HashMap;

public class Room
{
    public String description;
    
    public HashMap<String, Room> NR = new HashMap<String, Room>();
    
    public Room(String description) 
    {
        this.description = description;
    }
    
    public Room changeRoom(String direction) 
    {
        Room nextRoom = null;
        nextRoom = NR.get(direction);
        return nextRoom;
    }

    public void setExits(String key, Room value) 
    {
        NR.put(key, value);
    }

    @Override
    public String toString() 
    {
        return description;
    }
}
