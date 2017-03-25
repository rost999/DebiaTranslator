import tkinter as window_manager
from tkinter import messagebox

from utils import app_util
from utils.constant_holder import *


class ModifyWordPage(window_manager.Frame):
    def __init__(self, parent, container):
        window_manager.Frame.__init__(self, parent)
        self.controller = container
        self.config(background="green")
        self.grid(row=0, column=0, sticky="nsew")
        self.key_edit_text = window_manager.Entry(self, width=24)
        self.value_edit_text = window_manager.Entry(self, width=24)
        self.setup_page()

    def setup_page(self):
        self.setup_buttons()
        self.setup_labels()
        self.setup_edit_text()

    def setup_buttons(self):
        back_button = window_manager.Button(self, text=BUTTON_BACK_TEXT)
        back_button.config(background="grey", foreground="white")
        back_button.config(command=lambda: self.controller.show_window(app_util.get_welcome_page()))
        back_button.grid(row=2, column=0, sticky="ws", padx=8, pady=40)

        submit_button = window_manager.Button(self, text=BUTTON_SUBMIT_TEXT)
        submit_button.config(background="green", foreground="white")
        submit_button.config(command=lambda: self.confirm_choice())
        submit_button.grid(row=2, column=0, sticky="es", padx=8, pady=40)

    def setup_labels(self):
        word_key_label = window_manager.Label(self, text=TEXT_WORD_KEY)
        word_key_label.config(background="green", foreground="white", font=APP_FONT)
        word_key_label.grid(row=0, column=0, sticky="wn", padx=16, pady=48)

        word_value_label = window_manager.Label(self, text=TEXT_NEW_WORD_VALUE)
        word_value_label.config(background="green", foreground="white", font=APP_FONT)
        word_value_label.grid(row=1, column=0, sticky="wn", padx=16)


    def confirm_choice(self):
        result = messagebox.askyesno(APP_NAME, QUESTION_TO_MODIFY_TEXT)
        print(str.format("TESININGI: {}".format(result)))
        if result:
            self.modify_word_value(self.value_edit_text.get())

    def setup_edit_text(self):
        self.key_edit_text.config(background="white", foreground="black", font=APP_FONT)
        self.key_edit_text.grid(row=0, column=1, pady=48, sticky="en")

        self.value_edit_text.config(background="white", foreground="black", font=APP_FONT)
        self.value_edit_text.grid(row=1, column=1)

    def modify_word_value(self, new_word_value):
        database = app_util.get_database()
        database.execute(UPDATE_WORD_KEY_VALUE, (new_word_value, self.key_edit_text.get()))
        database.commit()
        database.close()
