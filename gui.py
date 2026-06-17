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