from js import document, setInterval, clearInterval
from pyodide import create_proxy
import funcCommon.commonFunc


class TimeFunctions:
    WORDS_AMOUNT = 25
    MISTAKES = "*"
    def __init__(self):
        self.displayText = document.getElementById("txt")
        self.__displayTime = document.getElementById("time")
        self.__interval = None
        self.__writtenText = ""
        self.__data = ""
        self.__defaultTime = 60
        self.__time = 60
        self.__firstTime = True
        self.__cursorIndex = 0
        self.__resultForChart = []

    def setTime(self, seconds):
        self.__defaultTime = seconds
        self.__time = seconds
        self.__displayTime.innerHTML = self.__time

    def timer(self):
        self.__time -= 1
        self.__displayTime.innerHTML = self.__time
        self.endOfTime()

    def endOfTime(self):
        if self.__time == 0:
            clearInterval(self.__interval)
            self.gameEnd()

    def runInterval(self):
        if self.__firstTime:
            proxy = create_proxy(self.timer)
            self.__interval = setInterval(proxy, 1000)
            self.__firstTime = False

    def setText(self):
        self.__data = funcCommon.commonFunc.getWords(TimeFunctions.WORDS_AMOUNT, 1)
        self.displayTextLines()

    def displayTextLines(self):
        self.displayText.innerHTML = ""
        for character in self.__data:
            characterSPAN = document.createElement("span")
            characterSPAN.innerHTML = character
            self.displayText.appendChild(characterSPAN)

    def checkShortcuts(self, event):
        if event.keyCode == 27:
            self.resetGame()

    def TextCorrection(self, input_value):
        text_list = self.displayText.querySelectorAll("span")

        input_text = self.__writtenText + input_value
        user_list_input = [char for char in input_text]

        for index, element in enumerate(text_list):
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

    def startGame(self, event):
        self.runInterval()
        value = event.target.value

        if len(value) > len(self.__data.split(" ")[self.__cursorIndex]):
            event.target.value = value[:len(self.__data.split(" ")[self.__cursorIndex])]
        self.TextCorrection(value)
        if " " in str(value):
            if len(value.replace(" ", "")) < len(self.__data.split(" ")[self.__cursorIndex]):
                self.replaceSpacesAsMistake(value)
                event.target.value = ""
            else:
                self.addWrittenWord(value)
                event.target.value = ""
            self.anotherTextWords()

    def replaceSpacesAsMistake(self, value):
        value = value.replace(" ", "")
        value += TimeFunctions.MISTAKES * (len(self.__data.split(" ")[self.__cursorIndex]) - len(value))
        self.TextCorrection(value)
        self.addWrittenWord(value+" ")

    def addWrittenWord(self, value):
        if self.__cursorIndex == TimeFunctions.WORDS_AMOUNT - 1:
            self.__cursorIndex += 1
            self.__writtenText += value.replace(" ", "")
        else:
            self.__cursorIndex += 1
            self.__writtenText += value

    def anotherTextWords(self):
        if self.__cursorIndex == TimeFunctions.WORDS_AMOUNT:
            self.collectChartInfo()
            self.__cursorIndex = 0
            self.__writtenText = ""
            self.setText()

    def collectChartInfo(self):
        for index, word in enumerate(self.__writtenText.split(" ")):
            if word == self.__data.split(" ")[index]:
                self.__resultForChart.append([self.__data.split(" ")[index], 0])
            else:
                wrongAmount = self.calculateMistakesInWord(rightWord=self.__data.split(" ")[index], wrongWord=word)
                self.__resultForChart.append([self.__data.split(" ")[index], wrongAmount])

    def calculateMistakesInWord(self, rightWord, wrongWord):
        mistakes = 0
        for i, character in enumerate(rightWord):
            if character != wrongWord[i]:
                mistakes += 1
        return mistakes

    def resetGame(self):
        self.__firstTime = True
        clearInterval(self.__interval)
        self.__cursorIndex = 0
        self.__writtenText = ""
        document.getElementById("text_input").value = ""
        self.setText()
        self.setTime(self.__defaultTime)


    # docasne
    def gameEnd(self):
        print("end of game")
        print("here will be link on chart with final Data")
        print(self.__resultForChart)
