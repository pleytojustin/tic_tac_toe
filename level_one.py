from random import randint
from engine import *
def levelOne(mapVal,move):
    count = 0
    validity = False
    #least to best 
    priorityMoves = [(1,1), (0,0), (0,2), (2,0), (2,2), (0,1), (1,0), (2,1), (1,2)]
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

                    x_bot, y_bot = checkWinningMove(mapVal,"X")
                    if(x_bot == None):
                        x_bot, y_bot = checkBlockingMove(mapVal,"O")
                    if(x_bot == None):
                        x_bot, y_bot = moveViaPriority(mapVal,priorityMoves)

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

                    x_bot, y_bot = checkWinningMove(mapVal,"O")
                    if(x_bot == None):
                        x_bot, y_bot = checkBlockingMove(mapVal,"X")
                    if(x_bot == None):
                        x_bot, y_bot = moveViaPriority(mapVal,priorityMoves)

                    mapVal = move.addO(mapVal,x_bot,y_bot) 
                move.moveNow = "X"
                printMaze(mapVal)
        except ValueError:
            print("put a space between x and y")
        count = count + 1
    printMaze(mapVal)
    checkWinningMove(mapVal,"X")
    return None
def moveViaPriority(mapVal, priority):
    x = 0
    y = 0
    for p in priority:
        if(mapVal[p[0]][p[1]] == "_"):
            return p[0], p[1]

    return x, y
def checkBlockingMove(mapVal,symbol):
        x = None
        y = None
        print("check blocking move symbol: " + str(symbol) )
        if(symbol == "X"):
                ########
                # FOR X 
                ########

                # X X *
                # _ _ _
                # _ _ _
                if(mapVal[0][0] == "X" and mapVal[0][1] == "X" and mapVal[0][2] == "_"):
                        print("for the block!")
                        x = 0
                        y = 2
                # X * X
                # _ _ _
                # _ _ _                
                elif(mapVal[0][0] == "X" and mapVal[0][2] == "X"  and mapVal[0][1] == "_"):
                        print("for the block!")
                        x = 0
                        y = 1
                # * X X
                # _ _ _
                # _ _ _                
                elif(mapVal[0][1] == "X" and mapVal[0][2] == "X"  and mapVal[0][0] == "_"):
                        print("for the block!")
                        x = 0
                        y = 0


                # _ _ _
                # X X *
                # _ _ _
                if(mapVal[1][0] == "X" and mapVal[1][1] == "X"  and mapVal[1][2] == "_"):
                        print("for the block!")
                        x = 1
                        y = 2
                # _ _ _
                # X * X
                # _ _ _                
                elif(mapVal[1][0] == "X" and mapVal[1][2] == "X"  and mapVal[1][1] == "_"):
                        print("for the block!")
                        x = 1
                        y = 1
                # _ _ _
                # * X X
                # _ _ _                
                elif(mapVal[1][1] == "X" and mapVal[1][2] == "X"  and mapVal[1][0] == "_"):
                        print("for the block!")
                        x = 1
                        y = 0


                # _ _ _
                # _ _ _
                # X X *
                elif(mapVal[2][0] == "X" and mapVal[2][1] == "X"  and mapVal[2][2] == "_"):
                        print("for the block!")
                        x = 2
                        y = 2
                # _ _ _
                # _ _ _
                # X * X                
                elif(mapVal[2][0] == "X" and mapVal[2][2] == "X"  and mapVal[2][1] == "_"):
                        print("for the block!")
                        x = 2
                        y = 1
                # _ _ _
                # _ _ _
                # * X X               
                elif(mapVal[2][1] == "X" and mapVal[2][2] == "X"  and mapVal[2][0] == "_"):
                        print("for the block!")
                        x = 2
                        y = 0



                # X _ _
                # X _ _
                # * _ _                
                elif(mapVal[0][0] == "X" and mapVal[1][0] == "X"  and mapVal[2][0] == "_"):
                        print("for the block!")
                        x = 2
                        y = 0
                # X _ _
                # * _ _
                # X _ _                
                elif(mapVal[0][0] == "X" and mapVal[2][0] == "X"  and mapVal[1][0] == "_"):
                        print("for the block!")
                        x = 1
                        y = 0
                # * _ _
                # X _ _
                # X _ _                
                elif(mapVal[1][0] == "X" and mapVal[2][0] == "X"  and mapVal[0][0] == "_"):
                        print("for the block!")
                        x = 0
                        y = 0


                # _ X _
                # _ X _
                # _ * _                
                elif(mapVal[0][1] == "X" and mapVal[1][1] == "X"  and mapVal[2][1] == "_"):
                        print("for the block!")
                        x = 2
                        y = 1
                # _ X _
                # _ * _
                # _ X _                
                elif(mapVal[0][1] == "X" and mapVal[1][2] == "X"  and mapVal[1][1] == "_"):
                        print("for the block!")
                        x = 1
                        y = 1
                # _ * _
                # _ X _
                # _ X _                
                elif(mapVal[1][1] == "X" and mapVal[2][1] == "X"  and mapVal[0][1] == "_"):
                        print("for the block!")
                        x = 0
                        y = 1
                

                # _ _ X
                # _ _ X
                # _ _ *                
                elif(mapVal[0][2] == "X" and mapVal[1][2] == "X"  and mapVal[2][2] == "_"):
                        print("for the block!")
                        x = 2
                        y = 2
                # _ _ X
                # _ _ *
                # _ _ X                
                elif(mapVal[0][2] == "X" and mapVal[2][2] == "X"  and mapVal[1][2] == "_"):
                        print("for the block!")
                        x = 1
                        y = 2
                # _ _ *
                # _ _ X
                # _ _ X                
                elif(mapVal[1][2] == "X" and mapVal[2][2] == "X"  and mapVal[0][2] == "_"):
                        print("for the block!")
                        x = 0
                        y = 2
        


                # X _ _
                # _ X _
                # _ _ *                
                elif(mapVal[0][0] == "X" and mapVal[1][1] == "X"  and mapVal[2][2] == "_"):
                        print("for the block!")
                        x = 2
                        y = 2
                # X _ _
                # _ * _
                # _ _ X              
                elif(mapVal[0][0] == "X" and mapVal[2][2] == "X"  and mapVal[1][1] == "_"):
                        print("for the block!")
                        x = 1
                        y = 1
                # * _ _
                # _ X _
                # _ _ X               
                elif(mapVal[1][1] == "X" and mapVal[2][2] == "X"  and mapVal[0][0] == "_"):
                        print("for the block!")
                        x = 0
                        y = 0
        else:
                ########
                # FOR O 
                ########

                # O O *
                # _ _ _
                # _ _ _
                if(mapVal[0][0] == "O" and mapVal[0][1] == "O"  and mapVal[0][2] == "_"):
                        print("for the block!")
                        x = 0
                        y = 2
                # O * O
                # _ _ _
                # _ _ _                
                elif(mapVal[0][0] == "O" and mapVal[0][2] == "O"  and mapVal[0][1] == "_"):
                        print("for the block!")
                        x = 0
                        y = 1
                # * O O
                # _ _ _
                # _ _ _                
                elif(mapVal[0][1] == "O" and mapVal[0][2] == "O"  and mapVal[0][0] == "_"):
                        print("for the block!")
                        x = 0
                        y = 0


                # _ _ _
                # O O *
                # _ _ _
                if(mapVal[1][0] == "O" and mapVal[1][1] == "O"  and mapVal[1][2] == "_"):
                        print("for the block!")
                        x = 1
                        y = 2
                # _ _ _
                # O * O
                # _ _ _                
                elif(mapVal[1][0] == "O" and mapVal[1][2] == "O"  and mapVal[1][1] == "_"):
                        print("for the block!")
                        x = 1
                        y = 1
                # _ _ _
                # * O O
                # _ _ _                
                elif(mapVal[1][1] == "O" and mapVal[1][2] == "O"  and mapVal[1][0] == "_"):
                        print("for the block!")
                        x = 1
                        y = 0


                # _ _ _
                # _ _ _
                # O O *
                elif(mapVal[2][0] == "O" and mapVal[2][1] == "O"  and mapVal[2][2] == "_"):
                        print("for the block!")
                        x = 2
                        y = 2
                # _ _ _
                # _ _ _
                # O * O               
                elif(mapVal[2][0] == "O" and mapVal[2][2] == "O"  and mapVal[2][1] == "_"):
                        print("for the block!")
                        x = 2
                        y = 1
                # _ _ _
                # _ _ _
                # * O O              
                elif(mapVal[2][1] == "O" and mapVal[2][2] == "O"  and mapVal[2][0] == "_"):
                        print("for the block!")
                        x = 2
                        y = 0



                # O _ _
                # O _ _
                # * _ _                
                elif(mapVal[0][0] == "O" and mapVal[1][0] == "O"  and mapVal[2][0] == "_"):
                        print("for the block!")
                        x = 2
                        y = 0
                # O _ _
                # * _ _
                # O _ _                
                elif(mapVal[0][0] == "O" and mapVal[2][0] == "O"  and mapVal[1][0] == "_"):
                        print("for the block!")
                        x = 1
                        y = 0
                # * _ _
                # O _ _
                # O _ _                
                elif(mapVal[1][0] == "O" and mapVal[2][0] == "O"  and mapVal[0][0] == "_"):
                        print("for the block!")
                        x = 0
                        y = 0


                # _ O _
                # _ O _
                # _ * _                
                elif(mapVal[0][1] == "O" and mapVal[1][1] == "O"  and mapVal[2][1] == "_"):
                        print("for the block!")
                        x = 2
                        y = 1
                # _ O _
                # _ * _
                # _ O _                
                elif(mapVal[0][1] == "O" and mapVal[1][2] == "O"  and mapVal[1][1] == "_"):
                        print("for the block!")
                        x = 1
                        y = 1
                # _ * _
                # _ O _
                # _ O _                
                elif(mapVal[1][1] == "O" and mapVal[2][1] == "O"  and mapVal[0][1] == "_"):
                        print("for the block!")
                        x = 0
                        y = 1
                

                # _ _ O
                # _ _ O
                # _ _ *                
                elif(mapVal[0][2] == "O" and mapVal[1][2] == "O"  and mapVal[2][2] == "_"):
                        print("for the block!")
                        x = 2
                        y = 2
                # _ _ O
                # _ _ *
                # _ _ O              
                elif(mapVal[0][2] == "O" and mapVal[2][2] == "O"  and mapVal[1][2] == "_"):
                        print("for the block!")
                        x = 1
                        y = 2
                # _ _ *
                # _ _ O
                # _ _ O   
                elif(mapVal[1][2] == "O" and mapVal[2][2] == "O"  and mapVal[0][2] == "_"):
                        print("for the block!")
                        x = 0
                        y = 2
        


                # O _ _
                # _ O _
                # _ _ *                
                elif(mapVal[0][0] == "O" and mapVal[1][1] == "O"  and mapVal[2][2] == "_"):
                        print("for the block!")
                        x = 2
                        y = 2
                # O _ _
                # _ * _
                # _ _ O             
                elif(mapVal[0][0] == "O" and mapVal[2][2] == "O"  and mapVal[1][1] == "_"):
                        print("for the block!")
                        x = 1
                        y = 1
                # * _ _
                # _ O _
                # _ _ O               
                elif(mapVal[1][1] == "O" and mapVal[2][2] == "O"  and mapVal[0][0] == "_"):
                        print("for the block!")
                        x = 0
                        y = 0        
        return x,y 
def checkWinningMove(mapVal,symbol):
        x = None
        y = None
        print("check winning move")
        if(symbol == "X"):
                ########
                # FOR X 
                ########

                # X X *
                # _ _ _
                # _ _ _
                if(mapVal[0][0] == "X" and mapVal[0][1] == "X" and mapVal[0][2] == "_"):
                        print("for the win!")
                        x = 0
                        y = 2
                # X * X
                # _ _ _
                # _ _ _                
                elif(mapVal[0][0] == "X" and mapVal[0][2] == "X"  and mapVal[0][1] == "_"):
                        print("for the win!")
                        x = 0
                        y = 1
                # * X X
                # _ _ _
                # _ _ _                
                elif(mapVal[0][1] == "X" and mapVal[0][2] == "X"  and mapVal[0][0] == "_"):
                        print("for the win!")
                        x = 0
                        y = 0


                # _ _ _
                # X X *
                # _ _ _
                if(mapVal[1][0] == "X" and mapVal[1][1] == "X"  and mapVal[1][2] == "_"):
                        print("for the win!")
                        x = 1
                        y = 2
                # _ _ _
                # X * X
                # _ _ _                
                elif(mapVal[1][0] == "X" and mapVal[1][2] == "X"  and mapVal[1][1] == "_"):
                        print("for the win!")
                        x = 1
                        y = 1
                # _ _ _
                # * X X
                # _ _ _                
                elif(mapVal[1][1] == "X" and mapVal[1][2] == "X"  and mapVal[1][0] == "_"):
                        print("for the win!")
                        x = 1
                        y = 0


                # _ _ _
                # _ _ _
                # X X *
                elif(mapVal[2][0] == "X" and mapVal[2][1] == "X"  and mapVal[2][2] == "_"):
                        print("for the win!")
                        x = 2
                        y = 2
                # _ _ _
                # _ _ _
                # X * X                
                elif(mapVal[2][0] == "X" and mapVal[2][2] == "X"  and mapVal[2][1] == "_"):
                        print("for the win!")
                        x = 2
                        y = 1
                # _ _ _
                # _ _ _
                # * X X               
                elif(mapVal[2][1] == "X" and mapVal[2][2] == "X"  and mapVal[2][0] == "_"):
                        print("for the win!")
                        x = 2
                        y = 0



                # X _ _
                # X _ _
                # * _ _                
                elif(mapVal[0][0] == "X" and mapVal[1][0] == "X"  and mapVal[2][0] == "_"):
                        print("for the win!")
                        x = 2
                        y = 0
                # X _ _
                # * _ _
                # X _ _                
                elif(mapVal[0][0] == "X" and mapVal[2][0] == "X"  and mapVal[1][0] == "_"):
                        print("for the win!")
                        x = 1
                        y = 0
                # * _ _
                # X _ _
                # X _ _                
                elif(mapVal[1][0] == "X" and mapVal[2][0] == "X"  and mapVal[0][0] == "_"):
                        print("for the win!")
                        x = 0
                        y = 0


                # _ X _
                # _ X _
                # _ * _                
                elif(mapVal[0][1] == "X" and mapVal[1][1] == "X"  and mapVal[2][1] == "_"):
                        print("for the win!")
                        x = 2
                        y = 1
                # _ X _
                # _ * _
                # _ X _                
                elif(mapVal[0][1] == "X" and mapVal[1][2] == "X"  and mapVal[1][1] == "_"):
                        print("for the win!")
                        x = 1
                        y = 1
                # _ * _
                # _ X _
                # _ X _                
                elif(mapVal[1][1] == "X" and mapVal[2][1] == "X"  and mapVal[0][1] == "_"):
                        print("for the win!")
                        x = 0
                        y = 1
                

                # _ _ X
                # _ _ X
                # _ _ *                
                elif(mapVal[0][2] == "X" and mapVal[1][2] == "X"  and mapVal[2][2] == "_"):
                        print("for the win!")
                        x = 2
                        y = 2
                # _ _ X
                # _ _ *
                # _ _ X                
                elif(mapVal[0][2] == "X" and mapVal[2][2] == "X"  and mapVal[1][2] == "_"):
                        print("for the win!")
                        x = 1
                        y = 2
                # _ _ *
                # _ _ X
                # _ _ X                
                elif(mapVal[1][2] == "X" and mapVal[2][2] == "X"  and mapVal[0][2] == "_"):
                        print("for the win!")
                        x = 0
                        y = 2
        


                # X _ _
                # _ X _
                # _ _ *                
                elif(mapVal[0][0] == "X" and mapVal[1][1] == "X"  and mapVal[2][2] == "_"):
                        print("for the win!")
                        x = 2
                        y = 2
                # X _ _
                # _ * _
                # _ _ X              
                elif(mapVal[0][0] == "X" and mapVal[2][2] == "X"  and mapVal[1][1] == "_"):
                        print("for the win!")
                        x = 1
                        y = 1
                # * _ _
                # _ X _
                # _ _ X               
                elif(mapVal[1][1] == "X" and mapVal[2][2] == "X"  and mapVal[0][0] == "_"):
                        print("for the win!")
                        x = 0
                        y = 0
        else:
                ########
                # FOR O 
                ########

                # O O *
                # _ _ _
                # _ _ _
                if(mapVal[0][0] == "O" and mapVal[0][1] == "O"  and mapVal[0][2] == "_"):
                        print("for the win!")
                        x = 0
                        y = 2
                # O * O
                # _ _ _
                # _ _ _                
                elif(mapVal[0][0] == "O" and mapVal[0][2] == "O"  and mapVal[0][1] == "_"):
                        print("for the win!")
                        x = 0
                        y = 1
                # * O O
                # _ _ _
                # _ _ _                
                elif(mapVal[0][1] == "O" and mapVal[0][2] == "O"  and mapVal[0][0] == "_"):
                        print("for the win!")
                        x = 0
                        y = 0


                # _ _ _
                # O O *
                # _ _ _
                if(mapVal[1][0] == "O" and mapVal[1][1] == "O"  and mapVal[1][2] == "_"):
                        print("for the win!")
                        x = 1
                        y = 2
                # _ _ _
                # O * O
                # _ _ _                
                elif(mapVal[1][0] == "O" and mapVal[1][2] == "O"  and mapVal[1][1] == "_"):
                        print("for the win!")
                        x = 1
                        y = 1
                # _ _ _
                # * O O
                # _ _ _                
                elif(mapVal[1][1] == "O" and mapVal[1][2] == "O"  and mapVal[1][0] == "_"):
                        print("for the win!")
                        x = 1
                        y = 0


                # _ _ _
                # _ _ _
                # O O *
                elif(mapVal[2][0] == "O" and mapVal[2][1] == "O"  and mapVal[2][2] == "_"):
                        print("for the win!")
                        x = 2
                        y = 2
                # _ _ _
                # _ _ _
                # O * O               
                elif(mapVal[2][0] == "O" and mapVal[2][2] == "O"  and mapVal[2][1] == "_"):
                        print("for the win!")
                        x = 2
                        y = 1
                # _ _ _
                # _ _ _
                # * O O              
                elif(mapVal[2][1] == "O" and mapVal[2][2] == "O"  and mapVal[2][0] == "_"):
                        print("for the win!")
                        x = 2
                        y = 0



                # O _ _
                # O _ _
                # * _ _                
                elif(mapVal[0][0] == "O" and mapVal[1][0] == "O"  and mapVal[2][0] == "_"):
                        print("for the win!")
                        x = 2
                        y = 0
                # O _ _
                # * _ _
                # O _ _                
                elif(mapVal[0][0] == "O" and mapVal[2][0] == "O"  and mapVal[1][0] == "_"):
                        print("for the win!")
                        x = 1
                        y = 0
                # * _ _
                # O _ _
                # O _ _                
                elif(mapVal[1][0] == "O" and mapVal[2][0] == "O"  and mapVal[0][0] == "_"):
                        print("for the win!")
                        x = 0
                        y = 0


                # _ O _
                # _ O _
                # _ * _                
                elif(mapVal[0][1] == "O" and mapVal[1][1] == "O"  and mapVal[2][1] == "_"):
                        print("for the win!")
                        x = 2
                        y = 1
                # _ O _
                # _ * _
                # _ O _                
                elif(mapVal[0][1] == "O" and mapVal[1][2] == "O"  and mapVal[1][1] == "_"):
                        print("for the win!")
                        x = 1
                        y = 1
                # _ * _
                # _ O _
                # _ O _                
                elif(mapVal[1][1] == "O" and mapVal[2][1] == "O"  and mapVal[0][1] == "_"):
                        print("for the win!")
                        x = 0
                        y = 1
                

                # _ _ O
                # _ _ O
                # _ _ *                
                elif(mapVal[0][2] == "O" and mapVal[1][2] == "O"  and mapVal[2][2] == "_"):
                        print("for the win!")
                        x = 2
                        y = 2
                # _ _ O
                # _ _ *
                # _ _ O              
                elif(mapVal[0][2] == "O" and mapVal[2][2] == "O"  and mapVal[1][2] == "_"):
                        print("for the win!")
                        x = 1
                        y = 2
                # _ _ *
                # _ _ O
                # _ _ O   
                elif(mapVal[1][2] == "O" and mapVal[2][2] == "O"  and mapVal[0][2] == "_"):
                        print("for the win!")
                        x = 0
                        y = 2
        


                # O _ _
                # _ O _
                # _ _ *                
                elif(mapVal[0][0] == "O" and mapVal[1][1] == "O"  and mapVal[2][2] == "_"):
                        print("for the win!")
                        x = 2
                        y = 2
                # O _ _
                # _ * _
                # _ _ O             
                elif(mapVal[0][0] == "O" and mapVal[2][2] == "O"  and mapVal[1][1] == "_"):
                        print("for the win!")
                        x = 1
                        y = 1
                # * _ _
                # _ O _
                # _ _ O               
                elif(mapVal[1][1] == "O" and mapVal[2][2] == "O"  and mapVal[0][0] == "_"):
                        print("for the win!")
                        x = 0
                        y = 0        
        return x,y 

def printMaze(maze):
#     print("/////////////////////////////////////////")
    for m in maze:
        print (*m, sep=" ")
    print("/////////////////////////////////////////")