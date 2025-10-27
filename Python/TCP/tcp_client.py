import socket

HOST = '127.0.0.1'  # Địa chỉ server
PORT = 65432        # Cổng trùng với server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print("Đã kết nối đến server.")
    
    while True:
        msg = input("Nhập tin nhắn ('exit' để thoát): ")
        if msg.lower() == 'exit':
            break
        s.sendall(msg.encode())          # Gửi dữ liệu
        data = s.recv(1024)              # Nhận phản hồi
        print("Server trả về:", data.decode())
