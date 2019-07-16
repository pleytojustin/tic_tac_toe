from random import seed
from random import randint
from level_zero import *
from level_one import *
from level_two import *
def initializeMap(size):

    initMap = [['_' for x in range(size)] for y in range(size)]     

    return initMap
def printMaze(map):
    for m in map:
        print (*m, sep=" ")
if __name__ == "__main__":
    initMap = initializeMap(3)

    # TEST CASE WIN LEFT TO RIGHT

    # initMap[0][0] = "O"
    # initMap[0][1] = "X"
    # initMap[0][2] = "O"

    # initMap[1][0] = "O"
    # initMap[1][1] = "X"
    # initMap[1][2] = "X"

    # initMap[2][0] = "X"
    # initMap[2][1] = "O"
    # initMap[2][2] = "O"

    printMaze(initMap)

    move = Engine()
    start = input("Who starts first? 1 - person or 2 - bot: ")
    if(start == "1"):
        print("PERSON STARTS FIRST")
        move.X = "PERSON"
        move.O = "BOT"
    else:
        print("BOT STARTS FIRST")
        move.X = "BOT"
        move.O = "PERSON"  

    #LEVEL 0
    # levelZero(initMap, move)

    #LEVEL 1
    #levelOne(initMap, move)

    #LEVEL 2
    levelTwo(initMap, move)