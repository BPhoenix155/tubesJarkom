import socket

serverPort=12000
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(('',serverPort))

serverSocket.listen(1)
print("Server siap, menunggu koneksi dari client...")

while True:
    connectionSocket, client_address = serverSocket.accept()
    print(f"Terhubung dengan client: {client_address}")
    data = connectionSocket.recv(1024).decode()
    print(f"Pesan dari client: {data}")
    response = f"Pesan '{data}' diterima dengan sukses!"
    connectionSocket.send(response.encode())
    connectionSocket.close()
    
    print("Koneksi ditutup, server dimatikan.")
