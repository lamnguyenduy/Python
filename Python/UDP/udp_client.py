import socket

SERVER_IP = "127.0.0.1"
SERVER_PORT = 12345

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

message = b"Hello UDP Server"
sock.sendto(message, (SERVER_IP, SERVER_PORT))

data, addr = sock.recvfrom(1024)
print("Received from server:", data.decode())

sock.close()
