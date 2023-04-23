from js import document
from pyodide import create_proxy
import random
import time
import func_common.common_func as common

WRONG = False
DATA = ""
DISPLAY_TEXT = document.getElementById("txt")
WRITTEN_TEXT = ""
FIRST_TIME = True
CURSOR_INDEX = 0
MISTAKES = 0
START_TIME = 0
TOTAL_WORD_COUNT = 0
LAST_WRONG_COUNT = 0


def set_text(ammount=2, difficulty=1):

    global DATA,TOTAL_WORD_COUNT
    TOTAL_WORD_COUNT = ammount
    DATA = common.get_words(ammount, difficulty)
    display_text()

def display_text():
    DISPLAY_TEXT.innerHTML = ""
    for character in DATA:
        character_span = document.createElement("span")
        character_span.innerHTML = character
        DISPLAY_TEXT.appendChild(character_span)

def check_shortcuts(event):
    if event.keyCode == 27:
        reset_game()



def text_correction(input_value):
    global WRONG,MISTAKES,CURSOR_INDEX,TOTAL_WORD_COUNT,LAST_WRONG_COUNT
    wrong_count = 0
    array_text = DISPLAY_TEXT.querySelectorAll('span')

    input_text = WRITTEN_TEXT + input_value
    user_list_input = [char for char in input_text]

    for index, element in enumerate(array_text):
        if len(user_list_input) <= index:
            element.classList.remove("correct")
            element.classList.remove("wrong")
        else:
            user_character = user_list_input[index]
            if element.innerText == user_character and wrong_count == 0:
                element.classList.remove("wrong")
                element.classList.add("correct")
            elif element.innerText != user_character or wrong_count > 0:
                element.classList.add("wrong")
                element.classList.remove("correct")
                wrong_count+=1

    if wrong_count > LAST_WRONG_COUNT:
        MISTAKES+=1

    LAST_WRONG_COUNT = wrong_count
    print(wrong_count)
    print("m",MISTAKES)
    if wrong_count > 0:
        WRONG = True
    else:
        WRONG = False


def input_event(event):
    global WRITTEN_TEXT, CURSOR_INDEX, FIRST_TIME, WRONG,MISTAKES
    if FIRST_TIME:
        common.timer_start()
        FIRST_TIME = False
    value = event.target.value
    if len(value) > len(DATA.split(" ")[CURSOR_INDEX]):
        event.target.value = value[:len(DATA.split(" ")[CURSOR_INDEX])]
    text_correction(value)
    if " " in str(value) and not WRONG:
        if len(value.replace(" ", "")) < len(DATA.split(" ")[CURSOR_INDEX]):
            value = value.replace(" ", "")
            value += "*" * (len(DATA.split(" ")[CURSOR_INDEX]) - len(value))
            text_correction(value)
            CURSOR_INDEX += 1
            event.target.value = ""
            WRITTEN_TEXT += value + " "
        else:
            CURSOR_INDEX += 1
            event.target.value = ""
            WRITTEN_TEXT += value
        another_text_words()

def another_text_words():
    global CURSOR_INDEX, WRITTEN_TEXT, FIRST_TIME, MISTAKES
    if CURSOR_INDEX == TOTAL_WORD_COUNT:
        print("Zabralo ti to:", common.timer_stop(), "sekund. Udělal jsi", MISTAKES, "chyb.")
        FIRST_TIME = True
        MISTAKES = 0
        CURSOR_INDEX = 0
        WRITTEN_TEXT = ""
        set_text()

def reset_game():
    global CURSOR_INDEX, WRITTEN_TEXT, FIRST_TIME
    FIRST_TIME = True
    CURSOR_INDEX = 0
    WRITTEN_TEXT = ""
    document.getElementById("text_input").value = ""
    set_text()
