import socket
import time

UDP_IP = "198.168.1.82"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, #Internet
					socket.SOCK_DGRAM) #UDP
sock.bind((UDP_IP,UDP_PORT))

while True:
	bits = 0
	bitrate = 0
	start = time.time()
	data, addr = sock.recvfrom(1024) #buffersize is 1024 bytes
	print "received data: ", data
	left_wheel, right_wheel = data.split()
	print "left wheel: ", left_wheel
	print "right wheel: ", right_wheel
	left_wheel_doubled = left_wheel * 2
	right_wheel_doubled = right_wheel * 2
	print "left wheel doubled: ", left_wheel_doubled
	print "right wheel doubled: ", right_wheel_doubled
	
	
	bits = len(data)*8
	
	duration = time.time() - start
	
	if duration > 0:
		bitrate = bits / duration
		print "bitrate: ", bitrate
	
