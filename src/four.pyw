from tkinter import *
import subprocess
import sys

root = Tk()
w = 900
h = 480

root.title("PyTacToe - 4x4")
root.iconbitmap("./Assets/Icons/four_by_four.ico")

ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()

x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))

root.resizable(False, False)

def go_back():
    subprocess.Popen(['python', 'src/menu.pyw'])
    sys.exit()

title_text = Label(root, text="Coming Soon...", font=("Arial", 40))
title_text.pack(anchor=CENTER, pady=30)

title_text = Label(root, text="Contribute to the project on GitHub > ", font=("Arial", 20))
title_text.pack(anchor=CENTER)

back_btn = Button(root, text="Go Back", font=("Arial", 15), width=10, height=1, background="lightblue", command=go_back)
back_btn.pack(anchor=CENTER, pady=50)


root.mainloop()