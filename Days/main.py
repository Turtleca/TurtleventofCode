# Main file for AoC For Turtle.ca
# gets date and runs the current day's challenge file with it's input
import sys

import datetime

#readInput()
# Takes the day to append to the input file
def readInput(day):
    fileName = "./inputs/day{:>02}-1.txt".format(str(day))
    openFile = open(fileName, "r")
    return(openFile)
#returns the python read file to be for looped through

#Checks how many arguments were given when running the program
# If there is only 1 just uses the current date to append the day
# If 2 uses that argument as the Day counter
if len(sys.argv) == 1:
  day = datetime.datetime.now().day
elif len(sys.argv) == 2:
  day = int(sys.argv[1])
else:
  print(f"Wrong number of arguments, expected 0 or 1 arguments (optional day override), got {len(sys.argv)-1}")
  exit(1)

# Written by Sekoia 
# appends the system path to properly look at all possible files that could be read
sys.path.insert(0, ".\Day{:>02}".format(str(day)))

# Import the first part of the day's advent challenge as "run()"
# imputs the read file of the day as the only argument
part1 = __import__("Day{:>02}-1".format(str(day)))
part1.run(readInput(day))

#Same as above except assumes part 2 is available
#part2 = __import__("Day{:>02}-2".format(str(day)))
#part2.run(readInput(day))
