from js import document, setInterval, clearInterval
from pyodide import create_proxy
import funcCommon.commonFunc


GlDisplayText = document.getElementById("txt")
GlDisplayTime = document.getElementById("time")
GlInterval = None
GlWrittenText = ""
GlData = ""
GlDefaultTime = 60
GlTime = 60
GlFirstTime = True
GlCursorIndex = 0
GlResultForChart = []

#const
WORDS_AMOUNT = 25
MISTAKE = "*"

def setTime(seconds):
    global GlTime, GlDefaultTime, GlDisplayTime
    GlDefaultTime = seconds
    GlTime = seconds
    GlDisplayTime.innerHTML = GlTime

def timer():
    global GlTime
    GlTime -= 1
    GlDisplayTime.innerHTML = GlTime
    endOfTime()

def endOfTime():
    if GlTime == 0:
        clearInterval(GlInterval)
        gameEnd()

def runInterval():
    global GlInterval, GlFirstTime
    if GlFirstTime:
        proxy = create_proxy(timer)
        GlInterval = setInterval(proxy, 1000)
        GlFirstTime = False

def setText():
    global GlData
    GlData = funcCommon.commonFunc.getWords(WORDS_AMOUNT, 1)
    displayText()

def displayText():
    GlDisplayText.innerHTML = ""
    for character in GlData:
        characterSpan = document.createElement("span")
        characterSpan.innerHTML = character
        GlDisplayText.appendChild(characterSpan)

def checkShortcuts(event):
    if event.keyCode == 27:
        resetGame()

def TextCorrection(input_value):
    array_text = GlDisplayText.querySelectorAll('span')

    input_text = GlWrittenText + input_value
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

def startGame(event):
    global GlWrittenText, GlCursorIndex
    runInterval()
    value = event.target.value

    if len(value) > len(GlData.split(" ")[GlCursorIndex]):
        event.target.value = value[:len(GlData.split(" ")[GlCursorIndex])]
    TextCorrection(value)
    if " " in str(value):
        if len(value.replace(" ", "")) < len(GlData.split(" ")[GlCursorIndex]):
            replaceSpacesAsMistake(value)
            event.target.value = ""
        else:
            addWrittenWord(value)
            event.target.value = ""
        anotherTextWords()

def replaceSpacesAsMistake(value):
    value = value.replace(" ", "")
    value += MISTAKE * (len(GlData.split(" ")[GlCursorIndex]) - len(value))
    TextCorrection(value)
    addWrittenWord(value+" ")

def addWrittenWord(value):
    global GlWrittenText, GlCursorIndex
    if GlCursorIndex == WORDS_AMOUNT - 1:
        GlCursorIndex += 1
        GlWrittenText += value.replace(" ", "")
    else:
        GlCursorIndex += 1
        GlWrittenText += value

def anotherTextWords():
    global GlCursorIndex, GlWrittenText
    if GlCursorIndex == WORDS_AMOUNT:
        collectChartInfo()
        GlCursorIndex = 0
        GlWrittenText = ""
        setText()

def collectChartInfo():
    global GlResultForChart
    print(GlWrittenText)
    print(GlData)
    for index, word in enumerate(GlWrittenText.split(" ")):
        if word == GlData.split(" ")[index]:
            GlResultForChart.append([GlData.split(" ")[index], 0])
        else:
            wrongAmount = calculateMistakesInWord(rightWord=GlData.split(" ")[index], wrongWord=word)
            GlResultForChart.append([GlData.split(" ")[index], wrongAmount])

def calculateMistakesInWord(rightWord, wrongWord):
    mistakes = 0
    for i, character in enumerate(rightWord):
        if character != wrongWord[i]:
            mistakes += 1
    return mistakes

def resetGame():
    global GlCursorIndex, GlWrittenText, GlFirstTime
    GlFirstTime = True
    clearInterval(GlInterval)
    GlCursorIndex = 0
    GlWrittenText = ""
    document.getElementById("text_input").value = ""
    setText()
    setTime(GlDefaultTime)

def gameEnd():
    print("end of game")
    print("here will be link on chart with final Data")
    print(GlResultForChart)