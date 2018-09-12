#!/bin/python
import socket
import os
users = []
banned = []
Usernames = []
Passwords = []
fd = open("Usercheck.txt", "ra")
fp = open("Passcheck.txt", "ra")
fb = open("Banlist.txt", "ra")
banned.append(fb.readlines())
Usernames.append(fd.readlines())
Passwords.append(fp.readlines())
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 13370
s.bind((host, port))
s.listen(5)
def connect():
	c, addr = s.accept()
	users.append(addr)
	print ("connection from:", addr)
	register()
def auth():
	usercheck = s.recv(1024)
	passcheck = s.recv(1024)
	if usercheck not in Usernames or passcheck not in Passwords or usercheck in banned:
		c.send("Denied")
	else:
		menu()
def register():
	register = s.recv(1024)
	if register == "1":
		c.send("-----REGISTER-----")
		c.send("USERNAME:")
		user = s.recv(1024)
		c.send("PASSWORD")
		pass1 = s.recv(1024)
		fd.write(user)
		fp.write(pass1)
		c.send("0")
	else:
		auth()
def menu():
	priv = s.recv(1024)
	if priv == "3":
		c.send("welcome admin")
		c.send("1: List users:")
		c.send("2: List Connected:")
		c.send("3: Shell")
		c.send("4: Echo Message:")
		c.send("5: Ban User")
		c.send("Choice:")
		choice = s.recv(1024)
		if choice == "1":
			c.send(Usernames)
		elif choice == "2":
			c.send(users)
		elif choice == "3":
			c.send("port:")
			c.send("ip:")
			ip = s.recv(1024)
			port = s.recv(1024)
			s.connect((ip, port))
			os.dup2(s.fileno(), 1)
			os.dup2(s.fileno(), 2)
			p = subprocess.call(["/bin/rbash", "-i"])
		elif choice == "4":
			c.send("Message:")
			message = s.recv(1024)
			c.send(message)
		elif choice == "5":
			ban()
		else:
			c.send("please chose 1-5")
	elif priv == "2":
		c.send("Welcome Mod:")
		c.send("1: List Connected")
		c.send("2: Ban Users")
		c.send("3: Echo Message")
		c.send("Choice:")
		choice = s.recv(1024)
		if choice == "1":
			c.send(users)
		elif choice == "2":
			ban()
		elif choice == "3":
			c.send("Message:")
			message = s.recv(1024)
			c.send(message)
		else:
			c.send("Chose 1-3")
	else:
		c.send("Welcome User")
		c.send("1: List Connected")
		c.send("2: Echo Message")
		c.send("Choice:")
		choice = s.recv(1024)
		if choice == "1":
			c.send(users)
		else:
			c.send("Message:")
			message = s.recv(1024)
			c.send(message)

def ban():
	c.send("username")
	user = s.recv(1024)
	banned.append(user)



while True:
	try:
		connect()
	except KeyboardInterrupt:
		s.close()
		break
