from random import randint
from engine import *
def levelZero(mapVal,move):
    count = 0
    validity = False
    while(move.checkMapIfWin(mapVal) == False and move.checkIfDraw(mapVal) == False):
        try:
            if(move.moveNow == "X"):
                print("TURN OF: " + move.X)
                if(move.X == "PERSON"):
                    x, y = input("input x and y: ").split()
                    while(move.inputXYValid(mapVal,x,y) == False):
                        x, y = input("Inavlid input try again x and y: ").split()
                    mapVal = move.addX(mapVal,x,y)    
                        
                else:
                    x_bot = randint(0, 2)
                    y_bot = randint(0, 2)
                    while(move.inputXYValid(mapVal,x_bot,y_bot) == False):
                        x_bot = randint(0, 2)
                        y_bot = randint(0, 2)
                    mapVal = move.addX(mapVal,x_bot,y_bot)              
                move.moveNow = "O"
                printMaze(mapVal)
            else:
                print("TURN OF: " + move.O)
                if(move.O == "PERSON"):
                    x, y = input("input x and y: ").split()
                    while(move.inputXYValid(mapVal,x,y) == False):
                        x, y = input("Inavlid input try again x and y: ").split()
                    mapVal = move.addO(mapVal,x,y)        
                else:
                    x_bot = randint(0, 2)
                    y_bot = randint(0, 2)
                    while(move.inputXYValid(mapVal,x_bot,y_bot) == False):
                        x_bot = randint(0, 2)
                        y_bot = randint(0, 2)
                    mapVal = move.addO(mapVal,x_bot,y_bot) 
                move.moveNow = "X"
                printMaze(mapVal)
        except ValueError:
            print("put a space between x and y")
        count = count + 1
    printMaze(mapVal)
    
    return None
def printMaze(maze):
    print("/////////////////////////////////////////")
    for m in maze:
        print (*m, sep=" ")
    print("/////////////////////////////////////////")