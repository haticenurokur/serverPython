import socket
import signal
from datetime import datetime
import sys


#def string_compare(str1, str2 = "Waiting"):
#	for i in range (len(str2)):
#		if(str1[i] != str2[i]):
#			return False
#
#	return True 


host = "192.168.0.10"
port = 2525
buf = 1024
bind_arg = (host,port)
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server_socket.bind(bind_arg)
server_socket.listen(1)

server,addr = server_socket.accept()


def signal_handler(sig,frame):
	print( "pressed ctrl + c" )
	server.close()
	server_socket.close()
	sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

def send_message():
	data = "Merhaba, ben raspi!"
	server.send(data.encode())

print(" Got connection from" , addr)

while True:
	msg = server.recv(buf).decode()
	target = "Waiting"
	now = datetime.now()
	today = now.strftime("%d %b %a %H:%M:%S %Z %Y")

	if msg == target:
		print("Output: Merhaba, ben raspi!   - " + str(today))
		send_message()
	else:
		print("Input : " + msg + " - " + str(today))

server.close()
server_socket.close()

