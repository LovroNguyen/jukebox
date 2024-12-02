import tkinter as tk
from view.library_ui import LibraryUI
from view.playlist_ui import PlaylistUI


class UIManager:
    def __init__(self):
        self.window = tk.Tk()
        self.show_library_ui()

    def show_library_ui(self):
        self.window.destroy()
        self.window = tk.Tk()
        app = LibraryUI(self.window, self)
        self.window.mainloop()

    def show_playlist_ui(self):
        self.window.destroy()
        self.window = tk.Tk()
        app = PlaylistUI(self.window, self)
        self.window.mainloop()
