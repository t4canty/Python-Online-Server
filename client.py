
from socket import *
import socket
import os
username=""
#host = input("host:")
#port = input("port:")
host = '127.0.0.1'
port = 1134
port = int(port)
s = socket.socket(AF_INET, SOCK_STREAM)
s.connect((host, port))
def register():
	reg = "1"
	print(reg)
	s.send(reg.encode())
	while reg == "1":
		print(s.recv(1024).decode("ascii"))
		print(s.recv(1024).decode("ascii"))
		s.send(input("Username:").encode())
		print(s.recv(1024).decode("ascii"))
		s.send(input("Password:").encode())
		reg = s.recv(1024).decode("ascii")
		print(reg)
	login()
def login():
	log = s.recv(100).decode("ascii")
	print(log)
	while log == "0":
		print(s.recv(400).decode("ascii"))
		username = input()		
		s.send(username.encode())
		print(s.recv(1024).decode("ascii"))
		password = input()		
		s.send(password.encode())
		print(s.recv(400).decode("ascii"))
		log = s.recv(100).decode("ascii")
	menu()
def menu():
	if username == "admin":
		print(s.recv(1024).decode("ascii"))
		print(s.recv(1024).decode("ascii"))
		print(s.recv(1024).decode("ascii"))
		print(s.recv(1024).decode("ascii"))
		print(s.recv(1024).decode("ascii"))
		print(s.recv(1024).decode("ascii"))
		print(s.recv(1024).decode("ascii"))
		choice = input("Choice:")
		s.send(choice.encode())
		if choice == "1":
			print(s.recv(1024).decode("ascii"))
		elif choice == "2":
			print(s.recv(1024).decode("ascii"))
		elif choice == "3":
			print(s.recv(1024).decode("ascii"))
			port = input()
			print(s.recv(1024).decode("ascii"))
			ip = input()
			s.send(ip)
			s.send(port)
			system.call(["nc", "-lvp", port])
		elif choice == "4":
			print(s.recv(1024).decode("ascii"))
			s.send(input("Message:").encode())
			print(s.recv(5000).decode("ascii"))
		elif choice == "5":
			print(s.recv(1024).decode("ascii"))
			s.send(input().encode())
		else:
			print(s.recv(1024).decode("ascii"))
	elif username == "tom":
		print(s.recv(1024).decode("ascii"))
		print(s.recv(1024).decode("ascii"))
		print(s.recv(1024).decode("ascii"))
		print(s.recv(1024).decode("ascii"))
		print(s.recv(1024).decode("ascii"))
		choice == input()
		s.send(choice.encode())
		if choice == "1":
			print(s.recv(1024).decode("ascii"))
		elif choice == "2":
			print(s.recv(1024).decode("ascii"))
			s.send(input().encode())
		elif choice == "3":
			print(s.recv(1024).decode("ascii"))
			s.send(input().encode())
			print(s.recv(1024).decode("ascii"))
		else:
			print(s.recv(1024).decode("ascii"))
	else:
		print(s.recv(1024).decode("ascii"))
		print(s.recv(1024).decode("ascii"))
		print(s.recv(1024).decode("ascii"))
		print(s.recv(1024).decode("ascii"))
		choice = input()
		s.send(choice.encode())
		if choice == "1":
			print(s.recv(1024).decode("ascii"))
		else:
			print(s.recv(1024).decode("ascii"))
			s.send(input().encode())
			print(s.recv(1024).decode("ascii"))
while True:
	try:
		register()
	except KeyboardInterrupt:
		s.close()
		break
