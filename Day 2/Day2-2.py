# WIN AT ROCK PAPER SCISSORS

#Point scores are
# 1 for Rock A 
# 2 for paper B 
# 3 for scissors C 

# X Loss
# Y Draw
# Z Win

# 0 for loss 
# 3 for draw
# 6 for win
ROCK = 1
PAPER = 2
SCISSORS = 3
LOSS = 0
DRAW = 3
WIN = 6
NEWLINE = "\n"
SPACE = " "

beatenBy = [PAPER, SCISSORS, ROCK]
beats = [SCISSORS, ROCK, PAPER]

def RPS():
    filename = "./inputs/day2-1.txt"
    openFile = open(filename, "r")
    totalScore = 0
    for line in openFile:
        roundScore = 0
        currentMove = ord(line[2]) - 87
        opponentMove = ord(line[0]) - 64
        print(currentMove, opponentMove)
        if beatenBy[opponentMove-1] == currentMove: #WIN
            roundScore = WIN + currentMove
        elif beats[opponentMove-1] == currentMove: #loos 
            roundScore = LOSS + currentMove
        else: 
            roundScore = DRAW + currentMove
        totalScore += roundScore
    print(totalScore)
    openFile.close()

RPS()