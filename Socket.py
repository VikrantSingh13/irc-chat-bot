import socket
from config import HOST, PORT, USER, PASS, CHANNEL

def open_socket():
	s = socket.socket()
	s.connect((HOST, PORT))
	s.send(("PASS " + PASS + "\r\n").encode('UTF-8'))
	s.send(("NICK " + USER + "\r\n").encode('UTF-8'))
	s.send(("JOIN #" + CHANNEL + "\r\n").encode('UTF-8'))
	return s
	
def send_message(s, message):
	message_temp = "PRIVMSG #" + CHANNEL + " :" + message
	s.send(message_temp + "\r\n")
	print("Sent: " + message_temp)
	