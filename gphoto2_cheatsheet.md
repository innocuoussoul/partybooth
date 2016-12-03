# GPhoto2 Cheat sheet
Some gphoto2 calls that might be useful for a photobooth 

##General
Take Photo and save it with a timestamp as name
    
    gphoto2 --capture-image-and-download --force-overwrite --filename "%m-%d-%Y_%H-%M-%S.%C"

##Nikon D5000 

Set image quality to "JPEG Fine"
	
	gphoto2 --set-config imagequality=2
	
Flip Mirror down

    gphoto --set-config viewfinder 0
    
Capture Movie to named fifo pipe and display using omxplayer

    mkfifo fifo.mjpg
    
    #this has to be started before capturing the movie
    #in a separate terminal or subprocess
    omxplayer fifo.mjpg --live
    gphoto2 --capture-movie --stdout > fifo.mjpg
    
    # Player has to be stopped before gphoto
    # Otherwise the camera will get confused
    killall omxplayer
    killall gphoto2
    
    # flip mirror back down
    gphoto2 --set-config viewfinder 0 
    
    
	

	
