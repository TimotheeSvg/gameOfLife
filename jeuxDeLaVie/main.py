from tkinter import * 
from itertools import combinations
import time
import random

def drawSquare(coo,color):
    x,y = map(int, coo.split('.'))
    offsetX = x*W_UNIT
    offsetY = y * H_UNIT
    canvas.create_rectangle(offsetX, offsetY, offsetX+W_UNIT,  offsetY + H_UNIT, fill=color)

def drawSquareWhite(coo):
    x,y = map(int, coo.split('.'))
    offsetX = x*W_UNIT
    offsetY = y * H_UNIT
    canvas.create_rectangle(offsetX, offsetY, offsetX+W_UNIT,  offsetY + H_UNIT, fill='white')

def getVoisin(coo):
    x,y = map(int, coo.split('.'))
    cooCheck = []
    for i in range(x-1,x+2):
        for j in range(y-1, y+2):
            if (f"{i}.{j}" != coo):
                cooCheck.append(f"{i}.{j}")
    return cooCheck

def chekVoisin(val):
    voisin = getVoisin(val)
    cmpt = 0
    for i in voisin:
        if i in coordBlackPiece:
            cmpt +=1
    return cmpt

def chekMap(tab):
    newtab = []
    for i in tab:
        voisin = getVoisin(i)
        for y in voisin:
            state = chekVoisin(y)

            if state == 3:
                if y not in newtab:
                    newtab.append(y)
                    drawSquare(y, 'black')
            elif state == 2:
                if (y in coordBlackPiece):
                    if y not in newtab:
                        newtab.append(y)
                        drawSquare(y, 'black')
            elif y in tab:
                drawSquare(y, 'white')

    return newtab

def drawMap():
    for i in coordBlackPiece:
        drawSquare(i, 'black')

def tickClock():
    global coordBlackPiece
    coordBlackPiece = chekMap(coordBlackPiece)
    window.after(1, tickClock)



WIDTH = "1500"
HEIGHT = "960"
W_UNIT = int(WIDTH)//75
H_UNIT = int(HEIGHT)//75

window = Tk()
window.title("Jeu de la vie")
window.geometry(f"{WIDTH}x{HEIGHT}")
window.resizable(width=0, height=0)
canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

for i in range(0, int(WIDTH), W_UNIT):
    canvas.create_line(i,0,i,HEIGHT)

for y in range(0,int(HEIGHT), H_UNIT):
    canvas.create_line(0,y,WIDTH,y)


firstMachine = ["10.10", "11.11", "12.9", "12.10", "12.11"]
helice = ["10.10", "9.10", "11.10"]

coordBlackPiece = ["10.10", "9.9", "9.11", "11.9", "11.10", "11.11"]
drawMap()
tickClock()

# window.after_idle(tickClock)
window.mainloop()