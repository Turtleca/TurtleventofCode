# WIN AT ROCK PAPER SCISSORS

#Point scores are
# 1 for Rock A X
# 2 for paper B Y
# 3 for scissors C Z

# 0 for loss 
# 3 for draw
# 6 for win

NEWLINE = "\n"
SPACE = " "

def RPS():
    filename = "C:/Users/sleep/OneDrive/Documents/PythonPrograms/ADventofCode/inputs/day2-1.txt"
    openFile = open(filename, "r")

    totalScore = 0
    LOSS = 0
    DRAW = 3
    WIN = 6
    ROCK = "A","X"
    PAPER = "B","Y"
    SCISSORS = "C","Z"

    for line in openFile:
        print(line)
    print(totalScore)

        
        

RPS()