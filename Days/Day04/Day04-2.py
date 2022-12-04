EMPTY = ''
def run(OpenFile):
    totalUselsess = 0
    for line in OpenFile:
        elfPairs = line
        elfPairs = elfPairs.strip("\n")
        elfPairs = elfPairs.split(",")
        elfPairs[0] = elfPairs[0].split("-")
        elfPairs[1] = elfPairs[1].split("-") #parse then append the stripped strings for comparison
        # check which of the strings overlapps at all with the other
        if (int(elfPairs[1][0]) <= int(elfPairs[0][0]) <= int(elfPairs[1][1])) or (int(elfPairs[1][0]) <= int(elfPairs[0][1]) <= int(elfPairs[1][1])):
            totalUselsess += 1
        elif (int(elfPairs[0][0]) <= int(elfPairs[1][0]) <= int(elfPairs[0][1])) or (int(elfPairs[0][0]) <= int(elfPairs[1][1]) <= int(elfPairs[0][1])):
            totalUselsess += 1

    print(f"Total overlapping sweeps are {totalUselsess}")