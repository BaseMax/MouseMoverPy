# RemoteMouse

## Infected.py

infected.py is a Python script that allows remote control of the mouse cursor on machines where it is executed. The script listens for incoming data from a connected client (running the spy.py program) and moves the mouse cursor based on the received data.

## Prerequisites

To use infected.py, you will need:

Python 3.x installed on your machine
The pyautogui module installed in Python (you can install it using pip install pyautogui)

## Usage

Open a terminal or command prompt and navigate to the directory where infected.py is located.
Run the script using the command python infected.py.
The script will start listening for incoming connections on the default port (5555).
Run the spy.py program on a separate machine to connect to the infected.py script and start controlling the mouse cursor remotely.

## License

This script is provided under the GPL-3.0 License.

## Spy.py

spy.py is a Python script that allows remote control of the mouse cursor on machines where the infected.py script is executed. The script sends data to the infected.py script to move the mouse cursor in different directions based on user input.

## Prerequisites

To use spy.py, you will need:

Python 3.x installed on your machine

## Usage
Open a terminal or command prompt and navigate to the directory where spy.py is located.
Run the script using the command python spy.py.
Enter commands in the format R 30, L 20, U 50, or D 10 to move the mouse cursor right, left, up, or down by the specified number of pixels, respectively.
The script will send the commands to the infected.py script running on a separate machine (where the mouse cursor will be moved accordingly).

## License
This script is provided under the GPL-3.0 License.

I hope this helps you create a clear and comprehensive README for your programs! Let me know if you have any further questions or concerns.
