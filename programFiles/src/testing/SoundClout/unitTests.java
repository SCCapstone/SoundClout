package SoundClout;

import org.junit.Test;

public class unitTests {
    @Test
    public void UserInputTest(){
        String userInput = null;
        try
        {
          int i =  Integer.parseInt(userInput);
        }
        catch(NumberFormatException ex)
        {
            System.out.println("This is not an integer");
        }
    }
}
