from sys import exit
from PIL import Image, ImageTk
import Tkinter as WindowManager

RESOURCE_PATH = "res/"
GREETING_MESSAGE = """##############################################
Debia Translator v0.1
With all the love from ZoomPal Team
Author = Darel

1- To translate phrase or word

2- Add word to the dictionary

3- Remove word from the dictionary

4- Exit the program
##############################################"""


def close_app():
    exit()


class WelcomeWindow(WindowManager.Frame):
    def __init__(self, master=None):
        WindowManager.Frame.__init__(self, master)
        self.master = master
        self.setup_window()

    def show_logo(self):
        rendered_logo = ImageTk.PhotoImage(Image.open(RESOURCE_PATH + "zoom_logo.jpg"))
        present_logo = WindowManager.Label(self, image=rendered_logo)
        present_logo.image = rendered_logo
        present_logo.place(x=0, y=0)

    def show_greeting_message(self):
        message = WindowManager.Label(self, text=GREETING_MESSAGE)
        message.pack()

    def setup_window(self):
        self.master.title("Debia Translator")
        self.pack(fill=WindowManager.BOTH, expand=True)

        next_button = WindowManager.Button(self, text="Next", command=close_app)
        next_button.place(x=1, y=1)
        self.show_logo()
        self.show_greeting_message()
