from js import document, setInterval, clearInterval
from pyodide import create_proxy
import random
import time

import funcTimeMode.timeFunc
import funcCommon.commonFunc

DISPLAY_TEXT = document.getElementById("txt")
DISPLAY_TIME = document.getElementById("time")
INTERVAL = None
WRITTEN_TEXT = ""
DATA = ""
DEFAULT_TIME = 60
TIME = 60
FIRST_TIME = True
CURSOR_INDEX = 0
MISTAKES = 0

def setTime(seconds):
    global TIME, DEFAULT_TIME, DISPLAY_TIME
    DEFAULT_TIME = seconds
    TIME = seconds
    DISPLAY_TIME.innerHTML = TIME

def timer():
    global TIME
    TIME -= 1
    DISPLAY_TIME.innerHTML = TIME

def runInterval():
    global INTERVAL, FIRST_TIME
    if FIRST_TIME:
        proxy = create_proxy(timer)
        INTERVAL = setInterval(proxy, 1000)
        FIRST_TIME = False

def setText():
    global DATA
    DATA = funcCommon.commonFunc.getWords(25, 1)
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
    array_text = DISPLAY_TEXT.querySelectorAll('span')

    input_text = WRITTEN_TEXT + input_value
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
    global WRITTEN_TEXT, CURSOR_INDEX, FIRST_TIME, INTERVAL

    runInterval()
    value = event.target.value
    if len(value) > len(DATA.split(" ")[CURSOR_INDEX]):
        event.target.value = value[:len(DATA.split(" ")[CURSOR_INDEX])]
    TextCorrection(value)
    if " " in str(value):
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
    global CURSOR_INDEX, WRITTEN_TEXT
    if CURSOR_INDEX == 25:
        CURSOR_INDEX = 0
        WRITTEN_TEXT = ""
        setText()

def resetGame():
    global CURSOR_INDEX, WRITTEN_TEXT, FIRST_TIME
    FIRST_TIME = True
    clearInterval(INTERVAL)
    CURSOR_INDEX = 0
    WRITTEN_TEXT = ""
    document.getElementById("text_input").value = ""
    setText()
    setTime(DEFAULT_TIME)


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
