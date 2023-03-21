# Mouse Mover

`mouse_mover` is a Python program that allows remote control of the mouse cursor on machines where it is executed. The program consists of two scripts - spy.py and infected.py.

## Installation

To use mouse_mover, you will need:

- Python 3.x installed on your machine
- The pyautogui module installed in Python (you can install it using pip install pyautogui)

## Usage

- Open a terminal or command prompt and navigate to the directory where mouse_mover is located.
- Run the infected.py script using the command python infected.py.
- The script will start listening for incoming connections on the default port (65432).
- Run the spy.py script on a separate machine to connect to the infected.py script and start controlling the mouse cursor remotely.

### `spy.py`

`spy.py` is the client script that sends data to the infected.py script to move the mouse cursor in different directions based on user input.

To use spy.py, follow these steps:

- Open a terminal or command prompt and navigate to the directory where spy.py is located.
- Run the script using the command python spy.py.
- Enter commands in the format R 30, L 20, U 50, or D 10 to move the mouse cursor right, left, up, or down by the specified number of pixels, respectively.
- The script will send the commands to the infected.py script running on a separate machine (where the mouse cursor will be moved accordingly).

### `infected.py`

`infected.py` is the server script that listens for incoming connections from the spy.py script and moves the mouse cursor based on the received data.

To use infected.py, follow these steps:

- Open a terminal or command prompt and navigate to the directory where infected.py is located.
- Run the script using the command python infected.py.
- The script will start listening for incoming connections on the default port (65432).
- Once the spy.py script connects to the infected.py script, the mouse cursor will start moving based on the commands sent by the spy.py script.

## License

This program is provided under the GPL-3.0 License.

I hope this helps you create a clear and comprehensive README for your program! Let me know if you have any further questions or concerns.

Copyright Ali, 2023
