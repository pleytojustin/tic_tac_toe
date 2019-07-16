class Engine():
    X = ""
    O = ""
    moveNow = "X"
    def checkIfDraw(self, mapVal):
        for row in mapVal:
            for m in row:
                if(m == "_"):
                    return False
        print("DRAW")
        return True

    def addO(self,mapVal,x,y):
        mapVal[int(x)][int(y)] = "O"
        return mapVal
    def addX(self,mapVal,x,y):
        mapVal[int(x)][int(y)] = "X"
        return mapVal
    def checkMapIfWin(self, mapVal):
        didWin = False
        whoWon = ""
        for m in mapVal:
            if( (m[0] == "X" and m[1] == "X" and m[2] == "X")):
                didWin = True
                whoWon = "X"
            if (m[0] == "O" and m[1] == "O" and m[2] == "O"):
                didWin = True
                whoWon = "O"

        for i in range(0, 3):
            if( (mapVal[0][i] == "X" and mapVal[1][i] == "X" and mapVal[2][i] == "X")):
                didWin = True
                whoWon = "X"           
            if((mapVal[0][i] == "O" and mapVal[1][i] == "O" and mapVal[2][i] == "O")):
                didWin = True 
                whoWon = "O"
        if(mapVal[0][0] == "X" and mapVal[1][1] == "X" and mapVal[2][2] == "X"):
                didWin = True 
                whoWon = "X"       
        if(mapVal[0][0] == "O" and mapVal[1][1] == "O" and mapVal[2][2] == "O"):
                didWin = True 
                whoWon = "O"    
        if(mapVal[0][2] == "X" and mapVal[1][1] == "X" and mapVal[2][0] == "X"):
                didWin = True 
                whoWon = "X"       
        if(mapVal[0][2] == "O" and mapVal[1][1] == "O" and mapVal[2][0] == "O"):
                didWin = True 
                whoWon = "O"   
        if(didWin == True and whoWon == "O"):
            print("O Won")
        if(didWin == True and whoWon == "X"):
            print("X Won")

        return didWin

    def inputXYValid(self, mapVal, x, y):
        if(mapVal[int(x)][int(y)] != "_"):
            return False
        return True
