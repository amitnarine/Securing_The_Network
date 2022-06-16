import socket

HOST = "192.168.75.128"  # The server's hostname or IP address
PORT = 65432  # The port used by the server 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Let the Internet worry about how my messages get there
s.connect( (HOST,PORT) )

val = input("out: ")
#print("Message is: " + val)

s.sendall(val.encode())
data = s.recv(1024).decode()
print("in: " + data) 
s.close()
