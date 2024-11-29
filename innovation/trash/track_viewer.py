import tkinter as tk
import tkinter.scrolledtext as tkst
import model.font_manager as fonts
import track_library as lib
import webbrowser

def set_text(text_area, content):
    text_area.delete("1.0", tk.END)
    text_area.insert(1.0, content)

class TrackViewer:
    def __init__(self, frame, status_lbl):
        self.status_lbl = status_lbl

        list_tracks_btn = tk.Button(frame, text="List All Tracks", command=self.list_tracks_clicked)
        list_tracks_btn.grid(row=0, column=0, padx=10, pady=10)

        enter_lbl = tk.Label(frame, text="Enter Track Number")
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)

        self.input_txt = tk.Entry(frame, width=3)
        self.input_txt.grid(row=0, column=2, padx=10, pady=10)

        check_track_btn = tk.Button(frame, text="View Track", command=self.view_tracks_clicked)
        check_track_btn.grid(row=0, column=3, padx=10, pady=10)

        play_btn = tk.Button(frame, text="Play", command=self.play_tracks_clicked)
        play_btn.grid(row=1, column=3, padx=10, pady=(100, 0))

        self.list_txt = tkst.ScrolledText(frame, width=48, height=12, wrap="none")
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)

        self.track_txt = tk.Text(frame, width=32, height=4, wrap="none")
        self.track_txt.grid(row=1, column=3, sticky="NW", padx=10, pady=10)

        self.list_tracks_clicked()

    def view_tracks_clicked(self):
        key = self.input_txt.get()
        name = lib.get_name(key)
        if name is not None:
            artist = lib.get_artist(key)
            rating = lib.get_rating(key)
            play_count = lib.get_play_count(key)
            track_details = f"{name}\n{artist}\nrating: {"☆"*rating}\nplays: {play_count}"
            set_text(self.track_txt, track_details)
        else:
            set_text(self.track_txt, f"Track {key} not found")
        self.status_lbl.configure(text="View Track button was clicked!")

    def list_tracks_clicked(self):
        track_list = lib.list_all()
        set_text(self.list_txt, track_list)
        self.status_lbl.configure(text="List Tracks button was clicked!")

    def play_tracks_clicked(self):
        key = self.input_txt.get()
        youtube_link = lib.get_youtube_link(key)
        if youtube_link:
            webbrowser.open(youtube_link)
            lib.increment_play_count(key)
            self.status_lbl.configure(text=f"Playing track {key}!")
            self.view_tracks_clicked()
        else:
            self.status_lbl.configure(text=f"No YouTube link found for track {key}.")


