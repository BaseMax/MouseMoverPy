import socket
import pyautogui

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        data = s.recv(1024)
        if not data:
            break

        data_str = data.decode('utf-8')
        print(f"Received: {data_str}")

        direction, pixels = data_str.split()
        pixels = int(pixels)

        print("Direction:", direction)
        print("Pixels:", pixels)
        print("")

        if direction == 'R':
            print("Moving right", pixels)
            pyautogui.moveRel(pixels, 0)
        elif direction == 'L':
            print("Moving left", pixels)
            pyautogui.moveRel(-pixels, 0)
        elif direction == 'U':
            print("Moving up", pixels)
            pyautogui.moveRel(0, -pixels)
        elif direction == 'D':
            print("Moving down", pixels)
            pyautogui.moveRel(0, pixels)
