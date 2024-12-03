import tkinter as tk
from tkinter import *
from tkinter import simpledialog
from utils.helpers import Helper
import model.font_manager as fonts
from model.playlist_management import PlaylistManagement



class PlaylistUI:
    def __init__(self, window, ui_manager):
        self.window = window
        self.ui_manager = ui_manager
        window.geometry("1200x600")
        window.title("JukeBox")

        fonts.configure()

        self.playlist_manager = PlaylistManagement()

        # Configure grid
        window.columnconfigure(0, weight=1)
        window.columnconfigure(1, weight=4)
        window.columnconfigure(2, weight=2)
        window.rowconfigure(0, weight=1)
        window.rowconfigure(1, weight=1)
        window.rowconfigure(2, weight=1)
        window.rowconfigure(3, weight=1)

        # Create widgets
        self.search_var = tk.StringVar()
        search_entry = tk.Entry(window, textvariable=self.search_var, width=35)
        search_entry.grid(row=0, column=1, sticky="w", padx=10, pady=(20, 10))
        search_entry.bind('<KeyRelease>', lambda event: Helper.search_song(self, event))

        self.back_button = tk.Button(window, text="Back", width=12, command=self.back_button_clicked)
        self.back_button.grid(row=1, column=0, sticky="n", padx=(40,30), pady=(10, 10))

        self.add_to_playlist_button = tk.Button(window, text="Add", width=10, command=self.add_to_playlist)
        self.add_to_playlist_button.grid(row=3, column=2, sticky="sw", padx=(50,25), pady=(0,20))

        self.remove_from_button = tk.Button(window, text="Remove", width=10, command=self.remove_song_from_playlist)
        self.remove_from_button.grid(row=3, column=3, sticky="sw", padx=(25,30), pady=(0,20))

        self.add_playlist_button = tk.Button(window, text="Add playlist", width=14, command=self.add_playlist)
        self.add_playlist_button.grid(row=1, column=0, padx=(20,10), pady=(20, 0))

        self.remove_playlist_button = tk.Button(window, text="Remove playlist", width=14, command=self.remove_playlist)
        self.remove_playlist_button.grid(row=1, column=0, sticky="s", padx=(20,10), pady=(0, 20))

        self.song_listbox = tk.Listbox(window, height=7, width=50, exportselection=0)
        self.song_listbox.grid(row=1, column=1, sticky="nsew", padx=10, pady=(10,15))
        self.song_listbox.bind('<<ListboxSelect>>', self.on_song_select)

        self.image_label = tk.Label(window, bg="white", width=19, height=9)
        self.image_label.grid(row=1, column=2, rowspan=2, columnspan=2, sticky="n", padx=(0, 0), pady=(10, 0))

        self.song_details_label = tk.Label(window, justify="left", width=30, anchor="w")
        self.song_details_label.grid(row=2, column=2, columnspan=2, padx=(20, 20), pady=(10, 0))

        self.playlist_song_listbox = tk.Listbox(window, height=7, width=50, exportselection=0)
        self.playlist_song_listbox.grid(row=2, column=1, sticky="nsew", padx=10, pady=(10,10))
        self.playlist_song_listbox.bind('<<ListboxSelect>>', self.on_playlist_song_select)

        self.playlist_listbox = tk.Listbox(window, height=7, width=10, exportselection=0)
        self.playlist_listbox.grid(row=2, column=0, sticky="nsew", padx=(10,0), pady=(10,10))
        self.playlist_listbox.bind('<<ListboxSelect>>', self.on_playlist_select)

        self.songs = []
        Helper.displayed_songs = []

        Helper.load_songs(self)
        self.load_playlists()

    def on_song_select(self, event):
        selected_index = self.song_listbox.curselection()
        if selected_index:
            song = Helper.displayed_songs[selected_index[0]]
            Helper.display_song_details(self, song)

    def on_playlist_select(self, event):
        selected_index = self.playlist_listbox.curselection()
        if selected_index:
            playlist_name = self.playlist_listbox.get(selected_index[0])
            self.playlist_manager.load_playlist_songs(self, playlist_name)

    def on_playlist_song_select(self, event):
        selected_index = self.playlist_song_listbox.curselection()
        if selected_index:
            song_str = self.playlist_songs[selected_index[0]]
            song_name, song_artist = song_str.split(' - ')
            for song in Helper.displayed_songs:
                if song['name'] == song_name and song['artist'] == song_artist:
                    Helper.display_song_details(self, song)
                    break

    def add_to_playlist(self):
        selected_song_index = self.song_listbox.curselection()
        selected_playlist_index = self.playlist_listbox.curselection()

        if not selected_song_index:
            tk.messagebox.showwarning("Warning", "Please select a song to add.")
            return
        if not selected_playlist_index:
            tk.messagebox.showwarning("Warning", "Please select a playlist to add the song to.")
            return

        # Get selected song and playlist
        song = Helper.displayed_songs[selected_song_index[0]]
        playlist_name = self.playlist_listbox.get(selected_playlist_index[0])

        # Add the song to the playlist
        self.playlist_manager.add_song_to_playlist(playlist_name, song)

        # Refresh the playlist song listbox
        self.playlist_manager.load_playlist_songs(self, playlist_name)

    def remove_song_from_playlist(self):
        selected_song_index = self.playlist_song_listbox.curselection()
        selected_playlist_index = self.playlist_listbox.curselection()

        if not selected_song_index:
            tk.messagebox.showwarning("Warning", "Please select a song to remove.")
            return
        if not selected_playlist_index:
            tk.messagebox.showwarning("Warning", "Please select a playlist.")
            return

        # Get selected song and playlist
        selected_song = self.playlist_song_listbox.get(selected_song_index[0])
        playlist_name = self.playlist_listbox.get(selected_playlist_index[0])

        # Remove the song from the playlist
        self.playlist_manager.remove_song_from_playlist(playlist_name, selected_song)

        # Refresh the playlist song listbox
        self.playlist_manager.load_playlist_songs(self, playlist_name)

    def add_playlist(self):
        def on_ok():
            playlist_name = entry.get()
            if not playlist_name.strip():
                tk.messagebox.showwarning("Warning", "Playlist name cannot be empty.")
            else:
                self.playlist_manager.add_playlist(self, playlist_name)
                self.load_playlists()
            dialog.destroy()

        dialog = tk.Toplevel(self.window)
        dialog.title("Playlist Name")
        dialog.geometry("320x140")

        label = tk.Label(dialog, text="Enter the name of the new playlist:")
        label.pack(pady=10)

        entry = tk.Entry(dialog, width=30)
        entry.pack(pady=5)

        button_frame = tk.Frame(dialog)
        button_frame.pack(pady=5)

        ok_button = tk.Button(button_frame, width=10, text="OK", command=on_ok)
        ok_button.pack(side="left", padx=5, pady=5)

        cancel_button = tk.Button(button_frame, width=10, text="Cancel", command=dialog.destroy)
        cancel_button.pack(side="right", padx=5, pady=5)

    def remove_playlist(self):
        selected_index = self.playlist_listbox.curselection()
        if not selected_index:
            tk.messagebox.showwarning("Warning", "Please select a playlist to remove.")
            return
        else:
            playlist_name = self.playlist_listbox.get(selected_index[0])
            self.playlist_manager.remove_playlist(self, playlist_name)
            self.load_playlists()

    def load_playlists(self):
        self.playlist_listbox.delete(0, tk.END)
        playlists = self.playlist_manager.get_playlists()
        print(f"Loading playlists into listbox: {playlists}")  # Debug output

        for playlist in playlists:
            self.playlist_listbox.insert(tk.END, playlist)

        print(f"Listbox contains {self.playlist_listbox.size()} items.")  # Debug output

    def update_song_listbox(self, songs):
        self.song_listbox.delete(0, tk.END)
        Helper.displayed_songs = songs
        for song in songs:
            self.song_listbox.insert(tk.END, f"{song['name']} - {song['artist']}")    

    def back_button_clicked(self):
        self.ui_manager.show_library_ui()