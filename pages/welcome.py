from sys import exit

import tkinter as window_manager
from PIL import Image, ImageTk

from utils import app_util
from utils.constant_holder import *


def close_app():
    exit()


class WelcomeWindow(window_manager.Frame):
    def __init__(self, parent, controller):
        window_manager.Frame.__init__(self, parent)
        self.config(background="green")
        self.controller = controller
        self.pages = {}
        self.variable = window_manager.IntVar()
        self.translate_option = window_manager.Radiobutton(self, text=TRANSLATE_OPTION,
                                                           value=1,
                                                           variable=self.variable, indicatoron=1)

        self.add_word_option = window_manager.Radiobutton(self, text=ADD_WORD_OPTION,
                                                          value=2,
                                                          variable=self.variable, indicatoron=1)

        self.remove_word_option = window_manager.Radiobutton(self, text=REMOVE_WORD_OPTION,
                                                             value=3,
                                                             variable=self.variable, indicatoron=1)
        self.modify_word_option = window_manager.Radiobutton(self, text=MODIFY_WORD_OPTION,
                                                             value=4,
                                                             variable=self.variable, indicatoron=1)
        self.setup_check_boxes()
        self.variable.set(1)

        self.setup_window()

    def setup_window(self):
        self.setup_greeting_message()
        self.setup_logo()
        self.setup_buttons()
        self.pages[1] = app_util.get_translate_page()
        self.pages[2] = app_util.get_add_word_page()

    def setup_logo(self):
        rendered_logo = ImageTk.PhotoImage(Image.open(RESOURCE_PATH + "zoom_logo.jpg").resize((96, 96)))
        present_logo = window_manager.Label(self, image=rendered_logo)
        present_logo.image = rendered_logo
        present_logo.grid(row=0, column=0, padx=16, pady=8, sticky="wn")

    def setup_greeting_message(self):
        message = window_manager.Label(self, text=GREETING_MESSAGE, font=APP_FONT)
        message.config(background="white", foreground="green", pady=8)
        message.grid(row=0, column=1, padx=8, pady=8, sticky="ne")

    def setup_buttons(self):
        quit_button = window_manager.Button(self, text=BUTTON_EXIT_TEXT)
        quit_button.config(background="red", font=APP_FONT, foreground="white")
        quit_button.config(padx="24", command=lambda: close_app())
        quit_button.grid(row=6, column=0, pady=16)

        continue_button = window_manager.Button(self, text=BUTTON_CONTINUE_TEXT, font=APP_FONT)
        continue_button.config(background="blue", foreground="white")
        continue_button.config(padx="24", command=lambda: self.get_user_choice())
        continue_button.grid(row=6, column=1, pady=16)
        print(self.variable)

    def get_user_choice(self):
        self.controller.show_window(self.pages[self.variable.get()])

    def setup_check_boxes(self):
        self.translate_option.config(foreground="green", background="white")
        self.translate_option.config(pady=8)
        self.translate_option.grid(row=2, column=0)

        self.add_word_option.config(foreground="green", background="white")
        self.add_word_option.config(pady=8)
        self.add_word_option.grid(row=3, column=0)

        self.modify_word_option.config(foreground="green", background="white")
        self.modify_word_option.config(pady=8)
        self.modify_word_option.grid(row=4, column=0)

        self.remove_word_option.config(foreground="green", background="white", anchor="w")
        self.remove_word_option.config(pady=8)
        self.remove_word_option.grid(row=5, column=0, padx=8)
