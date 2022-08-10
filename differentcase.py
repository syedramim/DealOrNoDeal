import random
import numpy as np
import math

def randomizeCases(l):
    caseValues = l
    np.random.shuffle(caseValues)
    return caseValues

def removeCases(l):
    newl = l
    for i in range(24):
        case = random.randint(0,25)
        while newl[case-1] == None:
            case = random.randint(1,25)
        newl[case-1] = None
    return newl

def getNewL(l):
    newl = []
    temp = l
    oldl = removeCases(temp)
    for i in range(len(oldl)):
        if oldl[i] != None:
            newl.append(oldl[i])
    return newl

def monteHall(l):
    print("An exact one in 26 chance is 0.038462")
    for j in range(26):
        trials = 20000
        score = 0
        orig = l
        for i in range(trials):
            orig = [0.01,1,5,10,25,50,75,100,200,300,400,500,750,1000,5000,10000,25000,50000,75000,100000,200000,300000,400000,500000,750000,1000000]
            randomOrder = randomizeCases(orig)
            mycase = randomOrder[j]
            if mycase == 1000000:
                score += 1
            
        print("If you always pick case ", j+1, " to start, the probability of your case having 1 million in it is ", score/trials)
    return 0

if __name__ == "__main__":
    caseValues = [0.01,1,5,10,25,50,75,100,200,300,400,500,750,1000,5000,10000,25000,50000,75000,100000,200000,300000,400000,500000,750000,1000000]
    monteHall(caseValues)



