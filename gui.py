from tkinter import *
from pynput.keyboard import Listener
from main import write_to_file
from tkinter import messagebox
import os

root = Tk()
root.config(bg="#0D1117")
root.title ("Keylogger")
root.geometry ("400x300")

title_label = Label(root, text="Keystroke Activity Monitor", font=("Consolas",20,"bold"), fg="#39FF14", bg="#0D1117")
title_label.pack(pady=10)

status_label = Label(root, text="Status: Ready...", font=("Consolas",14), fg="yellow", bg="#0D1117")
status_label.pack(pady=10)

count_label = Label(root, text="Total Keystrokes: 0", font=("Consolas",14), fg="white", bg="#0D1117")
count_label.pack()

key_count = 0
listener = None

def update_ui(count):
    root.after(0, lambda: count_label.config(text=f"Total Keystrokes: {count}"))

def on_press(key):
    write_to_file(key, update_ui)

def start_logging():

    global listener

    status_label.config(
         text = "Status: Monitoring...",
         font = ("Consolas", 14),
         fg = "green",
         bg="#0D1117"
    )

    listener = Listener(on_press=on_press)
    listener.start()

def stop_logging():

    global listener

    if listener:
        listener.stop()
        listener = None

    file_path = os.path.abspath("log.txt")

    status_label.config(
        text="Status: Stopped",
        font = ("Consolas", 14),
        fg = "red",
        bg="#0D1117")
    
    messagebox.showinfo(
        "Logging Stopped",
        f"log.txt saved successfully!\n\nPath:\n{file_path}"
    )
   
start_btn = Button(root, text="Start Capture", font=("Consolas", 16, "bold"), fg="black", bg="#39FF14", width=15, command=start_logging)
start_btn.pack(pady=30)

stop_btn = Button(root, text="Stop Capture", font=("Consolas", 16, "bold"), fg="black", bg="#39FF14", width=15, command=stop_logging)
stop_btn.pack(pady=5)



root.mainloop()