from tkinter import *
import subprocess
import sys

root = Tk()
w = 900
h = 480

root.title("PyTacToe - Credits")
root.iconbitmap("./Assets/Icons/menu.ico")

ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()

x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))

root.resizable(False, False)

def go_back():
    subprocess.Popen(['python', 'src/menu.pyw'])
    sys.exit()

title = Label(root, text="PyTacToe", font=("Arial", 40))
title.pack(side=TOP, pady=10)

name = Label(root, text="Developed by: Enrico Zangari", font=("Arial", 30))
name.pack(side=TOP, pady=20)


github = Label(root, text="GitHub > ahse-not", font=("Arial", 15))
github.pack(side=TOP, pady=20)

itch = Label(root, text="itch.io > asshes", font=("Arial", 15))
itch.pack(side=TOP, pady=20)

website = Label(root, text="Website > https://www.enricozangari.tech", font=("Arial", 15))
website.pack(side=TOP, pady=20)

store = Label(root, text="Store > https://www.ithog.enricozangari.tech", font=("Arial", 15))
store.pack(side=TOP, pady=20)


go_back = Button(root, text="Go Back", font=("Arial", 15), width=7, height=3, background="lightblue", command=go_back)
go_back.pack(anchor=SW, padx=5, pady=1)



root.mainloop()