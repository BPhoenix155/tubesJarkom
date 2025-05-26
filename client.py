import sys
import socket
def main():
    if len(sys.argv) != 4:
        print("Usage: python client.py <server_host> <server_port> <filename>")
        return
    host = sys.argv[1]
    port = int(sys.argv[2])
    filename = sys.argv[3]
    request_line = f"GET /{filename} HTTP/1.1\r\nHost: {host}\r\n\r\n"
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(request_line.encode())
        response = b""
        while True:
            data = s.recv(1024)
            if not data:
                break
            response += data
        print("Received response:\n")
        print(response.decode(errors='replace'))
if __name__ == "__main__":
    main()