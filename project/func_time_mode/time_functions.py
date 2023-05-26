from typing import List, Union, Any

import func_common.common_func
from js import clearInterval, document, setInterval
from pyodide import create_proxy


class TimeFunctions:
    WORDS_AMOUNT = 25
    MISTAKES = "*"

    def __init__(self) -> None:
        self.display_text = document.getElementById("txt")
        self.__display_time = document.getElementById("time")
        self.__interval = None
        self.__written_text = ""
        self.__data = ""
        self.__default_time = 60
        self.__time = 60
        self.__first_time = True
        self.__cursor_index = 0
        self.__result_for_chart: List[List[Union[str, int]]] = []

    def set_time(self, seconds: int) -> None:
        self.__default_time = seconds
        self.__time = seconds
        self.__display_time.innerHTML = self.__time

    def timer(self) -> None:
        self.__time -= 1
        self.__display_time.innerHTML = self.__time
        self.end_of_time()

    def end_of_time(self) -> None:
        if self.__time == 0:
            clearInterval(self.__interval)
            self.game_end()

    def run_interval(self) -> None:
        if self.__first_time:
            proxy = create_proxy(self.timer)
            self.__interval = setInterval(proxy, 1000)
            self.__first_time = False

    def set_text(self) -> None:
        self.__data = func_common.common_func.get_words(TimeFunctions.WORDS_AMOUNT, 1)
        self.display_text_lines()

    def display_text_lines(self) -> None:
        self.display_text.innerHTML = ""
        for character in self.__data:
            char_with_span = document.createElement("span")
            char_with_span.innerHTML = character
            self.display_text.appendChild(char_with_span)

    def check_shortcuts(self, event: Any) -> None:
        if event.keyCode == 27:
            func_common.common_func.hide_overlay(True)
            self.reset_game()

    def text_correction(self, input_value: str) -> None:
        text_list = self.display_text.querySelectorAll("span")

        input_text = self.__written_text + input_value
        user_list_input = list(input_text)

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

    def start_game(self, event: Any) -> None:
        self.run_interval()
        value = event.target.value

        if len(value) > len(self.__data.split(" ")[self.__cursor_index]):
            event.target.value = value[:len(self.__data.split(" ")[self.__cursor_index])]
        self.text_correction(value)
        if " " in str(value):
            if len(value.replace(" ", "")) < len(self.__data.split(" ")[self.__cursor_index]):
                self.replace_spaces_as_mistake(value)
                event.target.value = ""
            else:
                self.add_written_word(value)
                event.target.value = ""
            self.another_text_words()

    def replace_spaces_as_mistake(self, value: str) -> None:
        value = value.replace(" ", "")
        value += TimeFunctions.MISTAKES * \
                 (len(self.__data.split(" ")[self.__cursor_index]) - len(value))
        self.text_correction(value)
        self.add_written_word(value+" ")

    def add_written_word(self, word: str) -> None:
        if self.__cursor_index == TimeFunctions.WORDS_AMOUNT - 1:
            self.__cursor_index += 1
            self.__written_text += word.replace(" ", "")
        else:
            self.__cursor_index += 1
            self.__written_text += word

    def another_text_words(self) -> None:
        if self.__cursor_index == TimeFunctions.WORDS_AMOUNT:
            self.collect_chart_info()
            self.__cursor_index = 0
            self.__written_text = ""
            self.set_text()

    def collect_chart_info(self) -> None:
        for index, word in enumerate(self.__written_text.split(" ")):
            if word == self.__data.split(" ")[index]:
                self.__result_for_chart.append([self.__data.split(" ")[index], 0])
            else:
                wrong_amount = \
                    self.calculate_mistakes_in_word(right_word=self.__data.split(" ")[index],
                                                    wrong_word=word)
                self.__result_for_chart.append([self.__data.split(" ")[index], wrong_amount])

    def calculate_mistakes_in_word(self, right_word: str, wrong_word: str) -> int:
        mistakes = 0
        for i, character in enumerate(right_word):
            if character != wrong_word[i]:
                mistakes += 1
        return mistakes

    def reset_game(self) -> None:
        self.__first_time = True
        clearInterval(self.__interval)
        self.__cursor_index = 0
        self.__written_text = ""
        document.getElementById("text_input").value = ""
        self.set_text()
        self.set_time(self.__default_time)

    # docasne

    def game_end(self) -> None:
        print("end of game")
        print("here will be link on chart with final Data")
        print(self.__result_for_chart)
        func_common.common_func.show_chart([['Polozka', 3], ['test', 2], ['Polozka', 3], ['z', 1], ['test', 8]], "raw_wpm")
