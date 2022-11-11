from tkinter import *
from tkinter import messagebox
from tkinter.colorchooser import askcolor
import subprocess
import sys

root = Tk()
w = 452
h = 447

root.title("PyTacToe - 3x3")
root.iconbitmap("./Assets/Icons/three_by_three.ico")

ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()


x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))

root.resizable(False, False)

xTurn = True
turn = 0
won = False


def customMessage(title, message, text, command, text2, command2):
    window = Toplevel()
    window.geometry("300x100")
    window.iconbitmap("./Assets/Icons/menu.ico")
    window.title(title)

    window.resizable(False, False)

    Label(window, text=message, font=("Arial", 12)).pack(pady=12)
    Button(window, text=text, command=command, width=6, height=1, bg="lightgrey").place(x=80, y=55)
    Button(window, text=text2, command=command2, width=6, height=1, bg="lightgrey").place(x=155, y=55) 


def goBack():
    subprocess.Popen(['python', 'src/menu.pyw'])
    sys.exit()

def restart(t):

    global xTurn
    global turn
    global won

    won = False
    xTurn = t
    turn = 0
    btn1["text"], btn2["text"], btn3["text"], btn4["text"], btn5["text"], btn6["text"], btn7["text"], btn8["text"], btn9["text"] = "", "", "", "", "", "", "", "", ""

def write(btn):

    global xTurn
    global turn
    global won

    if xTurn == False and btn["text"] == "":
        btn["text"] = "O"
        xTurn = True
        turn += 1
        win()
        tie()
    elif xTurn == True and btn["text"] == "":
        btn["text"] = "X"
        xTurn = False
        turn += 1
        win()
        tie()
    else:
        messagebox.showwarning("ERROR", "You can't place that there, wait until your turn.")


def win():
    global won

        #Horizontal Win Check for X
    if btn1["text"] == "X" and btn2["text"] == "X" and btn3["text"] == "X":
        messagebox.showinfo("WINNER - X | LOSER - O", "X won the game hortizontally. Congrats!")
        won = True
        restart(True)
    elif btn4["text"] == "X" and btn5["text"] == "X" and btn6["text"] == "X":
        messagebox.showinfo("WINNER - X | LOSER - O", "X won the game horizontally. Congrats!")
        won = True
        restart(True)
    elif btn7["text"] == "X" and btn8["text"] == "X" and btn9["text"] == "X":
        messagebox.showinfo("WINNER - X | LOSER - O", "X won the game horizontally. Congrats!")
        won = True
        restart(True)
    #Vertical Win Check for X
    elif btn1["text"] == "X" and btn4["text"] == "X" and btn7["text"] == "X":
        messagebox.showinfo("WINNER - X | LOSER - O", "X won the game vertically. Congrats!")
        won = True
        restart(True)
    elif btn2["text"] == "X" and btn5["text"] == "X" and btn8["text"] == "X":
        messagebox.showinfo("WINNER - X | LOSER - O", "X won the game vertically. Congrats!")
        won = True
        restart(True)
    elif btn3["text"] == "X" and btn6["text"] == "X" and btn9["text"] == "X":
        messagebox.showinfo("WINNER - X | LOSER - O", "X won the game vertically. Congrats!")
        won = True
        restart(True)
    #Diagonal Win Check for X
    elif btn1["text"] == "X" and btn5["text"] == "X" and btn9["text"] == "X":
        messagebox.showinfo("WINNER - X | LOSER - O", "X won the game diagonally. Congrats!")
        won = True
        restart()
    elif btn3["text"] == "X" and btn5["text"] == "X" and btn7["text"] == "X":
        messagebox.showinfo("WINNER - X | LOSER - O", "X won the game diagonally. Congrats!")
        won = True
        restart(True)
    #Horizontal Win Check for O
    elif btn1["text"] == "O" and btn2["text"] == "O" and btn3["text"] == "O":
        messagebox.showinfo("WINNER - O | LOSER - X", "O won the game hortizontally. Congrats!")
        won = True
        restart(False)
    elif btn4["text"] == "O" and btn5["text"] == "O" and btn6["text"] == "O":
        messagebox.showinfo("WINNER - O | LOSER - X", "O won the game horizontally. Congrats!")
        won = True
        restart(False)
    elif btn7["text"] == "O" and btn8["text"] == "O" and btn9["text"] == "O":
        messagebox.showinfo("WINNER - O | LOSER - X", "O won the game horizontally. Congrats!")
        won = True
        restart(False)
    #Vertical Win Check for O
    elif btn1["text"] == "O" and btn4["text"] == "O" and btn7["text"] == "O":
        messagebox.showinfo("WINNER - O | LOSER - X", "O won the game vertically. Congrats!")
        won = True
        restart(False)
    elif btn2["text"] == "O" and btn5["text"] == "O" and btn8["text"] == "O":
        messagebox.showinfo("WINNER - O | LOSER - X", "O won the game vertically. Congrats!")
        won = True
        restart()
    elif btn3["text"] == "O" and btn6["text"] == "O" and btn9["text"] == "O":
        messagebox.showinfo("WINNER - O | LOSER - X", "O won the game vertically. Congrats!")
        won = True
        restart(False)
    #Diagonal Win Check for O
    elif btn1["text"] == "O" and btn5["text"] == "O" and btn9["text"] == "O":
        messagebox.showinfo("WINNER - O | LOSER - X", "O won the game diagonally. Congrats!")
        won = True
        restart(False)
    elif btn3["text"] == "O" and btn5["text"] == "O" and btn7["text"] == "O":
        messagebox.showinfo("WINNER - O | LOSER - X", "O won the game diagonally. Congrats!")
        won = True
        restart(False)


def tie():
    if won == False and turn == 9:
        tryAgain = messagebox.askyesno("IT'S A TIE :(", "It's a tie, care to try again?")
        if tryAgain == True:
            restart(True)
        else:
            goBack()
        





#First row
btn1 = Button(root, text="", font=('Arial', 14), width=13, height=6, command=lambda: write(btn1))
btn2 = Button(root, text="", font=('Arial', 14), width=13, height=6, command=lambda: write(btn2))
btn3 = Button(root, text="", font=('Arial', 14), width=13, height=6, command=lambda: write(btn3))

#Second row
btn4 = Button(root, text="", font=('Arial', 14), width=13, height=6, command=lambda: write(btn4))
btn5 = Button(root, text="", font=('Arial', 14), width=13, height=6, command=lambda: write(btn5))
btn6 = Button(root, text="", font=('Arial', 14), width=13, height=6, command=lambda: write(btn6))

#Third row
btn7 = Button(root, text="", font=('Arial', 14), width=13, height=6, command=lambda: write(btn7))
btn8 = Button(root, text="", font=('Arial', 14), width=13, height=6, command=lambda: write(btn8))
btn9 = Button(root, text="", font=('Arial', 14), width=13, height=6, command=lambda: write(btn9))

#First row grid
btn1.grid(row=0, column=0)
btn2.grid(row=0, column=1)
btn3.grid(row=0, column=2)

#Second row grid
btn4.grid(row=1, column=0)
btn5.grid(row=1, column=1)
btn6.grid(row=1, column=2)

#Third row grid
btn7.grid(row=2, column=0)
btn8.grid(row=2, column=1)
btn9.grid(row=2, column=2)

buttons = [btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9]


def changeText():

    global buttons

    color = askcolor(title="Choose a text color")
    for button in buttons:
        button["fg"] = color[1]


def changeBackground():

    global buttons

    color = askcolor(title="Choose a background color")
    for button in buttons:
        button["bg"] = color[1]

def confirmChangeX():
    confirm = messagebox.askyesno("Are you sure?", "Changing this configuration will reset the game and make X start. \nAre you sure you want to proceed?")
    if confirm == True:
        restart(True)

def confirmChangeO():
    confirm = messagebox.askyesno("Are you sure?", "Changing this configuration will reset the game and make O start. \nAre you sure you want to proceed?")
    if confirm == True:
        restart(False)

def changeStarting():
    customMessage("Changing Starting Player", "What player do you want to start?", "X", confirmChangeX, "O", confirmChangeO)



options = Menu(root)
root.config(menu=options)

file = Menu(options, tearoff=False)
options.add_cascade(label="File", menu=file, underline=0)

file.add_command(label="Exit", command=goBack)

opt = Menu(options, tearoff=False)
options.add_cascade(label="Options", menu=opt, underline=1)

opt.add_command(label="Starting Player", command=changeStarting)

customize = Menu(options, tearoff=False)
options.add_cascade(label="Customize", menu=customize, underline=0)

customize.add_command(label="Text Color", command=changeText)
customize.add_command(label="Background Color", command=changeBackground)

root.mainloop()