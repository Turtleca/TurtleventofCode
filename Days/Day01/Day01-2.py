NEWLINE = "\n"

def run(openfile):
    elfCount = 0
    oneElf = 0
    twoElf = 0
    threeElf = 0
    elfTotal = 0
    calorieone = 0
    calorietwo = 0
    caloriethree = 0

    for line in openfile:
        
        if line != NEWLINE:
            elfTotal += int(line)
        else:
            elfCount += 1
            if calorieone < elfTotal:
                caloriethree = calorietwo
                calorietwo = calorieone
                calorieone = elfTotal
                oneElf = elfCount
            elif calorietwo < elfTotal:
                caloriethree = calorietwo
                calorietwo = elfTotal
                twoElf = elfCount
            elif caloriethree < elfTotal:
                caloriethree = elfTotal
                threeElf = elfCount
            elfTotal = 0
    openfile.close()
    calorieTOTAL = calorieone + calorietwo + caloriethree
    print("""Rankings of elves to calories
    1) %s\t%s
    2) %s\t%s
    3) %s\t%s
    
    Total: %s""" %(oneElf,calorieone,twoElf,calorietwo,threeElf,caloriethree,calorieTOTAL))