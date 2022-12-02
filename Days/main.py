import sys

import datetime

def readInput(day):
    fileName = "./inputs/day{:>02}-1.txt".format(str(day))
    openFile = open(fileName, "r")
    return(openFile)

if len(sys.argv) == 1:
  day = datetime.datetime.now().day
elif len(sys.argv) == 2:
  day = int(sys.argv[1])
else:
  print(f"Wrong number of arguments, expected 0 or 1 arguments (optional day override), got {len(sys.argv)-1}")
  exit(1)

sys.path.insert(0, "./Day{:>02}".format(str(day)))

part1 = __import__("Day{:>02}-1".format(str(day)))
part1.run(readInput(day))

part2 = __import__("Day{:>02}-2".format(str(day)))
part2.run(readInput(day))
