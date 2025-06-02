import socket
import os
def handle_client(connection_socket, client_address):
    try:
        request = connection_socket.recv(1024).decode()
        print(f"terima server dari{client_address}:\n{request}")
        lines = request.splitlines()
        if len(lines) == 0:
            return
        filename = lines[0].split()[1].lstrip("/")
        if os.path.exists(filename):
            with open(filename, "rb") as f:
                content = f.read()
            header = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n"
            response = header.encode() + content
            connection_socket.sendall(response)
        else:
            header = "HTTP/1.1 404 Not Found\r\n\r\n"
            body = "<html><body><h1>404 Not Found</h1></body></html>"
            response = header.encode() + body.encode()
        connection_socket.sendall(response)
    except Exception as e:
        print(f"Error handling client {client_address}: {e}")
    finally:
        connection_socket.close()
def start_server(port=2005):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('', port))
    server_socket.listen(1)
    print(f"server sudah siap di {port}...")
    connection_socket, client_address = server_socket.accept()
    handle_client(connection_socket, client_address)

if __name__ == "__main__":
    start_server()