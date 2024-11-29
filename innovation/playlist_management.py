import tkinter as tk
from tkinter import *
import tkinter.scrolledtext as tkst
import model.font_manager as fonts
import trash.track_library as lib
import webbrowser

def set_text(text_area, content):
    text_area.delete("1.0", tk.END)
    text_area.insert(1.0, content)

class PlaylistManager:
    def __init__(self,window):
        self.window = window
        window.geometry("1000x500")
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
        search_entry.bind('<KeyRelease>', ) #self.search_song

        # invisible label for grid placement
        undisplay_lbl = tk.Label(window)
        undisplay_lbl.grid(row=2, column=0, padx=10, pady=10)

        self.song_listbox = Listbox(window, height=14, width=50)
        self.song_listbox.grid(row=1, column=1, rowspan=3, sticky="nsew", padx=10, pady=(10,20))
        self.song_listbox.bind('<<ListboxSelect>>', self.on_song_select)

        self.playlist_button = tk.Button(window, text="Playlist", width=12, command=self.playlist_button_clicked)
        self.playlist_button.grid(row=1, column=0, sticky="n", padx=(20,10), pady=(10, 10))

        self.image_label = tk.Label(window, bg="white", width=19, height=9)
        self.image_label.grid(row=1, column=2, rowspan=2, sticky="n", padx=(0, 0), pady=(10, 10))

        self.song_details_label = tk.Label(window, justify="left", width=30, anchor="w")
        self.song_details_label.grid(row=3, column=2, sticky="n", padx=(20, 20), pady=(10, 0))

        self.play_button = tk.Button(window, text="Play", width=10, command=self.play_song)
        self.play_button.grid(row=4, column=2, sticky="s", padx=10, pady=(0, 10))

        self.songs = []
        self.displayed_songs = []  # Add this line to store the currently displayed songs

        self.load_songs()


    # def __init__(self, frame, status_lbl):
    #     self.status_lbl = status_lbl

    #     list_tracks_btn = tk.Button(frame, text="List All Tracks", command=self.list_tracks_clicked)
    #     list_tracks_btn.grid(row=0, column=0, padx=10, pady=10)

    #     enter_lbl = tk.Label(frame, text="Enter Track Number")
    #     enter_lbl.grid(row=0, column=1, padx=10, pady=10)

    #     self.input_txt = tk.Entry(frame, width=3)
    #     self.input_txt.grid(row=0, column=2, padx=10, pady=10)

    #     check_track_btn = tk.Button(frame, text="Add Track", command=self.add_tracks_clicked)
    #     check_track_btn.grid(row=0, column=3, padx=10, pady=10)

    #     self.list_txt = tkst.ScrolledText(frame, width=48, height=12, wrap="none")
    #     self.list_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)

    #     self.track_txt = tk.Text(frame, width=32, height=4, wrap="none")
    #     self.track_txt.grid(row=1, column=3, sticky="NW", padx=10, pady=10)

    #     reset_list_btn = tk.Button(frame, text="Reset List", command=self.reset_tracks_clicked)
    #     reset_list_btn.grid(row=1, column=3, padx=10, pady=10)

    #     play_btn = tk.Button(frame, text="Play", command=self.play_tracks_clicked)
    #     play_btn.grid(row=1, column=3, padx=10, pady=(100, 0))

    #     self.list_tracks_clicked()

    # def reset_tracks_clicked(self):
    #     self.track_txt.delete('1.0', tk.END)

    # def play_tracks_clicked(self):
    #     key = self.input_txt.get()
    #     youtube_link = lib.get_youtube_link(key)
    #     if youtube_link:
    #         webbrowser.open(youtube_link)
    #         lib.increment_play_count(key)
    #     else:
    #         self.status_lbl.configure(text=f"No YouTube link found for track {key}.")

    # def add_tracks_clicked(self):
    #     key = self.input_txt.get()
    #     name = lib.get_name(key)
    #     if name is not None:
    #         artist = lib.get_artist(key)
    #         rating = lib.get_rating(key)
    #         play_count = lib.get_play_count(key)
    #         track_details = f"{name} - {artist} - {'☆'*rating}\n"
    #         self.track_txt.insert(tk.END, track_details)
    #     else:
    #         set_text(self.track_txt, f"Track {key} not found")

    # def list_tracks_clicked(self):
    #     track_list = lib.list_all()
    #     set_text(self.list_txt, track_list)

if __name__ == "__main__":
    window = tk.Tk()
    app = PlaylistManager(window)
    window.mainloop()