import random
import numpy as np
def randomizeCases(l):
    caseValues = l
    np.random.shuffle(caseValues)
    return caseValues

firstcase = 0
def getFirstCase(l):
    global firstcase
    case = int(input("Pick a case. You keep this one until the end. "))
    firstcase = l[case-1]
    l[case-1] = None
    return l

def removeCase(l):
    case = int(input("Pick a case to remove: "))
    print(l[case-1])
    while case < 1 or case > 26:
        case = int(input("Not between 1 and 26. Pick a case to remove: "))
    while l[case-1] == None:
        case = int(input("You already picked that one. Pick a case to remove: "))
    print("You just removed the case with %", l[case-1], "in it")
    l[case-1] = None
    print("Cases Left: ", casesLeft(l))
    return l

def getEX(l):
    sum = 0
    numCases = 0
    for i in range(len(l)):
        if l[i] != None:
            sum += l[i]
            numCases += 1
    expectedValue = round((sum/numCases),2)
    return expectedValue
    
def getOffer(l,r):
    offer = getEX(l)
    if r == 1:
        return round(offer*(.106804),2)
    elif r == 2:
        return round(offer*(.215985),2)
    elif r == 3:
        return round(offer*(.373357),2)
    elif r == 4:
        return round(offer*(.518857),2)
    elif r == 5:
        return round(offer*(.630936),2)
    elif r == 6:
        return round(offer*(.737169),2)
    elif r == 7:
        return round(offer*(.871227),2)
    elif r == 8:
        return round(offer*(.91328),2)
    return offer

def compareOffer(l,r):
    offer = getOffer(l,r)
    moreThanOffer = 0
    numInList = 0
    for i in range(len(l)):
        if l[i] != None and l[i] > offer:
            moreThanOffer += 1
        if l[i] != None:
            numInList += 1
    prob = (moreThanOffer/numInList) * 100
    prob = round(prob,2)
    print("There are ", moreThanOffer, "cases out of ", numInList, "greater than the offer of $", offer)
    print("So, there is a ", prob, "% chance of getting more than this offer")
    

def printMaxMoney(l):
    max = 0
    casesLeft = 0
    for i in range(len(l)):
        if l[i] != None and l[i]>max:
            max = l[i]
        if l[i] != None:
            casesLeft += 1
    prob = (1/casesLeft) * 100
    prob = round(prob,2)
    print("The Most Money You Can Make Is: ", max)
    print("You Have a ", prob, "% chance of Winning the Max Amount")

def takeOrDont(l):
    print("Deal or No Deal?")
    answer = str(input())
    if answer == "Deal":
        print("Congrats, you just won $", getOffer(l))
        return 0
    elif answer == "No Deal":
        print("Lets keep going")
        return 1
    else:
        print("Please enter the phrase 'Deal' or 'No Deal'")
        takeOrDont(l)
    
def findRemainingCases(l):
    count = 0
    for i in range(len(l)):
        if l[i] != None:
            count += 1
    return count

def getLastCase(l):
    count = 0
    for i in range(len(l)):
        if l[i] != None:
            return l[i]

def switch(l):
    answer = str(input("Do you want to switch? "))
    if answer == "Yes":
        print("You just won: $", getLastCase(l))
    elif answer == "No":
        print("You just won: $", firstcase)
    else:
        print("Please enter the phrase 'Yes' or 'No'")
        switch(l)

def casesLeft(l):
    newl = []
    for i in range(len(l)):
        if l[i] != None:
            newl.append(i+1)
    return newl

def simulate(l,verb):
    getFirstCase(l)
    round = 1
    while verb>1:
        for i in range(0,verb):
            removeCase(l)
            printMaxMoney(l)
        getOffer(l,round)
        compareOffer(l,round)
        round += 1
        deal = takeOrDont(l)
        if deal == 0:
            exit(0)
        print("ROUND",round)
        verb -= 1
    numCasesLeft = findRemainingCases(l)
    while numCasesLeft != 2:
        removeCase(l)
        printMaxMoney(l)
        getOffer(l,round)
        compareOffer(l,round)
        round += 1
        deal = takeOrDont(l)
        if deal == 0:
            exit(0)
        print("ROUND",round)
        numCasesLeft = findRemainingCases(l)
    print("We now know that the last two values are $", firstcase, "and $",getLastCase(l))
    print("The question is... Which one is in your case?")
    print("If you want you can switch. If you switch you open the last case on the stage")
    print("If you don't switch, you win whatever is in the case you picked in the beginning.")
    switch(l)


if __name__ == "__main__":
    caseValues = [0.01,1,5,10,25,50,75,100,200,300,400,500,750,1000,5000,10000,25000,50000,75000,100000,200000,300000,400000,500000,750000,1000000]
    caseOrder = randomizeCases(caseValues)
    verbose = 6
    simulate(caseOrder,verbose)
    

