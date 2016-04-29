import socket
import time

class IRCClient:
	def __init__(self, host, port, nickname, username, realname):
		self.host = host
		self.port = port
		self.nickname = nickname
		self.username = username
		self.realname = realname
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	def connect(self):
		self.sock.connect((self.host, self.port))
		self.sock.send(("NICK " + self.nickname + "\r\n").encode())
		self.sock.send(("USER " + self.username + " 0 * :" + self.realname + "\r\n").encode())

	def messaging(self):
		initialInput = input("What input would u like?")
		initialInput
		self.sock.send((initialInput + "\r\n").encode())
		# self.sock.send(("PRIVMSG " + self.messagechannel + " " + self.message + "\r\n").encode())

	def receive(self):
		while True:
			messages = self.sock.recv(8000).decode()
			self.sock.settimeout(20)
			print(messages)


messageclient = IRCClient("chat.freenode.net", 6667, "bassleb", "bassdogga", "Sebastian")

while True:
	messageclient.connect()
	messageclient.messaging()
	messageclient.receive()