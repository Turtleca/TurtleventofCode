#half a string the check for the same upper/lowercase letter in both
# a-z have proitorities 1-26
# A-Z have 27-52
# sum all up at the end

def run(openFile):
    totalScore = 0
    for line in openFile:
        #parse the line and split into 2 equal sections
        line = line.strip("\n")
        length = len(line)
        lineList = [line[:length//2],line[length//2:]]
        print(lineList)

        lineChecked = False
        
        #Now to check for the same character in a string
        for char1 in lineList[0]:
            for char2 in lineList[1]:
                if char1 == char2 and lineChecked == False:
                    if ord(char1) < 97:
                        totalScore += (ord(char1) - 38)
                        lineChecked = True

                    else:
                        totalScore += (ord(char1) - 96)
                    lineChecked = True

    print(f"the total score for part 1 is {totalScore}")