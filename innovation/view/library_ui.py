import tkinter as tk
from tkinter import *
import model.font_manager as fonts
from utils.helpers import Helper


class LibraryUI:
    def __init__(self, window, ui_manager):
        self.window = window
        self.ui_manager = ui_manager
        window.geometry("1200x600")
        window.title("JukeBox")

        fonts.configure()

        # Create GUI

        window.columnconfigure(0, weight=1)
        window.columnconfigure(1, weight=4)
        window.columnconfigure(2, weight=2)
        window.rowconfigure(0, weight=1)
        window.rowconfigure(1, weight=1)
        window.rowconfigure(2, weight=1)
        window.rowconfigure(3, weight=1)

        # create search bar
        self.search_var = tk.StringVar()
        search_entry = tk.Entry(window, textvariable=self.search_var, width=35)
        search_entry.grid(row=0, column=1, sticky="w", padx=10, pady=(20, 10))
        search_entry.bind('<KeyRelease>', lambda event: Helper.search_song(self, event))

        # invisible label for grid placement
        undisplay_lbl = tk.Label(window)
        undisplay_lbl.grid(row=2, column=0, padx=10, pady=10)

        self.song_listbox = Listbox(window, height=14, width=50)
        self.song_listbox.grid(row=1, column=1, rowspan=3, sticky="nsew", padx=10, pady=(10,20))
        self.song_listbox.bind('<<ListboxSelect>>', self.on_song_select)

        self.playlist_button = tk.Button(window, text="Playlist", width=12, command= self.playlist_button_clicked)
        self.playlist_button.grid(row=1, column=0, sticky="n", padx=(40,30), pady=(10, 10))

        self.image_label = tk.Label(window, bg="white", width=19, height=9)
        self.image_label.grid(row=1, column=2, rowspan=2, sticky="n", padx=(0, 0), pady=(10, 10))

        self.song_details_label = tk.Label(window, justify="left", width=30, anchor="w")
        self.song_details_label.grid(row=3, column=2, sticky="n", padx=(20, 20), pady=(10, 0))

        self.play_button = tk.Button(window, text="Play", width=10, command=lambda: Helper.play_song(self))
        self.play_button.grid(row=4, column=2, sticky="s", padx=10, pady=(0, 20))

        self.songs = []
        Helper.displayed_songs = []  # Add this line to store the currently displayed songs

        Helper.load_songs(self)

    def on_song_select(self, event):
        selected_index = self.song_listbox.curselection()
        if selected_index:
            song = Helper.displayed_songs[selected_index[0]]
            Helper.display_song_details(self, song)

    def update_song_listbox(self, songs):
        self.song_listbox.delete(0, tk.END)
        Helper.displayed_songs = songs  # Update the displayed songs
        for song in songs:
            self.song_listbox.insert(tk.END, f"{song['name']} - {song['artist']}")

    def playlist_button_clicked(self):
        self.ui_manager.show_playlist_ui()