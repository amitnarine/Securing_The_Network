
import socket,ssl

context = ssl.SSLContext(ssl.PROTOCOL_TLS)
context.verify_mode = ssl.CERT_REQUIRED
context.check_hostname = False
context.load_verify_locations("Downloads/rootCA.crt")

HOST = "192.168.75.128"  # The server's hostname or IP addres
PORT = 65432  # The port used by the server                                                                                                                                                   
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connstream = context.wrap_socket(s, server_hostname="192.168.75.128")                                                                                                               
# Let the Internet worry about how my messages get there

connstream.connect( (HOST, PORT) )

val = input("out: ")
#print("Message is: " + val)

connstream.sendall(val.encode())
data = connstream.recv(1024).decode()
print("in: " + data)
connstream.close()


