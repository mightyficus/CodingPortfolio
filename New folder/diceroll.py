#diceroll.py
"""
Diceroll.py
Author: John Cooper Hopkin
22 November 2018
A script to roll groups of dice and determine the individual group total
and full total
"""
import sys
import re
import random

def test(teststr):


    if re.search("^([\d]+)g([\d]+)d([\d]+)$", teststr, re.IGNORECASE):
        regex = re.search("^([\d]+)g([\d]+)d([\d]+)$", teststr, re.IGNORECASE)
        print(regex)
        print()
        #print(regex[0])
        print(regex[1])
        print(regex[2])
        print(regex[3])
    elif re.search("([\d]+)g ([\d]+)d ([\d]+)", teststr, re.IGNORECASE):
        regex = re.search("([\d]+)g ([\d]+)d ([\d]+)", teststr, re.IGNORECASE)
        print(regex)
        print()
        #print(regex[0])
        print(regex[1])
        print(regex[2])
        print(regex[3])
    else:
        print("Input not valid.")



#test("1g10d20")

def isvalid(inString):
    if re.search("^([\d]+)g([\d]+)d([\d]+)$", inString, re.IGNORECASE):
        return True
    elif re.search("([\d]+)g ([\d]+)d ([\d]+)", inString, re.IGNORECASE):
        return True
    else:
        print("Input not valid.")
        return False

def groups(inString):
    if re.search("^([\d]+)g([\d]+)d([\d]+)$", inString, re.IGNORECASE):
        regex = re.search("^([\d]+)g([\d]+)d([\d]+)$", inString, re.IGNORECASE)
        return int(regex[1]), int(regex[2]), int(regex[3])
    elif re.search("([\d]+)g ([\d]+)d ([\d]+)", inString, re.IGNORECASE):
        regex = re.search("([\d]+)g ([\d]+)d ([\d]+)", inString, re.IGNORECASE)
        return int(regex[1]), int(regex[2]), int(regex[3])


def totalRoll(groups, number, die):
    #TODO Implement rolling function (print to console)
    #input("Inside the totalRoll func")
    groupTotals = []

    for i in range(groups):

        total = 0
        for j in range(number):
            total += random.randrange(1,die+1)
        groupTotals.append(total)


    #print out list of group totals, then total
    print("Group totals: ",end='')
    for i in range(len(groupTotals)-1):
        print(groupTotals[i], end=", ")
    print(groupTotals[-1])

    print()
    print("Final Total:", sum(groupTotals))


def manualInput():
    #TODO: Implement manual Input mode (0 to exit)
    try:
        while(True):
            #number of groups
            groups = int(input("Enter the number of dice groups: "))
            if (groups == 0):
                return 1
            elif (groups < 0):
                raise Exeption("You can't have a negative group number!")

            #number of dice
            number = int(input("Enter the number of dice to roll: "))
            if (number < 1):
                raise Exeption("You can't roll less than 1 die!")

            #type of die
            die = int(input("Enter the type of die: "))
            if (die < 2):
                raise Exeption("You can't have a die with less than two sides!")

            #roll the dice
            totalRoll(groups, number, die)
            input("In the input section")

    except:
        print("Invalid Input!")
        print("Try again, or enter 0 to exit...")

def commandArgs():
    try:
        if isvalid(sys.argv[1]):
            totalRoll(groups(sys.argv[1]))
            return 1
        else:
            print("Invalid Arguments, please enter manually...")
    except:
        print("Invalid Arguments, please enter manually...")
        return manualInput()



if __name__ == "__main__":
    if len(sys.argv) > 1:
        commandArgs()
    else:
        manualInput()

    input("Press any key to exit...")
