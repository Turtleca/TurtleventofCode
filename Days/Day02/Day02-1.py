# WIN AT ROCK PAPER SCISSORS

#Point scores are
# 1 for Rock A X
# 2 for paper B Y
# 3 for scissors C Z

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

def run(openFile):
    totalScore = 0
    for line in openFile:
        roundScore = 0
        opponentMove = ord(line[0]) - 64
        currentMove = ord(line[2]) - 87
        if beatenBy[opponentMove-1] == currentMove: #WIN
            roundScore = WIN + currentMove
        elif beats[opponentMove-1] == currentMove: #loos 
            roundScore = LOSS + currentMove
        else: 
            roundScore = DRAW + currentMove
        totalScore += roundScore
    openFile.close()
    print(totalScore)