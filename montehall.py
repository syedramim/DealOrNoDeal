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
            case = random.randint(0,25)
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
    trials = num_trials(0.01,0.5)#20000
    score = 0
    orig = l
    for i in range(trials):
        orig = [0.01,1,5,10,25,50,75,100,200,300,400,500,750,1000,5000,10000,25000,50000,75000,100000,200000,300000,400000,500000,750000,1000000]
        randomOrder = randomizeCases(orig)
        newl = getNewL(randomOrder)
        mycase = newl[0]
        othercase = newl[1]
        if mycase > othercase:
            score += 1
    return score/trials

def num_trials(error,prob):
    trials = math.ceil((1/prob) * (.25/pow(error,2)))
    return trials
#print(num_trials(0.01,0.5))

if __name__ == "__main__":
    caseValues = [0.01,1,5,10,25,50,75,100,200,300,400,500,750,1000,5000,10000,25000,50000,75000,100000,200000,300000,400000,500000,750000,1000000]
    print(monteHall(caseValues))



