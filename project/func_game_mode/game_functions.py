from js import document
from pyodide import create_proxy
import random
import time
import func_common.common_func as common

class GameFunctions:
    def __init__(self):
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


    def move_car(self, car):
        position = ((1+ self.cursor_index)/self.total_word_count) * 850
        car.style.left = str(position) +"px"

    def reset_car(self, car):
        car.style.left =  str((1/self.total_word_count) * 850) + "px"
    def set_text(self, ammount=25, difficulty=1):
        self.total_word_count = ammount
        self.data = common.get_words(ammount, difficulty)
        self.display_text()
        self.reset_car(self.player)

    def display_text(self):
        self.displayed_text.innerHTML = ""
        for character in self.data:
            character_span = document.createElement("span")
            character_span.innerHTML = character
            self.displayed_text.appendChild(character_span)

    def check_shortcuts(self, event):
        if event.keyCode == 27:
            self.reset_game()

    def text_correction(self, input_value):
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

    def input_event(self, event):
        self.move_car(self.player)

        if self.first_time:
            common.timer_start()
            self.first_time = False
        value = event.target.value
        if len(value) > len(self.data.split(" ")[self.cursor_index]):
            event.target.value = value[:len(self.data.split(" ")[self.cursor_index])]
        self.text_correction(value)
        if " " in str(value) and not self.wrong:
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


    def another_text_words(self, TOTAL_WORD_COUNT):
        if self.cursor_index == TOTAL_WORD_COUNT:
            print("Zabralo ti to:", common.timer_stop(), "sekund. Udělal jsi", self.mistakes, "chyb.")
            self.first_time = True
            self.mistakes = 0
            self.cursor_index = 0
            self.written_text = ""
            self.set_text()


    def reset_game(self):
        self.first_time = True
        self.cursor_index = 0
        self.written_text = ""
        self.set_text()