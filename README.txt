This is the soundclout program!


The object of this program is to communicate with Raspberry Pis that are running rfcomm-pi-server.py 

The Pis will be sent data that tells them how to control their attached motors. 

PLEASE NOTE

The code within requires proper configuration of bluetooth on both the Pi, and the client computer. 

The code will NOT WORK without proper configuration

The testing for this application was done with Junit and can be found in ProgramFiles/src/testing.
Use the command java -cp .:/usr/share/java/junit.jar org.junit.runner.JUnitCore [test class name].
