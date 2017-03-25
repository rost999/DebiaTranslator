# coding=utf-8

import tkinter as window_manager

from utils import app_util
from utils.constant_holder import *


class TranslatePage(window_manager.Frame):
    def __init__(self, parent, controller):
        window_manager.Frame.__init__(self, parent)
        self.config(background="green")
        self.grid(row=0, column=0, sticky="nsew")
        self.text_watcher = window_manager.StringVar()
        self.input_edit_field = window_manager.Text(self, width=48, height=8, wrap=window_manager.WORD)
        self.result_value = window_manager.Label(self, width=48, height=8, textvariable=self.text_watcher)
        self.setup_page()
        self.controller = controller

        self.letter_map = {}

    def setup_page(self):
        self.setup_label()
        self.setup_buttons()
        self.setup_edit_box()

    def setup_label(self):
        input_label = window_manager.Label(self, text=TEXT_TO_TRANSLATE_LABEL)
        input_label.config(background="green", foreground="white", font=APP_FONT)
        input_label.grid(row=0, column=0, sticky="wn", padx=16, pady=24)

        result_label = window_manager.Label(self, text=TRANSLATION_RESULT_LABEL)
        result_label.config(background="green", foreground="white", font=APP_FONT)
        result_label.grid(row=1, column=0, sticky="wn", padx=16)

    def setup_edit_box(self):
        self.input_edit_field.config(background="white", foreground="black", font=APP_FONT)
        self.input_edit_field.grid(row=0, column=1, pady=8, sticky="en")

        self.result_value.config(background="white", foreground="black", font=APP_FONT)
        self.result_value.grid(row=1, column=1)

        scrollbar = window_manager.Scrollbar(self.result_value)
        # scrollbar.pack(side=window_manager.RIGHT)

    def go_back(self):
        self.controller.show_window(app_util.get_welcome_page())


    def setup_buttons(self):
        back_button = window_manager.Button(self, text=BUTTON_BACK_TEXT)
        back_button.config(background="grey", foreground="white")
        back_button.config(command=lambda: self.go_back())
        back_button.grid(row=2, column=0, sticky="ws", padx=8, pady=16)

        submit_button = window_manager.Button(self, text=BUTTON_SUBMIT_TEXT)
        submit_button.config(background="green", foreground="white")
        submit_button.config(command=lambda: self.translate_text())
        submit_button.grid(row=2, column=1, sticky="wn", padx=8, pady=16)

    def translate_text(self):
        user_input = self.input_edit_field.get(1.0, window_manager.END + "-1c")
        self.text_watcher.set(self.translate(user_input))

    def translate(self, user_input):
        self.setup_map()
        next_letter = ""
        after_next_letter = ""
        result = ""
        i = 0

        # trying to check if the full word
        # match any word in the dictionary
        # if not then just check letter by letter
        try:
            return self.letter_map[user_input]
        except KeyError:
            pass

        user_input = user_input.lower()

        try:
            while i < len(user_input):
                letter_at = user_input[i]

                if letter_at == " ":
                    result += letter_at
                    i += 1
                    continue

                elif letter_at == "’" or letter_at == "'":
                    i += 1
                    continue

                elif letter_at == "\n":
                    result += letter_at
                    i += 1
                    continue

                else:
                    try:
                        next_letter = user_input[i + 1]
                    except IndexError:
                        pass
                    try:
                        after_next_letter = user_input[i + 2]
                    except IndexError:
                        pass

                    if letter_at == "e" and (next_letter == "’" or next_letter == "'"):
                        try:
                            temp = self.letter_map[letter_at + "'"]
                        except KeyError:
                            temp = self.letter_map[letter_at + "’"]

                        result += temp
                        i += 1
                        continue

                    if letter_at == "n" and (after_next_letter == "’" or after_next_letter == "'"):
                        try:
                            temp = self.letter_map[letter_at + next_letter + "’"]

                        except KeyError:
                            temp = self.letter_map[letter_at + next_letter + "'"]

                        result += temp
                        i += 3

                    elif letter_at == "n" and next_letter == "e":
                        result += self.letter_map[(letter_at + next_letter)]
                        i += 2
                        continue

                    else:
                        result += self.letter_map[letter_at]
                        i += 1

            print("Current Result: " + result)
            return result
        except KeyError:
            # check maybe the word as new line inside
            result = ""
            for words in user_input.split("\n"):
                try:
                    result += self.letter_map[words]
                    print(result)
                except KeyError:
                    result += " NOT FOUND "
                result += "\n"
            return result

    def setup_map(self):
        database = app_util.get_database()
        cursor = database.cursor()
        cursor.execute(SELECT_EVERYTHING)
        for key, value in cursor.fetchall():
            self.letter_map[key] = value

        print(self.letter_map)
        database.close()
