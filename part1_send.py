import socket

UDP_IP = "192.168.1.82"
UDP_PORT = 5005
robot_wheels = "8 7"
left_wheel, right_wheel = robot_wheels.split()

print "UDP target IP: ", UDP_IP
print "UDP target port: ", UDP_PORT
print "robot wheels data: ", robot_wheels
print "left wheel: ", left_wheel
print "right wheel: ", right_wheel

sock = socket.socket(socket.AF_INET, #Internet
					socket.SOCK_DGRAM) #UDP
sock.sendto(robot_wheels, (UDP_IP,UDP_PORT))
