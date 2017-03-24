from main_screen import WelcomeWindow
import Tkinter as WindowManager


class show_main_screen(WindowManager.Tk):
    def __init__(self, *args, **kwargs):
        WindowManager.Tk.__init__(self, args, kwargs)
        container = WindowManager.Frame(self)
        container.pack(side=WindowManager.TOP, fill=WindowManager.BOTH, expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        welcome_frame = WelcomeWindow(container, self)
        self.frames[WelcomeWindow] = welcome_frame

        welcome_frame.grid(row=0, column=0, sticky="nsew")

