from js import document
import js
from pyodide import create_proxy
import random
import time
import func_common.common_func as common

class GameFunctions:
    def __init__(self):
        self.cmn_func = common.Cmn()
        self.wrong = False
        self.data = ""
        self.displayed_text = document.getElementById("txt")
        self.written_text = ""
        self.first_time = True
        self.cursor_index = 0
        self.mistakes = 0
        self.start_time = 0
        self.total_word_count = 0
        self.last_wrong_count = 0
        self.player = document.getElementById("player")
        self.bot = document.getElementById("bot")
        self.player_won = False
        self.data_for_chart = list()
        self.difficulty = 1
        self.text_input = document.getElementById("text_input")
        self.lost = document.getElementById("lost")


    def move_player(self, car) -> None:
        position = ((1+self.cursor_index)/(self.total_word_count -1)) * 850
        car.style.left = str(position) +"px"

    def move_bot(self, difficulty=1) -> None:
        position = int(self.bot.style.left.replace("px", ""))
        if difficulty == 1:
            speed = 55
        elif difficulty == 2:
            speed = 45
        elif difficulty == 3:
            speed = 35

        def move() -> None:
            if(not self.player_won):
                nonlocal position # definovano mimo "move"
                position += 1
                self.bot.style.left = str(position) + "px"
                if position < 850 and not self.player_won:
                    js.setTimeout(create_proxy(move), speed)
                else:
                    if(not self.player_won):
                        self.end_game(self.bot)
        move()

    def reset_car(self, car) -> None:
        car.style.left ="0px"
    def set_text(self, ammount=25, difficulty=1) -> None:
        self.total_word_count = ammount
        self.data = self.cmn_func.get_words(ammount, difficulty)
        self.display_text()
        self.reset_car(self.player)
        self.reset_car(self.bot)

    def display_text(self) -> None:
        self.displayed_text.innerHTML = ""
        for character in self.data:
            character_span = document.createElement("span")
            character_span.innerHTML = character
            self.displayed_text.appendChild(character_span)

    def check_shortcuts(self, event) -> None:
        if event.keyCode == 27:
            self.reset_game()
            self.text_input.value = ""
            self.cmn_func.hide_overlay(True)
            self.lost.style.visibility = "hidden"
            self.text_input.disabled = False

    def text_correction(self, input_value) -> None:
        wrong_count = 0
        array_text = self.displayed_text.querySelectorAll('span')

        input_text = self.written_text + input_value
        user_list_input = [char for char in input_text]

        for index, element in enumerate(array_text):
            if len(user_list_input) <= index:
                element.classList.remove("correct")
                element.classList.remove("wrong")
                element.classList.remove("warn")
            else:
                if wrong_count > 0:
                    element.classList.remove("correct")
                    element.classList.remove("wrong")
                    element.classList.add("warn")
                else:
                    user_character = user_list_input[index]
                    if element.innerText == user_character: #spravne
                        element.classList.remove("wrong")
                        element.classList.add("correct")
                        element.classList.remove("warn")
                    elif element.innerText != user_character:
                        element.classList.add("wrong")
                        element.classList.remove("correct")
                        element.classList.remove("warn")
                        wrong_count += 1

        if wrong_count > self.last_wrong_count:
            self.mistakes += 1

        self.last_wrong_count = wrong_count
        if wrong_count > 0:
            self.wrong = True
        else:
            self.wrong = False

    def input_event(self, event) -> None:
        if self.first_time:
            self.cmn_func.timer_start()
            self.player_won = False
            self.first_time = False
            self.move_bot(self.difficulty)

        value = event.target.value
        if len(value) > len(self.data.split(" ")[self.cursor_index]):
            event.target.value = value[:len(self.data.split(" ")[self.cursor_index])]

        self.text_correction(value)
        if " " in str(value) and not self.wrong:
            #konec slova
            self.data_for_chart.append([str(value), self.cmn_func.timer_stop()])
            self.cmn_func.timer_start()
            self.move_player(self.player)
            if len(value.replace(" ", "")) < len(self.data.split(" ")[self.cursor_index]):
                value = value.replace(" ", "")
                value += "*" * (len(self.data.split(" ")[self.cursor_index]) - len(value))
                self.text_correction(value)
                self.cursor_index += 1
                event.target.value = ""
                self.written_text += value + " "
            else:
                self.cursor_index += 1
                event.target.value = ""
                self.written_text += value
            self.another_text_words(self.total_word_count)


    def another_text_words(self, TOTAL_WORD_COUNT) -> None:
        if self.cursor_index == TOTAL_WORD_COUNT:
            self.end_game(self.player)

    def change_difficulty(self, event) -> None:
        selected_value = event.target.id
        if selected_value == "optionHard":
            self.difficulty = 3
        elif selected_value == "optionMedium":
            self.difficulty = 2
        else:
            self.difficulty = 1
        self.lost.style.visibility = "hidden"
        self.text_input.disabled = False
        self.text_input.focus()
        self.reset_game()


    def reset_game(self) -> None:
        self.text_input.value = ""
        self.player_won = True
        self.mistakes = 0
        self.first_time = True
        self.cursor_index = 0
        self.written_text = ""
        self.set_text(difficulty=self.difficulty)
        self.data_for_chart = []


    def end_game(self, car) -> None:
        if car == self.player:
            self.player_won = True
            self.cmn_func.show_chart(self.data_for_chart, "raw_wpm")
        elif car == self.bot:
            self.lost.style.visibility = "visible"
            self.text_input.disabled = True
        self.reset_game()
