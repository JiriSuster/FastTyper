import json
import logging as log
import random
import time

START_TIME = time.time()

def getWords(ammount, level):
    if level == 1:
        pathToFile = "funcCommon/words/wordsLVL1.json"
    
    elif level == 2:
        pathToFile = "funcCommon/words/wordsLVL2.json"
    
    elif level == 3:
        pathToFile = "funcCommon/words/wordsLVL2.json"
    
    elif level == 4:
        pathToFile = "funcCommon/words/wordsLVL4.json"
    
    else:
        log.debug("you picked wrong level, selecting 1")
        level = 1
        pathToFile = "funcCommon/words/wordsLVL1.json"
    
    
    with open(pathToFile, 'r') as file:
        wordsJSON = json.load(file)
        words = wordsJSON["words"]
        outputText = ""
        for i in range(ammount):
            randomWord = random.choice(words)
            outputText += randomWord + " "
        return outputText[:-1]
    

def timerStart():
    global START_TIME
    START_TIME = time.time()




def timerStop():
    global START_TIME
    return time.time() - START_TIME

def rawWpmCounter(allcharAmount, timeInSeconds):
    return round((allcharAmount / 5) / (timeInSeconds / 60))

def wpmCounter(allcharAmount, errors, timeInSeconds):
    return rawWpmCounter(allcharAmount-errors, timeInSeconds)

#return correct percent accuracy
def accuracyCounter(allcharAmount, errors):
    return round((allcharAmount - errors) / (allcharAmount / 100))
