from js import document
from pyodide import create_proxy
import random

import funcTimeMode.timeFunc
import funcCommon.commonFunc
DISPLAY_TEXT = document.getElementById("txt")
DATA = ""
TIME = 60
listOfWords = ["from", "add", "call", "another"]

def setTime(seconds):
    global TIME
    TIME = seconds
    document.getElementById("time").innerHTML = TIME
def getRandomText(wordsAmount):
    text = ''
    for i in range(wordsAmount-1):
        text += random.choice(listOfWords) + " "
    text += random.choice(listOfWords)
    return text
def checkShortcuts(event):
    global DATA
    if event.keyCode == 27:
        DATA = getRandomText(20)
        displayText()

def displayText():
    DISPLAY_TEXT.innerHTML = ""
    for character in DATA:
        characterSpan = document.createElement("span")
        characterSpan.innerHTML = character
        DISPLAY_TEXT.appendChild(characterSpan)
def inputEvent(event):
    if " " in str(event.target.value):
         event.target.value = ""

def setup():
    global DATA
    DATA = getRandomText(20)
    displayText()

    click_proxy = create_proxy(inputEvent)
    click = document.getElementById("text_input")
    click.addEventListener("input", click_proxy)

    check_proxy = create_proxy(checkShortcuts)
    document.addEventListener("keydown", check_proxy)

    #setTime
    document.getElementById("time").innerHTML = TIME

def main():
    setup()

if __name__ == "__main__":
    main()
