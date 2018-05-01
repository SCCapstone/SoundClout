This is the soundclout program!


The object of this program is to communicate with Raspberry Pis that are running rfcomm-pi-server.py 

The Pis will be sent data that tells them how to control their attached motors. 

PLEASE NOTE

The code within requires proper configuration of bluetooth on both the Pi, and the client computer. 

The code will NOT WORK without proper configuration

The testing for this application was done with pytest and can be found at SoundClout\kivy\
To run testing, cd to the kivy directory and type the command python -m pytest
