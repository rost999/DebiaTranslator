import tkinter as WindowFramework

from utils.app_util import *


class DebiaTranslatorApp(WindowFramework.Tk):
    def __init__(self, *args, **kwargs):
        WindowFramework.Tk.__init__(self, *args, **kwargs)
        container = WindowFramework.Frame(self)
        container.pack(side=WindowFramework.TOP, fill=WindowFramework.BOTH, expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        self.geometry("480x300")

        for page in (get_welcome_page(), get_translate_page(),
                     get_add_word_page(), get_modify_word_page(), get_remove_word_page()):
            frame = page(container, self)
            self.frames[page] = frame

        self.show_window(get_welcome_page())

    def show_window(self, window_to_show):
        current_frame = self.frames[window_to_show]
        current_frame.tkraise()


if __name__ == "__main__":
    app = DebiaTranslatorApp()
    app.title(APP_NAME)
    app.mainloop()

