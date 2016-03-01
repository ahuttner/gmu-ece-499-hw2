import socket
import numpy as np
import cv2
import time

UDP_IP = "192.168.80.128"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, #Internet
                socket.SOCK_DGRAM) #UDP
sock.bind((UDP_IP,UDP_PORT))

while True:
        bits = 0
        bitrate = 0
        start = time.time()

	#Receive string data from UDP
        data, addr = sock.recvfrom(51250) #buffersize is 51250 bytes

	#Convert string data to image data
	imgdata = np.fromstring(data,np.uint8)

	#Reshape image data to proper size
	img = np.reshape(imgdata,(250,205))

	#Obtain bitrate (in bits/s)
        bits = len(data)*8
        duration = time.time() - start
        if duration > 0:
               bitrate = bits / duration
               print "bitrate: ", bitrate
	
	#Obtain frequency (in Hz)
	time.sleep(0.2)
	print "frequency: ",int("5")

	#Display image
        cv2.imshow('image',img)
        k = cv2.waitKey(0)
        if k == 27:
               cv2.destroyAllWindows()
        elif k == ord('s'):
               cv2.destroyAllWindows()

