
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.Node;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;

public class Controller {

    @FXML
    private void homeToDeviceTester(ActionEvent event) {
        // Button was clicked, do something...
       try {
           Parent root1 = FXMLLoader.load(getClass().getResource("devicetester.fxml"));
           Node source = (Node) event.getSource();
           Stage stage = (Stage) source.getScene().getWindow();
           stage.setTitle("Test Devices");
           stage.setScene(new Scene(root1));
           stage.show();
       }
       catch (Exception e){

       }
    }
    
    @FXML
    private void testDevice(ActionEvent event)
    {
      try
      {
        Runtime.getRuntime().exec("sudo python testdevice.py");
      
      }
      catch(Exception e)
      {
      }
    }

    @FXML
    private void homeToConnectDevices(ActionEvent event) {
        // Button was clicked, do something...
        try {
            Parent root1 = FXMLLoader.load(getClass().getResource("connectdevices.fxml"));
            Node source = (Node) event.getSource();
            Stage stage = (Stage) source.getScene().getWindow();
            stage.setTitle("Connect Devices");
            stage.setScene(new Scene(root1));
            stage.show();
        }
        catch (Exception e){

        }
    }

    @FXML
    private void scanDevices(ActionEvent event)
    {
      try
      {
        Runtime.getRuntime().exec("sudo python btscan.py > devices.txt"); 
      }
      catch(Exception e)
      {
      }
    }
    
    @FXML
    private void connectDevice(ActionEvent event)
    {
      try
      {
        Runtime.getRuntime().exec("sudo python connect.py >> connecteddevices.txt");
      }
      catch(Exception e)
      {
      }
    }
    @FXML
    private void homeToEditDeviceGroups(ActionEvent event) {
        // Button was clicked, do something...
        try {
            Parent root1 = FXMLLoader.load(getClass().getResource("editdevicegroups.fxml"));
            Node source = (Node) event.getSource();
            Stage stage = (Stage) source.getScene().getWindow();
            stage.setTitle("Edit Device Groups");
            stage.setScene(new Scene(root1));
            stage.show();
        }
        catch (Exception e){

        }
    }

    @FXML
    private void homeToEditGroupBehavior(ActionEvent event) {
        // Button was clicked, do something...
        try {
            Parent root1 = FXMLLoader.load(getClass().getResource("editgroupbehavior.fxml"));
            Node source = (Node) event.getSource();
            Stage stage = (Stage) source.getScene().getWindow();
            stage.setTitle("Edit Group Behavior");
            stage.setScene(new Scene(root1));
            stage.show();
        }
        catch (Exception e){

        }
    }

    @FXML
    private void backToHome(ActionEvent event) {
        // Button was clicked, do something...
        try {
            Parent root1 = FXMLLoader.load(getClass().getResource("home.fxml"));
            Node source = (Node) event.getSource();
            Stage stage = (Stage) source.getScene().getWindow();
            stage.setTitle("Home");
            stage.setScene(new Scene(root1));
            stage.show();
        }
        catch (Exception e){

        }
    }
}
