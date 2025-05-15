import socket

serverName='servername'
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverPort=12000
clientSocket.connect(('',serverPort))
message = "Halo dari client 103012330330"
clientSocket.send(message.encode())
response = clientSocket.recv(1024).decode()
print(f"Balasan dari server: {response}")
clientSocket.close()
