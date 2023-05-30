from js import document
from pyodide import create_proxy
import func_game_mode.game_functions as gf
import func_common.common_func as cf


def main():
    game = gf.GameFunctions()
    setup(game)


def setup(game):
    cmn_func = cf.Cmn()
    game.set_text()
    click_proxy = create_proxy(game.input_event)
    click = document.getElementById("text_input")
    click.addEventListener("input", click_proxy)
    check_proxy = create_proxy(game.check_shortcuts)
    hide_proxy = create_proxy(cmn_func.hide_overlay)
    document.addEventListener("keydown", check_proxy)

    button = document.getElementById("ok")
    button.addEventListener("click", hide_proxy)

    change_difficulty_proxy = create_proxy(game.change_difficulty)
    radio_buttons = document.querySelectorAll('input[type="radio"]')
    for radio_button in radio_buttons:
        radio_button.addEventListener('change', change_difficulty_proxy)




if __name__ == "__main__":
    main()
