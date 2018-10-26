
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
	#reg = "1"
	reg = "0"
	print(reg)
	s.send(reg.encode())
	while reg == "1	":
		print(s.recv(100).decode("ascii"))
		print(s.recv(100).decode("ascii"))
		username = input()
		s.send(username.encode())
		print(s.recv(100).decode("ascii"))
		password = input()
		s.send(password.encode())
		reg = s.recv(100).decode("ascii")
		print(reg)
	login()
def login():
	log = s.recv(1024).decode("ascii")
	#log = '0'
	print(log)
	while log == "0":
		print(s.recv(1024).decode("ascii"))
		username = input()
		s.send(username.encode())
		print(s.recv(1024).decode("ascii"))
		password = input()
		s.send(password.encode())
		print(s.recv(1024).decode("ascii"))
		log = s.recv(1024).decode("ascii")
		print(log)
	menu()
def menu():
	while True:
		print("NO LONGER IN LOGIN")
		if username == "admin":
			print("\n", s.recv(1024).decode("ascii"))
			#print("\n", s.recv(1000).decode("ascii"))
			#print("\n", s.recv(1000).decode("ascii"))
			#print("\n", s.recv(1000).decode("ascii"))
			#print("\n", s.recv(1000).decode("ascii"))
			#print("\n",s.recv(1000).decode("ascii"))
			choice = input("Choice:")
			#print(choice)
			s.send(choice.encode())
			if choice == "1":
				print(s.recv(1024).decode("ascii"))
			elif choice == "2":
				print(s.recv(1024).decode("ascii"))
			elif choice == "3":
				print(s.recv(1024).decode("ascii"))
				port = input()
				port = int(port)
				print(s.recv(1024).decode("ascii"))
				ip = input()
				s.send(ip)
				s.send(port)
				system.call(["nc", "-lvp", port])
			elif choice == "4":
				print(s.recv(1024).decode("ascii"))
				s.send(input("Message:").encode())
				print(s.recv(1024).decode("ascii"))
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
