import socket
import time

UDP_IP = "10.159.253.209"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, #Internet
					socket.SOCK_DGRAM) #UDP
sock.bind((UDP_IP,UDP_PORT))

while True:
	bits = 0
	bitrate = 0
	start = time.time()

	#Obtain data from UDP
	data, addr = sock.recvfrom(1024) #buffersize is 1024 bytes

	#Display received data
	print "received data: ", data
	left_wheel, right_wheel = data.split()
	print "left wheel: ", left_wheel
	print "right wheel: ", right_wheel

	#Display data's values doubled
	left_wheel_doubled = left_wheel * 2
	right_wheel_doubled = right_wheel * 2
	print "left wheel doubled: ", left_wheel_doubled
	print "right wheel doubled: ", right_wheel_doubled
	
	#Obtain bitrate (in bits/s)
	bits = len(data)*8
	duration = time.time() - start
	if duration > 0:
		bitrate = bits / duration
		print "bitrate: ", bitrate
	
