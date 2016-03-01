import numpy as np
import cv2
import socket

UDP_IP = "laptop-5eeg2bjq.byod.gmu.edu"
UDP_PORT = 5005

#Read image
image = cv2.imread('robot1.jpg',0)

#Resize image for transfer through UDP
resized = cv2.resize(image,(205,250))

#Convert image to string for transfer through UDP
imagestr = resized.tostring()

print "UDP target IP: ", UDP_IP
print "UDP target port: ", UDP_PORT

sock = socket.socket(socket.AF_INET, #Internet
                socket.SOCK_DGRAM) #UDP
sock.sendto(imagestr, (UDP_IP,UDP_PORT))
