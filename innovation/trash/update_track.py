import tkinter as tk
import tkinter.scrolledtext as tkst
import font_manager as fonts
import inovation.trash.track_library as lib
import webbrowser

def set_text(text_area, content):
    text_area.delete("1.0", tk.END)
    text_area.insert(1.0, content)

class TrackUpdater:
    def __init__(self, frame, status_lbl):
        self.status_lbl = status_lbl

        enter_name_lbl = tk.Label(frame, text="Enter Track Number")
        enter_name_lbl.grid(row=0, column=1, padx=10, pady=10)

        self.input_txt = tk.Entry(frame, width=35)
        self.input_txt.grid(row=0, column=2, padx=10, pady=10)

        enter_rating_lbl = tk.Label(frame, text="Enter New Track Rating")
        enter_rating_lbl.grid(row=2, column=1, padx=10, pady=10)

        self.rating_txt = tk.Entry(frame, width=35)
        self.rating_txt.grid(row=2, column=2, padx=10, pady=10)

        list_tracks_btn = tk.Button(frame, text="Update Rating", width=55, command=self.update_track_clicked)
        list_tracks_btn.grid(row=3, column=1, padx=10, pady=10, columnspan=2, sticky="ns")

    def update_track_clicked(self):
        number, rating = self.get_input_values()
        
        if not self.validate_input(number, rating):
            return
        self.update_track(number, rating)

    def get_input_values(self):
        try:
            number = self.input_txt.get()
            rating = int(self.rating_txt.get())
            return number, rating
        except ValueError:
            self.status_lbl.configure(text="Rating must be a number.")
            return None, None

    def validate_input(self, number, rating):
        errors = []
        if not number:
            errors.append("Track number")
        if rating is None or rating < 1 or rating > 5:
            errors.append("Rating must be between 1 and 5")
    
        if errors:
            self.status_lbl.configure(text=f"Please enter {', '.join(errors)}.")
            return False
        return True

    def update_track(self, number, rating):
        lib.get_name(number)
        lib.set_rating(number, rating)
        play_count = lib.get_play_count(number)
        self.status_lbl.configure(text=f"Track number {number} with rating {'☆'*rating} with {play_count} time(s) played was update successfully!")
