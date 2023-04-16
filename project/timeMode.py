import funcTimeMode.timeFunctions as tf
from js import document
from pyodide import create_proxy

class Start:
    def __init__(self):
        self.timeFunc = tf.TimeFunctions()
    def inputEvent(self, event):
        self.timeFunc.startGame(event)

    def setupTime(self, seconds):
        self.timeFunc.setTime(seconds)
        self.timeFunc.resetGame()

    def setupGame(self):
        self.timeFunc.setText()
        self.timeFunc.setTime(60)
        click_proxy = create_proxy(self.inputEvent)
        click = document.getElementById("text_input")
        click.addEventListener("input", click_proxy)

        check_proxy = create_proxy(self.timeFunc.checkShortcuts)
        document.addEventListener("keydown", check_proxy)


newGame = Start()
newGame.setupGame()
