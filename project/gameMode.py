from js import document
from pyodide import create_proxy
import random
import time
import funcGameMode.gameFunc as game
import funcCommon.commonFunc as common

WRONG = False
DATA = ""
DISPLAY_TEXT = document.getElementById("txt")
WRITTEN_TEXT = ""
DATA = ""
FIRST_TIME = True
CURSOR_INDEX = 0
MISTAKES = 0
START_TIME = 0
TOTAL_WORD_COUNT = 0
LAST_WRONG_COUNT = 0


def setText(ammount=2, difficulty=1):

    global DATA,TOTAL_WORD_COUNT
    TOTAL_WORD_COUNT = ammount
    DATA = common.getWords(ammount, difficulty)
    displayText()

def displayText():
    DISPLAY_TEXT.innerHTML = ""
    for character in DATA:
        characterSpan = document.createElement("span")
        characterSpan.innerHTML = character
        DISPLAY_TEXT.appendChild(characterSpan)

def checkShortcuts(event):
    if event.keyCode == 27:
        resetGame()



def TextCorrection(input_value):
    global WRONG,MISTAKES,CURSOR_INDEX,TOTAL_WORD_COUNT,LAST_WRONG_COUNT
    wrongCount = 0
    array_text = DISPLAY_TEXT.querySelectorAll('span')

    input_text = WRITTEN_TEXT + input_value
    user_list_input = [char for char in input_text]

    for index, element in enumerate(array_text):
        if len(user_list_input) <= index:
            element.classList.remove("correct")
            element.classList.remove("wrong")
        else:
            user_character = user_list_input[index]
            if element.innerText == user_character and wrongCount == 0:
                element.classList.remove("wrong")
                element.classList.add("correct")
            elif element.innerText != user_character or wrongCount > 0:
                element.classList.add("wrong")
                element.classList.remove("correct")
                wrongCount+=1

    if wrongCount > LAST_WRONG_COUNT:
        MISTAKES+=1

    LAST_WRONG_COUNT = wrongCount
    print(wrongCount)
    print("m",MISTAKES)
    if wrongCount > 0:
        WRONG = True
    else:
        WRONG = False


def inputEvent(event):
    global WRITTEN_TEXT, CURSOR_INDEX, FIRST_TIME, INTERVAL, WRONG,MISTAKES
    if FIRST_TIME:
        common.timerStart()
        FIRST_TIME = False
    value = event.target.value
    if len(value) > len(DATA.split(" ")[CURSOR_INDEX]):
        event.target.value = value[:len(DATA.split(" ")[CURSOR_INDEX])]
    TextCorrection(value)
    if " " in str(value) and not WRONG:
        if len(value.replace(" ", "")) < len(DATA.split(" ")[CURSOR_INDEX]):
            value = value.replace(" ", "")
            value += "*" * (len(DATA.split(" ")[CURSOR_INDEX]) - len(value))
            TextCorrection(value)
            CURSOR_INDEX += 1
            event.target.value = ""
            WRITTEN_TEXT += value + " "
        else:
            CURSOR_INDEX += 1
            event.target.value = ""
            WRITTEN_TEXT += value
        anotherTextWords()

def anotherTextWords():
    global CURSOR_INDEX, WRITTEN_TEXT, FIRST_TIME, MISTAKES
    if CURSOR_INDEX == TOTAL_WORD_COUNT:
        print("Zabralo ti to:", common.timerStop(), "sekund. Udělal jsi", MISTAKES, "chyb.")
        FIRST_TIME = True
        MISTAKES = 0
        CURSOR_INDEX = 0
        WRITTEN_TEXT = ""
        setText()

def resetGame():
    global CURSOR_INDEX, WRITTEN_TEXT, FIRST_TIME
    FIRST_TIME = True
    CURSOR_INDEX = 0
    WRITTEN_TEXT = ""
    document.getElementById("text_input").value = ""
    setText()


def setup():
    setText()
    click_proxy = create_proxy(inputEvent)
    click = document.getElementById("text_input")
    click.addEventListener("input", click_proxy)

    check_proxy = create_proxy(checkShortcuts)
    document.addEventListener("keydown", check_proxy)

def main():
    setup()

if __name__ == "__main__":
    main()
