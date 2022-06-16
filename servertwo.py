import socket

HOST = "192.168.75.128"
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)			# specify the “backlog” for this socket
conn, addr = s.accept()  # wait and accept the connection
data = conn.recv(1024)   # read the content of the message
#print("Server says: " + data);
conn.sendall(data)
conn.close()
