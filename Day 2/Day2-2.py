# WIN AT ROCK PAPER SCISSORS

#Point scores are
# 1 for Rock A 
# 2 for paper B 
# 3 for scissors C 

# X Loss 1
# Y Draw 2
# Z Win 3

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

normalGame = [ROCK, PAPER, SCISSORS]
beatenBy = [PAPER, SCISSORS, ROCK]
beats = [SCISSORS, ROCK, PAPER]

def RPS():
    filename = "./inputs/day2-1.txt"
    openFile = open(filename, "r")
    totalScore = 0
    for line in openFile:
        roundScore = 0
        opponentMove = ord(line[0]) - 64
        gameState = ord(line[2]) - 87
        myMove = 0
        if (WIN/3)+1 == gameState: #WIN
            roundScore = WIN + beatenBy[opponentMove-1]
        elif (LOSS/3)+1 == gameState: #LOSS
            roundScore = LOSS + beats[opponentMove-1]
        else: # DRAW
            roundScore = DRAW + opponentMove
        totalScore += roundScore
    print(totalScore)
    openFile.close()

RPS()