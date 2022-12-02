#create a code that adds up sequences of numbers separated by newlines

NEWLINE = "\n"

def day1(openfile):
    elfCount = 0
    bestElf = 0
    elfTotal = 0
    calorieMax = 0

    for line in openfile:
        
        if line != NEWLINE:
            elfTotal += int(line)
        else:
            elfCount += 1
            if calorieMax < elfTotal:
                calorieMax = elfTotal
                bestElf = elfCount
            elfTotal = 0
    openfile.close
    print("Best elf is %s with a count of %s calories" %(bestElf,calorieMax))