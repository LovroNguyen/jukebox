import tkinter as tk
import tkinter.scrolledtext as tkst

import font_manager as fonts
import track_library as lib
from track_library import library


def set_text(text_area, content):   
    text_area.delete("1.0", tk.END) 
    text_area.insert(1.0, content)


class ListCreator():
    def __init__(self, window):
        window.geometry("800x350")
        window.title("Create Track List")

        # Create List All Tracks Buttom
        list_tracks_btn = tk.Button(window, text="List All Tracks", command=self.list_tracks_clicked)
        list_tracks_btn.grid(row=0, column=0, padx=10, pady=10)

        # Create Enter Track Number Label
        enter_lbl = tk.Label(window, text="Enter Track Number")
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)

        # Create Track Number text area
        self.input_txt = tk.Entry(window, width=3)
        self.input_txt.grid(row=0, column=2, padx=10, pady=10)

        # Create View Track Button
        check_track_btn = tk.Button(window, text="Add Track", command=self.add_tracks_clicked) 
        check_track_btn.grid(row=0, column=3, padx=10, pady=10)

        # Create scrolled text area for Tracks List display
        self.list_txt = tkst.Text(window, width=48, height=12, wrap="none") 
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)

        # Create Added List Tracks text area
        self.track_txt = tk.Text(window, width=32, height=4, wrap="none") 
        self.track_txt.grid(row=1, column=3, sticky="NW", padx=10, pady=10)

        # Create status label
        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="W", padx=10, pady=10)

        # Create Reset Buttom
        reset_list_btn = tk.Button(window, text="Reset List", command=self.reset_tracks_clicked)
        reset_list_btn.grid(row=1, column=3, padx=10, pady=10)

        # Create Play Buttom
        play_btn = tk.Button(window, text="Play", command=self.play_tracks_clicked)
        play_btn.grid(row=1, column=3, padx=10, pady=(100,0))

        self.list_tracks_clicked()


    def reset_tracks_clicked(self):
        self.track_txt.delete('1.0', tk.END)
        self.status_lbl.configure(text="Reset List button was clicked!")

    def play_tracks_clicked(self): # NOT HAVE INCREASE PLAY COUNT YET!!!
        self.status_lbl.configure(text=f"Play button was clicked!")

    def add_tracks_clicked(self): 
        key = self.input_txt.get()
        name = lib.get_name(key)
        if name is not None:
            artist = lib.get_artist(key)
            rating = lib.get_rating(key)
            play_count = lib.get_play_count(key)
            track_details = f"{name} - {artist} - {'☆'*rating}\n"

            self.track_txt.insert(tk.END, track_details)
        else:
            set_text(self.track_txt, f"Track {key} not found")
        self.status_lbl.configure(text="Add Track button was clicked!")

    def list_tracks_clicked(self):
        track_list = lib.list_all()
        set_text(self.list_txt, track_list) 
        self.status_lbl.configure(text="List Tracks button was clicked!")


if __name__ == "__main__":
    window = tk.Tk()
    fonts.configure()
    ListCreator(window)
    window.mainloop()