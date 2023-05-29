import json
from js import document
import logging as log
import random
import time
import js
import plotly.graph_objects as go


class Cmn:

    def __init__(self) -> None:
        self.start_time = time.time()

    def get_words(self, amount: int, level: int) -> str:
        if level == 1:
            path_to_file = "func_common/words/wordsLVL1.json"

        elif level == 2:
            path_to_file = "func_common/words/wordsLVL2.json"

        elif level == 3:
            path_to_file = "func_common/words/wordsLVL2.json"

        elif level == 4:
            path_to_file = "func_common/words/wordsLVL4.json"

        else:
            log.debug("you picked wrong level, selecting 1")
            level = 1
            path_to_file = "func_common/words/wordsLVL1.json"

        with open(path_to_file, 'r') as file:
            wordsJSON = json.load(file)
            words = wordsJSON["words"]
            output_text = ""
            for i in range(amount):
                random_word = random.choice(words)
                output_text += random_word + " "
            return output_text[:-1]

    def timer_start(self) -> None:
        self.start_time = time.time()

    def timer_stop(self) -> float:
        return round((time.time() - self.start_time), 2)

    def _raw_wpm_counter(self, all_char_amount: int, time_in_seconds: float) -> float:
        return round((all_char_amount / 5) / (time_in_seconds / 60))

    def _wpm_counter(self, all_char_amount: int, time_in_seconds: float, errors: int) -> float:
        return self._raw_wpm_counter(all_char_amount - errors, time_in_seconds)

    def _accuracy_counter(self, all_char_amount: int, errors: int) -> float:
        return round((all_char_amount - errors) / (all_char_amount / 100))

    def show_chart(self, data_list, method: str) -> None:
        def pad_unique(arr,
                       pad='\u200b'):
            # z githubu https://github.com/plotly/plotly.js/issues/1516
            # nemuze byt 1 stejna polozka 2x na stejne ose, tak se pirda pokazde 0widthspace
            mem = set()
            for idx, val in enumerate(arr):
                while val in mem:
                    val += pad
                mem.add(str(val))
                arr[idx] = val
            return arr

        x = list()
        y = list()
        if method == "raw_wpm":
            for data in data_list:
                x.append(data[0])
                y.append(self._raw_wpm_counter(len(data[0]), data[1]))
        elif method == "wpm":
            for data in data_list:
                x.append(data[0])
                y.append(self._wpm_counter(len(data[0]), data[1], data[2]))

        x = pad_unique(x)
        y = pad_unique(y)

        fig = go.Figure()
        fig.add_trace(
            go.Scatter(x=x, y=y, mode='lines+markers', marker_color='rgb(57,106,177)', marker_size=15, line_width=5,
                       line_shape='spline'))
        fig.update_layout(plot_bgcolor='rgb(78,74,74)',
                          paper_bgcolor='rgb(30, 30, 30)', font=dict(family='Arial', size=20, color='white'))

        js.plot(fig.to_json(), "chart")
        document.getElementById("overlay").style.visibility = "visible"
        document.getElementById("text_input").disabled = True
        wpm = 0
        for item in y:
            wpm += int(item)
        document.getElementById("wpm").innerHTML = round(wpm / len(y), 2)

    def hide_overlay(self, PE_object):
        document.getElementById("overlay").style.visibility = "hidden"
        text_input = document.getElementById("text_input")
        text_input.disabled = False
        text_input.value = ""
        text_input.focus()
