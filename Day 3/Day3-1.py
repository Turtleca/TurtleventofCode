import sys
sys.path.append("./Modules")

from readFile import readInput

aFile = readInput(2)

for line in aFile:
    print(line, end="")
aFile.close