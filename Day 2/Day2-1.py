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

def RPS():
    filename = "./inputs/day2-1.txt"
    openFile = open(filename, "r")
    totalScore = 0
    for line in openFile:
        currentMove = ord(line[0]) - 64
        opponentMove = ord(line[2]) - 87
        print(currentMove, opponentMove)
        if currentMove == ROCK:
            totalScore += ROCK
            if opponentMove == ROCK:
                totalScore += DRAW
                print("+1 +3")
            elif opponentMove == PAPER:
                totalScore += LOSS
                print("+1 +0")
            elif opponentMove == SCISSORS:
                totalScore += WIN
                print("+1 +6")
        if currentMove == PAPER:
            totalScore += PAPER
            if opponentMove == ROCK:
                totalScore += WIN
                print("+2 +6")
            elif opponentMove == PAPER:
                totalScore += DRAW
                print("+2 +3")
            elif opponentMove == SCISSORS:
                totalScore += LOSS
                print("+2 +0")
        if currentMove == SCISSORS:
            totalScore += SCISSORS
            if opponentMove == ROCK:
                totalScore += LOSS
                print("+3 + 0")
            elif opponentMove == PAPER:
                totalScore += WIN
                print("+3 + 6")
            elif opponentMove == SCISSORS:
                totalScore += DRAW
                print("+3 + 3")
        

    print(totalScore)

        
        

RPS()