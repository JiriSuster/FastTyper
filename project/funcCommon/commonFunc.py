import json
import logging as log
import random

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
        return outputText
    


