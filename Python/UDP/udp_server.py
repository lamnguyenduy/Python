import socket

HOST = ''       # lắng nghe trên mọi IP
PORT = 12345

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((HOST, PORT))
print("UDP server listening on port", PORT)

while True:
    data, addr = sock.recvfrom(1024)
    print(f"Received from {addr}: {data.decode()}")
    sock.sendto(b"Hello UDP Client", addr)
