from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
from random import randint


def checkWinner(p):
    b = [[1, 2, 3], [1, 5, 9],
         [1, 4, 7], [2, 5, 8],
         [3, 6, 9], [3, 5, 7],
         [4, 5, 6], [7, 8, 9]]
    return any(all(i in p for i in c) for c in b)


def isFull():
    return len(p1) + len(p2) >= 9


def isFree(n):
    return n not in p1 and n not in p2

def computerAttack(p):
    if (((all(i in p for i in [7, 5])) or all(i in p for i in [1, 2])) or (all(i in p for i in [9, 6]))) and isFree(3):
        buClick(3)
    elif ((all(i in p for i in [3, 1])) or (all(i in p for i in [8, 5]))) and isFree(2):
        buClick(2)
    elif ((all(i in p for i in [2, 3])) or (all(i in p for i in [9, 5])) or (all(i in p for i in [7, 4]))) and isFree(1):
        buClick(1)
    elif (all(i in p for i in [4, 1])) and isFree(7):
        buClick(7)
    elif ((all(i in p for i in [4, 5])) or (all(i in p for i in [9, 3]))) and isFree(6):
        buClick(6)
    elif ((all(i in p for i in [5, 6])) or (all(i in p for i in [7, 1]))) and isFree(4):
        buClick(4)
    elif(((all(i in p for i in [7, 3])) or (all(i in p for i in [2, 8])) or all(i in p for i in [6, 4]) or (all(i in p for i in [9, 1])))) and isFree(5):
        buClick(5)
    elif ((all(i in p for i in [7, 8])) or (all(i in p for i in [1, 5])) or (all(i in p for i in [6, 3]))) and isFree(9):
        buClick(9)
    elif (((all(i in p for i in [5, 3])) or all(i in p for i in [8, 9]))) and isFree(7):
        buClick(7)
    elif ((all(i in p for i in [7, 9])) or (all(i in p for i in [5, 2]))) and isFree(8):
        buClick(8)
    else:
        computerDefense(p1)


def computerDefense(p):
    if len(p) == 1:
        a = randint(1, 9)
        while a == p[0]:
            a = randint(1, 9)
        buClick(a)

    elif (((all(i in p for i in [7, 5])) or all(i in p for i in [1, 2])) or (all(i in p for i in [9, 6]))) and isFree(3):
        buClick(3)
    elif ((all(i in p for i in [3, 1])) or (all(i in p for i in [8, 5]))) and isFree(2):
        buClick(2)
    elif ((all(i in p for i in [2, 3])) or (all(i in p for i in [9, 5])) or (all(i in p for i in [7, 4]))) and isFree(1):
        buClick(1)
    elif (all(i in p for i in [4, 1])) and isFree(7):
        buClick(7)
    elif ((all(i in p for i in [4, 5])) or (all(i in p for i in [9, 3]))) and isFree(6):
        buClick(6)
    elif ((all(i in p for i in [5, 6])) or (all(i in p for i in [7, 1]))) and isFree(4):
        buClick(4)
    elif(((all(i in p for i in [7, 3])) or (all(i in p for i in [2, 8])) or all(i in p for i in [6, 4]) or (all(i in p for i in [9, 1])))) and isFree(5):
        buClick(5)
    elif ((all(i in p for i in [7, 8])) or (all(i in p for i in [1, 5])) or (all(i in p for i in [6, 3]))) and isFree(9):
        buClick(9)
    elif (((all(i in p for i in [5, 3])) or all(i in p for i in [8, 9]))) and isFree(7):
        buClick(7)
    elif ((all(i in p for i in [7, 9])) or (all(i in p for i in [5, 2]))) and isFree(8):
        buClick(8)

    else:
        b = randint(1, 9)
        while not isFree(b):
            b = randint(1, 9)
        buClick(b)


def setLayout(id, text):
    if (id == 1):
        bu1.config(text=text)
        bu1.state(['disabled'])
    elif id == 2:
        bu2.config(text=text)
        bu2.state(['disabled'])
    elif id == 3:
        bu3.config(text=text)
        bu3.state(['disabled'])

    elif id == 4:
        bu4.config(text=text)
        bu4.state(['disabled'])

    elif id == 5:
        bu5.config(text=text)
        bu5.state(['disabled'])

    elif id == 6:
        bu6.config(text=text)
        bu6.state(['disabled'])

    elif id == 7:
        bu7.config(text=text)
        bu7.state(['disabled'])

    elif id == 8:
        bu8.config(text=text)
        bu8.state(['disabled'])

    elif id == 9:
        bu9.config(text=text)
        bu9.state(['disabled'])


def buClick(id):
    global activePlayer
    if activePlayer == 1:
        setLayout(id, 'X') # player chooses X or O and start playing
        p1.append(id) # append list of moves of the player
        root.title('Tic Tac Toe: You')
        activePlayer = 2
        if checkWinner(p1):
            showinfo('Winner', 'WP, You Won ! ')
            exit()
        if not isFull():
            computerAttack(p2)
        else:
            showinfo('Tied', 'GG WP Tied Game ! ')
            exit()
    else:
        setLayout(id , 'O')
        p2.append(id)
        root.title('Tic Tac Toe: Computer')
        activePlayer = 1
        if checkWinner(p2):
            showinfo('Winner', 'Computer Won ! ')
            exit('GG')
        if isFull():
            showinfo('Tied', 'GG WP Tied Game ! ')
            exit()


def createButtons():
    global bu1, bu2, bu3, bu4, bu5, bu6, bu7, bu8, bu9
    bu1 = ttk.Button(root, text=' ')
    bu1.grid(row=0, column=0, sticky='snew', ipadx=40, ipady=40)
    bu1.config(command=lambda : buClick(1))
    # sticky 'snew' ==> south north east west
    #ipadx, y ==> padding x, y # margin ==> padx, y


    bu2 = ttk.Button(root, text=' ')
    bu2.grid(row=0, column=1, sticky='snew', ipadx=40, ipady=40)
    bu2.config(command=lambda : buClick(2))


    bu3 = ttk.Button(root, text=' ')
    bu3.grid(row=0, column=2, sticky='snew', ipadx=40, ipady=40)
    bu3.config(command=lambda : buClick(3))


    bu4 = ttk.Button(root, text=' ')
    bu4.grid(row=1, column=0, sticky='snew', ipadx=40, ipady=40)
    bu4.config(command=lambda : buClick(4))


    bu5 = ttk.Button(root, text=' ')
    bu5.grid(row=1, column=1, sticky='snew', ipadx=40, ipady=40)
    bu5.config(command=lambda : buClick(5))


    bu6 = ttk.Button(root, text=' ')
    bu6.grid(row=1, column=2, sticky='snew', ipadx=40, ipady=40)
    bu6.config(command=lambda : buClick(6))


    bu7 = ttk.Button(root, text=' ')
    bu7.grid(row=2, column=0, sticky='snew', ipadx=40, ipady=40)
    bu7.config(command=lambda : buClick(7))


    bu8 = ttk.Button(root, text=' ')
    bu8.grid(row=2, column=1, sticky='snew', ipadx=40, ipady=40)
    bu8.config(command=lambda : buClick(8))


    bu9 = ttk.Button(root, text=' ')
    bu9.grid(row=2, column=2, sticky='snew', ipadx=40, ipady=40)
    bu9.config(command=lambda : buClick(9))


root=Tk()
ttk.Style().theme_use('clam')
while 1:
    activePlayer = 1
    p1 = []
    p2 = []
    createButtons()
    root.mainloop()