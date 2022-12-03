#half a string the check for the same upper/lowercase letter in both
# a-z have proitorities 1-26
# A-Z have 27-52
# sum all up at the end

def run(openFile):
    for line in openFile:
        line = line.strip("\n")
        length = len(line)
        lineList = [line[:length//2],line[length//2:]]
        print(lineList)