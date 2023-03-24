from js import document
from pyodide import create_proxy
import random
import time

import funcTimeMode.timeFunc
import funcCommon.commonFunc

DISPLAY_TEXT = document.getElementById("txt")
OLD_INPUT_TEXT = ""
DATA = ""
DEFAULT_TIME = 60
TIME = 60
CURSOR_INDEX = 0
listOfWords = ["from", "add", "call", "another"]

def setTime(seconds):
    global TIME, DEFAULT_TIME
    DEFAULT_TIME = seconds
    TIME = seconds
    document.getElementById("time").innerHTML = TIME

def setText():
    global DATA
    DATA = getRandomText(25)
    displayText()

def getRandomText(wordsAmount):
    text = ''
    for i in range(wordsAmount-1):
        text += random.choice(listOfWords) + " "
    text += random.choice(listOfWords)
    return text
def checkShortcuts(event):
    if event.keyCode == 27:
        setTime(DEFAULT_TIME)
        setText()

def displayText():
    DISPLAY_TEXT.innerHTML = ""
    for character in DATA:
        characterSpan = document.createElement("span")
        characterSpan.innerHTML = character
        DISPLAY_TEXT.appendChild(characterSpan)

def changeText(input_value):
    array_text = DISPLAY_TEXT.querySelectorAll('span')


    input_text = OLD_INPUT_TEXT + input_value
    user_list_input = [char for char in input_text]

    for index, element in enumerate(array_text):
        if len(user_list_input) <= index:
            element.classList.remove("correct")
            element.classList.remove("wrong")
        else:
            user_character = user_list_input[index]
            if element.innerText == user_character:
                element.classList.remove("wrong")
                element.classList.add("correct")
            elif element.innerText != user_character:
                element.classList.add("wrong")
                element.classList.remove("correct")


def inputEvent(event):
    global OLD_INPUT_TEXT, CURSOR_INDEX
    value = event.target.value
    if len(value) > len(DATA.split(" ")[CURSOR_INDEX]):
        event.target.value = value[:len(DATA.split(" ")[CURSOR_INDEX])]
    changeText(value)
    if " " in str(value):
        OLD_INPUT_TEXT += value
        CURSOR_INDEX += 1
        event.target.value = ""

def setup():
    setText()
    setTime(TIME)

    click_proxy = create_proxy(inputEvent)
    click = document.getElementById("text_input")
    click.addEventListener("input", click_proxy)

    check_proxy = create_proxy(checkShortcuts)
    document.addEventListener("keydown", check_proxy)

def main():
    setup()

if __name__ == "__main__":
    main()
