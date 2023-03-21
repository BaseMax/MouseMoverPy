import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Server is listening on {HOST}:{PORT}")
    conn, addr = s.accept()
    print(f"Connected by {addr}")
    while True:
        data = input("What do you want to do? ")
        conn.sendall(bytes(data, encoding='utf-8'))
