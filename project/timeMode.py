import funcTimeMode.timeFunc as timeFunc
from js import document
from pyodide import create_proxy

def inputEvent(event):
    timeFunc.startGame(event)

def setupTime(seconds):
    timeFunc.setTime(seconds)
    timeFunc.resetGame()

def setupGame():
    timeFunc.setText()
    timeFunc.setTime(60)
    click_proxy = create_proxy(inputEvent)
    click = document.getElementById("text_input")
    click.addEventListener("input", click_proxy)

    check_proxy = create_proxy(timeFunc.checkShortcuts)
    document.addEventListener("keydown", check_proxy)

def main():
    setupGame()

if __name__ == "__main__":
    main()
