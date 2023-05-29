from typing import Any

from js import document
from pyodide import create_proxy

import func_time_mode.time_functions as tf
import func_common.common_func as cf

class Start:
    def __init__(self) -> None:
        self.time_func = tf.TimeFunctions()
        self.cmn_func = cf.Cmn()

    def input_event(self, event: Any) -> None:
        self.time_func.start_game(event)

    def setup_time(self, seconds: int) -> None:
        self.time_func.set_time(seconds)
        self.time_func.reset_game()

    def setup_game(self) -> None:
        self.time_func.set_text()
        self.time_func.set_time(60)
        click_proxy = create_proxy(self.input_event)
        click = document.getElementById("text_input")
        click.addEventListener("input", click_proxy)
        hide_proxy = create_proxy(self.cmn_func.hide_overlay)
        button = document.getElementById("ok")
        button.addEventListener("click", hide_proxy)

        check_proxy = create_proxy(self.time_func.check_shortcuts)
        document.addEventListener("keydown", check_proxy)


new_game = Start()
new_game.setup_game()
