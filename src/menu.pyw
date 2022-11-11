from tkinter import *
import subprocess
import sys

root = Tk()
w = 900
h = 480

root.title("PyTacToe - Menu")
root.configure(background='grey')
root.iconbitmap("./Assets/Icons/menu.ico")

ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()

x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))

root.resizable(False, False)

#Function to open three by three (t x t)
def txt():
    subprocess.Popen(['python', 'src/three.pyw'])
    sys.exit()

#Function to open four by four (f x f)
def fxf():
    subprocess.Popen(['python', 'src/four.pyw'])
    sys.exit()
def credits():
    subprocess.Popen(['python', 'src/credits.pyw'])
    sys.exit()

title_text = Label(root, text="PyTacToe", font=("Arial", 40), bg="grey")
title_text.pack(side=TOP, pady=50)
three_by_three = Button(root, text="3 x 3", font=("Arial", 30), width=6, height=0, command=txt)
three_by_three.pack(anchor=CENTER)
four_by_four = Button(root, text="4 x 4", font=("Arial", 30), width=6, height=0, command=fxf)
four_by_four.pack(anchor=CENTER, pady=20)
credit = Button(root, text="Credits", font=("Arial", 30), width=6, height=0, command=credits)
credit.pack(anchor=CENTER)


root.mainloop()