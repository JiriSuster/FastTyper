from js import document
from pyodide import create_proxy
import funcGameMode.gameFunc as game



def main():
    setup()

def setup():
    game.set_text()
    click_proxy = create_proxy(game.input_event)
    click = document.getElementById("text_input")
    click.addEventListener("input", click_proxy)

    check_proxy = create_proxy(game.check_shortcuts)
    document.addEventListener("keydown", check_proxy)

if __name__ == "__main__":
    main()
