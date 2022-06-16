import socket, ssl

context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain(certfile="mydomain.com.crt", keyfile="mydomain.com.key")

HOST = "192.168.75.128"
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

connstream = context.wrap_socket(s, server_side=True)

connstream.bind((HOST, PORT))
connstream.listen(1)			# specify the “backlog” for this socket
conn, addr = connstream.accept()  # wait and accept the connection
data = conn.recv(1024)   # read the content of the message
conn.sendall(data)
#print("Server says: " + data);
conn.close()
