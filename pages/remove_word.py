import tkinter as window_manager
from tkinter import messagebox

from utils import app_util
from utils.constant_holder import *


class RemoveWordPage(window_manager.Frame):
    def __init__(self, parent, controller):
        window_manager.Frame.__init__(self, parent)
        self.controller = controller
        self.config(background="green")
        self.grid(row=0, column=0, sticky="nsew")
        self.key_edit_text = window_manager.Entry(self, width=24)
        self.setup_page()

    def setup_page(self):
        self.setup_buttons()
        self.setup_labels()
        self.setup_edit_text()

    def setup_buttons(self):
        back_button = window_manager.Button(self, text=BUTTON_BACK_TEXT)
        back_button.config(background="grey", foreground="white")
        back_button.config(command=lambda: self.controller.show_window(app_util.get_welcome_page()))
        back_button.grid(row=2, column=0, sticky="ws", padx=8, pady=56)

        submit_button = window_manager.Button(self, text=BUTTON_SUBMIT_TEXT)
        submit_button.config(background="green", foreground="white")
        submit_button.config(command=lambda: self.confirm_choice())
        submit_button.grid(row=2, column=1, sticky="es", padx=8, pady=56)

    def confirm_choice(self):
        result = messagebox.askyesno(APP_NAME, QUESTION_TO_MODIFY_TEXT)
        if result:
            self.remove_word()

    def remove_word(self):
        database = app_util.get_database()
        database.execute(DELETE_WORD, (self.key_edit_text.get(), ))
        database.commit()
        database.close()

    def setup_labels(self):
        word_key_label = window_manager.Label(self, text=KEY_TO_DELETE_TEXT)
        word_key_label.config(background="green", foreground="white", font=APP_FONT)
        word_key_label.grid(row=0, column=0, sticky="wn", padx=16, pady=48)

    def setup_edit_text(self):
        self.key_edit_text.config(background="white", foreground="black", font=APP_FONT)
        self.key_edit_text.grid(row=0, column=1, pady=48, sticky="en")


