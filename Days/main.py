from readFile import readInput
from datetime import date
import importlib

dateToday = str(date.today()).split("-")[2]
challengeNum = 1

fileToday = readInput(dateToday)

print("Today is: %s  \nstarting program ./Day %s/Day%s-%s.py " %(dateToday,dateToday,dateToday,challengeNum))

day = importlib.import_module("Day %s.Day%s-%s" %(dateToday,dateToday,challengeNum))
