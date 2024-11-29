import tkinter as tk
import tkinter.scrolledtext as tkst


import track_library as lib
import font_manager as fonts


def set_text(text_area, content):   
    text_area.delete("1.0", tk.END) 
    text_area.insert(1.0, content)


class TrackViewer():
    def __init__(self, window):
        window.geometry("750x350")      # set the window size
        window.title("View Tracks")     # set window title

        list_tracks_btn = tk.Button(window, text="List All Tracks", command=self.list_tracks_clicked) # create button name "List All Tracks"
        list_tracks_btn.grid(row=0, column=0, padx=10, pady=10) # set button size

        enter_lbl = tk.Label(window, text="Enter Track Number") # create "Enter Track Number" label
        enter_lbl.grid(row=0, column=1, padx=10, pady=10) # set label size

        self.input_txt = tk.Entry(window, width=3) # create "Enter Track Number" text area
        self.input_txt.grid(row=0, column=2, padx=10, pady=10) # set "Enter Track Number" text area size 

        check_track_btn = tk.Button(window, text="View Track", command=self.view_tracks_clicked) # create "View Track" Button with 'view_track_clicked' command
        check_track_btn.grid(row=0, column=3, padx=10, pady=10) # set "View Track" button size

        self.list_txt = tkst.ScrolledText(window, width=48, height=12, wrap="none") # create scrolled text area for Tracks display
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10) # set tracks display text area

        self.track_txt = tk.Text(window, width=24, height=4, wrap="none") # create added tracks text area
        self.track_txt.grid(row=1, column=3, sticky="NW", padx=10, pady=10) # set added tracks text area size

        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10)) # create annouce action label
        self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="W", padx=10, pady=10) # set label size

        self.list_tracks_clicked() # invoke the function to list all tracks on startup

    def view_tracks_clicked(self): 
        key = self.input_txt.get()  # get the track number from the input text field
        name = lib.get_name(key)  # get the track name using the track number
        if name is not None:  # if the track name is found
            artist = lib.get_artist(key)  # get the artist name using the track number
            rating = lib.get_rating(key)  # get the track rating using the track number
            play_count = lib.get_play_count(key)  # get the play count using the track number
            track_details = f"{name}\n{artist}\nrating: {rating}\nplays: {play_count}"  # format the track details
            set_text(self.track_txt, track_details)  # display the track details in the track text area
        else:  # if the track name is not found
            set_text(self.track_txt, f"Track {key} not found")  # display an error message in the track text area
        self.status_lbl.configure(text="View Track button was clicked!")  # update the status label

    def list_tracks_clicked(self):
        track_list = lib.list_all()  # get the list of all tracks
        set_text(self.list_txt, track_list)  # display the list of all tracks in the list text area
        self.status_lbl.configure(text="List Tracks button was clicked!")  # update the status label

if __name__ == "__main__":  # only runs when this file is run as a standalone
    window = tk.Tk()        # create a TK object
    fonts.configure()       # configure the fonts
    TrackViewer(window)     # open the TrackViewer GUI
    window.mainloop()       # run the window main loop, reacting to button presses, etc
