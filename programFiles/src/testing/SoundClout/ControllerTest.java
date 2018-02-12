package SoundClout;

import org.junit.Test;

import javax.swing.*;
import java.util.Scanner;
import java.io.File;
import java.awt.event.ActionEvent;

import static org.junit.Assert.*;

public class ControllerTest {
    @Test
    public void disconnect() throws Exception {
        //checks the list of connected devices before and after disconnect is pressed
        File file = new File("devices.txt");
        Scanner inputFile = new Scanner (file);
        String beforeConnect = inputFile.toString();
        Controller c = new Controller();
        javafx.event.ActionEvent mock = new javafx.event.ActionEvent();
        c.disconnect(mock);
        String afterConnect = inputFile.toString();
        if (beforeConnect != afterConnect){
            System.out.print("device has disconnected");
        }
        else{
            System.out.println("device has not disconnected");
        }

    }
}