import tkinter as tk
import tkinter.scrolledtext as tkst

import track_library as lib
import font_manager as fonts


def set_text(text_area, content):   
    text_area.delete("1.0", tk.END) 
    text_area.insert(1.0, content)


class TrackUpdater():
    def __init__(self, window):
        window.geometry("650x250")
        window.title("Update Tracks")

        enter_name_lbl = tk.Label(window, text="Enter Track Name")
        enter_name_lbl.grid(row=0, column=1, padx=10, pady=10)

        self.input_txt = tk.Entry(window, width=45)
        self.input_txt.grid(row=0, column=2, padx=10, pady=10)

        enter_artist_lbl = tk.Label(window, text="Enter Artist Name")
        enter_artist_lbl.grid(row=1, column=1, padx=10, pady=10)

        self.artist_txt = tk.Entry(window, width=45)
        self.artist_txt.grid(row=1, column=2, padx=10, pady=10)

        enter_rating_lbl = tk.Label(window, text="Enter Track Rating")
        enter_rating_lbl.grid(row=2, column=1, padx=10, pady=10)

        self.rating_txt = tk.Entry(window, width=45)
        self.rating_txt.grid(row=2, column=2, padx=10, pady=10)

        list_tracks_btn = tk.Button(window, text="Add Track", width=55, command=self.add_track_clicked) #command=self.add_track_clicked
        list_tracks_btn.grid(row=3, column=1, padx=10, pady=10, columnspan=2, sticky="ns")

        # Create status label
        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=4, column=1, columnspan=2, sticky="SW", padx=10, pady=10)        


    def add_track_clicked(self):
        name, artist, rating = self.get_input_values()
        
        if not self.validate_input(name, artist, rating):
            return
        self.add_track(name, artist, rating)

    def get_input_values(self):
        try:
            name = self.input_txt.get()
            artist = self.artist_txt.get()
            rating = int(self.rating_txt.get())
            return name, artist, rating
        except ValueError:
            self.status_lbl.configure(text="Rating must be a number.")
            return None, None, None

    def validate_input(self, name, artist, rating):
        errors = []
        if not name:
            errors.append("Name of Track")
        if not artist:
            errors.append("Artist")
        if rating is None or rating < 1 or rating > 5:
            errors.append("Rating must be between 1 and 5")
    
        if errors:
            self.status_lbl.configure(text=f"Please enter {', '.join(errors)}.")
            return False
        return True

    def add_track(self, name, artist, rating):
        # Add track to the library
        lib.get_artist(artist)
        lib.get_name(name)
        lib.get_rating(rating)
        self.status_lbl.configure(text=f"Track {name} by {artist} with rating {rating} was added successfully!")


if __name__ == "__main__":
    window = tk.Tk()
    fonts.configure()
    TrackUpdater(window)
    window.mainloop()