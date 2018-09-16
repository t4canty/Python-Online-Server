#!/bin/python
from socket import *
import os
import socket
users = []
banned = []
Usernames = []
Passwords = []
fd = open("Usercheck.txt", "a+")
fp = open("Passcheck.txt", "a+")
fb = open("Banlist.txt", "a+")
for line in fd:
	Usernames.append(line.strip())
	print(Usernames)
for line in fp:
	Passwords.append(line.strip())
	print(Password)
for line in fb:
	banned.append(line.strip())
	print(banned)
s = socket.socket(AF_INET, SOCK_STREAM);
host = '127.0.0.1'
port = 1134
s.bind((host, port))
s.listen(5)
c, addr = s.accept()
print(Usernames)
print(Passwords)
def auth():
	
	log = "0"	
	c.send(log.encode())
	print(log)
	while log == "0":
		c.send("Username:".encode())
		usercheck = c.recv(1024).decode("ascii")
		print(usercheck)
		c.send("Password:".encode())
		passcheck = c.recv(1024).decode("ascii")
		print(passcheck)
		if usercheck not in Usernames or passcheck not in Passwords or usercheck in banned:
			c.send("Denied".encode())
			c.send(log.encode())
		else:
			c.send("Accepted".encode())
			log = "1"			
			c.send(log.encode())
			menu()
def register():
	register = c.recv(1024).decode("ascii")
	print(register)
	while register == "1":
		c.send("-----REGISTER-----".encode())
		c.send("USERNAME:".encode())
		user = c.recv(1024).decode("ascii")
		print(user)
		c.send("PASSWORD".encode())
		pass1 = c.recv(1024).decode("ascii")
		print(pass1)
		fd.writelines(user)
		fp.writelines(pass1)
		c.send("0".encode())
		register = "0"
	auth()
def menu():
	if user in usernames == "admin":
		c.send("welcome admin".encode())
		c.send("1: List users:".encode())
		c.send("2: List Connected:".encode())
		c.send("3: Shell".encode())
		c.send("4: Echo Message:".encode())
		c.send("5: Ban User".encode())
		c.send("Choice:".encode())
		choice = c.recv(1024).decode("ascii")
		if choice == "1":
			c.send(Usernames.encode())
		elif choice == "2":
			c.send(users.encode())
		elif choice == "3":
			c.send("port:".encode())
			c.send("ip:".encode())
			ip = c.recv(1024).decode("ascii")
			port = c.recv(1024).decode("ascii")
			s.connect((ip, port))
			os.dup2(s.fileno(), 1)
			os.dup2(s.fileno(), 2)
			p = subprocess.call(["/bin/rbash", "-i"])
		elif choice == "4":
			c.send("Message:".encode())
			message = c.recv(5000).decode("ascii")
			c.send(message.encode())
		elif choice == "5":
			ban()
		else:
			c.send("please chose 1-5".encode())
	elif user in usernames == "tom":
		c.send("Welcome Mod:".encode())
		c.send("1: List Connected".encode())
		c.send("2: Ban Users".encode())
		c.send("3: Echo Message".encode())
		c.send("Choice:".encode())
		choice = c.recv(1024).decode("ascii")
		if choice == "1":
			c.send(users.encode())
		elif choice == "2":
			ban()
		elif choice == "3":
			c.send("Message:".encode())
			message = c.recv(1024).decode("ascii")
			c.send(message.encode())
		else:
			c.send("Chose 1-3".encode())
	else:
		c.send("Welcome User".encode())
		c.send("1: List Connected".encode())
		c.send("2: Echo Message".encode())
		c.send("Choice:".encode())
		choice = c.recv(1024).decode("ascii")
		if choice == "1":
			c.send(users.encode())
		else:
			c.send("Message:".encode())
			message = c.recv(1024).decode("ascii")
			c.send(message.encode())

def ban():
	c.send("username".encode())
	user = c.recv(1024).decode("ascii")
	banned.append(user)
while True:
	try:
		users.append(addr)
		print("Connection:", users)
		register()
	except KeyboardInterrupt:
		s.close()
		break
