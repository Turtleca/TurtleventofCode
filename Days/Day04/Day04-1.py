EMPTY = ''
def run(OpenFile):
    elfPairs = []
    totalUselsess = 0
    for line in OpenFile:
        line = line.split(" ")
        line = line[0].strip("\n.")
        if line != EMPTY:
            elfPairs.append(line) #parse then append the stripped strings for comparison
        if len(elfPairs) == 2:
            # check which of the strings encomases the other
            if elfPairs[0][0] <= elfPairs[1][0] and elfPairs[0][len(elfPairs[0])-1] >= elfPairs[1][len(elfPairs[1])-1]:
                totalUselsess += 1
            elif elfPairs[0][0] >= elfPairs[1][0] and elfPairs[0][len(elfPairs[0])-1] <= elfPairs[1][len(elfPairs[1])-1]:
                totalUselsess += 1
            elfPairs = []

    print(totalUselsess)