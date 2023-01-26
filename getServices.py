import socket

def scan(ip,port,l):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.settimeout(2)
	space = 10 - l
	space = " " * space
	if s.connect_ex((ip,port)):
		return None
	else :
		try:
			service = socket.getservbyport(port)
			print(str(port) + "/TCP" + space + service)
		except socket.error:
			print(str(port) + "/TCP" + space + "Unknown")

		except KeyboardInterrupt:
			print("[-] Exiting!")
			exit(1)
		


	return True 
# scan("127.94.185.106", 80,0)