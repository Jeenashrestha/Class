from text_to_speech import speak
import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox
ROOT = tk.Tk()

ROOT.withdraw()
# the input dialog
balance= 100
USER_INP = simpledialog.askstring(title="Check your balance",
                                  prompt="1. Send text (*400#)\n 2. Read aloud (1415)")

if USER_INP == '*400#':
    txt = 'Your balance is Rs ' + str(balance)
    messagebox.showinfo("Balance", txt)
elif USER_INP == '1415':
    txt = 'Your balance is Rs ' + str(balance)
    speak(txt, "en", save=False)
else:
    print("Error")
