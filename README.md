# Python Keylogger with Tkinter GUI

A simple Python-based Keylogger application with a graphical user interface (GUI) built using Tkinter. The application captures keyboard keystrokes, displays a live keystroke counter, and stores the logged keys in a text file.

## Features

- User-friendly Tkinter GUI
- Start and Stop Logging functionality
- Real-time keystroke counter
- Logs keystrokes with timestamps
- Stores captured data in a text file
- Simple and lightweight implementation

## Technologies Used

- Python
- Tkinter
- Pynput

## Project Structure

SCT_CS-04/
│
├── main.py
├── gui.py
├── log.txt
├── README.md
└── .gitignore


## Installation

1. Clone the repository:

```bash
git clone <https://github.com/nandinimalge/SCT_CS_04.git>
```

2. Navigate to the project directory:

```bash
cd <SCT_CS_04>
```

3. Install the required package:

```bash
pip install pynput
```

4. Run the application:

```bash
python gui.py
```

## How It Works

- Click **Start Capture** to begin recording keystrokes.
- The application logs each keystroke along with its timestamp.
- The live counter displays the total number of keystrokes captured.
- Click **Stop Capture** to stop logging.

## Learning Outcomes

This project helped in understanding:

- GUI development using Tkinter
- Event handling in Python
- File handling
- Keyboard listeners using Pynput
- Modular Python programming

## Disclaimer

This project was developed strictly for educational and learning purposes. Always obtain proper authorization before monitoring or recording keyboard activity on any device.

## Author

**Nandini Malge**