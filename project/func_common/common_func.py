import json
import logging as log
import random
import time

START_TIME = time.time()


def get_words(amount, level):
    if level == 1:
        path_to_file = "func_common/words/wordsLVL1.json"
    
    elif level == 2:
        path_to_file = "func_common/words/wordsLVL2.json"
    
    elif level == 3:
        path_to_file = "func_common/words/wordsLVL2.json"
    
    elif level == 4:
        path_to_file = "func_common/words/wordsLVL4.json"
    
    else:
        log.debug("you picked wrong level, selecting 1")
        level = 1
        path_to_file = "func_common/words/wordsLVL1.json"

    with open(path_to_file, 'r') as file:
        wordsJSON = json.load(file)
        words = wordsJSON["words"]
        outputText = ""
        for i in range(amount):
            randomWord = random.choice(words)
            outputText += randomWord + " "
        return outputText[:-1]
    

def timer_start():
    global START_TIME
    START_TIME = time.time()




def timer_stop():
    global START_TIME
    return time.time() - START_TIME


def raw_wpm_counter(all_char_amount, time_in_seconds):
    return round((all_char_amount / 5) / (time_in_seconds / 60))


def wpm_counter(all_char_amount, errors, time_in_seconds):
    return raw_wpm_counter(all_char_amount-errors, time_in_seconds)


# return correct percent accuracy
def accuracy_counter(all_char_amount, errors):
    return round((all_char_amount - errors) / (all_char_amount / 100))

