#!/bin/python
from socket import *
import os
import socket
users = []
banned = []
Usernames = []
Passwords = []
with open("Usercheck.txt") as fd:
	for line in fd:
		Usernames.append(line.strip())
		print(Usernames)
with open("Passcheck.txt") as fp:
	for line in fp:
		Passwords.append(line.strip())
		print(Passwords)
with open("Banlist.txt") as fb:
	for line in fb:
		banned.append(line.strip())
		print(banned)
fd = open("Usercheck.txt", "a")
fp = open("Passcheck.txt", "a")
fb = open("Banlist.txt", "a")
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
		print(Usernames)
		c.send("Password:".encode())
		passcheck = c.recv(1024).decode("ascii")
		print(passcheck)
		print(Passwords)
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
	while True:
		if "admin" in  Usernames:
			#c.send("welcome admin".encode())
			c.send("BEGIN MENU \n 1: List users:\n 2: List connected \n 3: Shell\n 4: Message \n 5: Ban".encode())
			choice = c.recv(1024).decode("ascii")
			print(choice)
			if choice == "1":
				user1 = ''.join(Usernames)
				c.send(user1.encode())
			elif choice == "2":
				user1 = ''.join(users)
				c.send(user1.encode())
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
		elif "tom" in Usernames:
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
	c.send("username:".encode())
	user = c.recv(1024).decode("ascii")
	banned.append(user)
while True:
	try:
		while True:
			users.append(addr)
			print("Connection:", users)
			register()
			print (c.recv(1024))
	except KeyboardInterrupt:
		s.close()
		break
