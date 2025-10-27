import socket

HOST = '127.0.0.1'  # Địa chỉ localhost
PORT = 65432        # Cổng bất kỳ (trên 1024)

# Tạo socket TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))      # Gắn địa chỉ & cổng
    s.listen()                # Lắng nghe kết nối
    print(f"Server đang lắng nghe tại {HOST}:{PORT} ...")

    conn, addr = s.accept()   # Chấp nhận kết nối

    print("Client kết nối từ:", addr)

    with conn:
        print(f"Đã kết nối với {addr}")
        while True:
            data = conn.recv(1024)    # Nhận dữ liệu từ client
            if not data:
                break
            print("Client gửi:", data.decode())
            conn.sendall(data)        # Gửi lại (echo)
