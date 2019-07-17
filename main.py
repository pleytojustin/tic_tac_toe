from random import seed
from random import randint
from level_zero import *
from level_one import *
from level_two import *
def whoStarts(move):
    start = input("Who starts first? 1 - person or 2 - bot: ")
    if(start == "1"):
        print("PERSON STARTS FIRST")
        move.X = "PERSON"
        move.O = "BOT"
    else:
        print("BOT STARTS FIRST")
        move.X = "BOT"
        move.O = "PERSON"
    return move
def initializeMap(size):

    initMap = [['_' for x in range(size)] for y in range(size)]     

    return initMap
def printMaze(map):
    for m in map:
        print (*m, sep=" ")
if __name__ == "__main__":
    initMap = initializeMap(3)
    printMaze(initMap)

    move = Engine()

    level = input("Select a level 0, 1, 2: ")
    if level == "0":
        move = whoStarts(move)
        levelZero(initMap, move)
    elif level == "1":
        move = whoStarts(move)
        levelOne(initMap, move)
    elif level == "2":
        move = whoStarts(move)
        levelTwo(initMap, move)

    # move = whoStarts(move)
    # #LEVEL 0
    # # levelZero(initMap, move)

    # #LEVEL 1
    # #levelOne(initMap, move)

    # #LEVEL 2
    # levelTwo(initMap, move)   
