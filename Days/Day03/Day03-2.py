#half a string the check for the same upper/lowercase letter in both
# a-z have proitorities 1-26
# A-Z have 27-52
# sum all up at the end

# part 2 compare every 3 lines
#TODO be able to run more than one line or at least remember every 3
# try the append case and check if the lenght of the list is == 6
#wait I dont gotta check every line individually

def run(openFile):
    totalScore = 0
    sackList = []
    for line in openFile:
        #remove the newline character
        line = line.strip("\n")
        #append current list to the group
        sackList.append(line)

        #Now to check for the same character in a string
        if (len(sackList) == 3):
            #print(f"appended {sackList}") #debug

            #Check ALL THE CHARACTERS
            lineChecked = False
            for char1 in sackList[0]:
                for char2 in sackList[1]:
                    for char3 in sackList[2]:
                        if (char1 == char2 == char3) and lineChecked == False:
                            if ord(char1) < 97:
                                totalScore += (ord(char1) - 38)
                            else:
                                totalScore += (ord(char1) - 96)
                            lineChecked = True
            sackList = []
    openFile.close()
    print(f"the total score for part 2 is {totalScore}")