import tkinter as tk
import tkinter.scrolledtext as tkst
from tkinter import *
from tkinter import messagebox
import font_manager as fonts
import webbrowser
import os
import csv
from PIL import Image, ImageTk
from playlist_management import PlaylistManager



def set_text(text_area, content):
    text_area.delete("1.0", tk.END)
    text_area.insert(1.0, content)


class Main:
    def __init__(self, window):
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
        search_entry.bind('<KeyRelease>', self.search_song)

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


    def clear_frame(self):
        for widget in self.window.winfo_children():
            widget.destroy()

    def load_songs(self):
        script_dir = os.path.dirname(__file__)
        csv_path = os.path.join(script_dir, "songs.csv")
        self.songs = []
        with open(csv_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                song = {
                    'name': row['name'],
                    'image_path': os.path.join(script_dir, row['image']),
                    'artist': row['artist'],
                    'youtube_link': row['youtube_link']
                }
                self.songs.append(song)
        self.update_song_listbox(self.songs)

    def update_song_listbox(self, songs):
        self.song_listbox.delete(0, tk.END)
        self.displayed_songs = songs  # Update the displayed songs
        for song in songs:
            self.song_listbox.insert(tk.END, f"{song['name']} - {song['artist']}")

    def search_song(self, event):
        query = self.search_var.get().strip().lower()
        filtered_songs = [song for song in self.songs if query in song['name'].lower() or query in song['artist'].lower()]
        self.update_song_listbox(filtered_songs)

    def play_song(self):
        selected_index = self.song_listbox.curselection()
        if selected_index:
            song = self.displayed_songs[selected_index[0]]  # Use displayed_songs instead of self.songs
            webbrowser.open(song['youtube_link'])
        else:
            messagebox.showwarning(title="Warning", message="Please choose a song from the list !")

    def on_song_select(self, event):
        selected_index = self.song_listbox.curselection()
        if selected_index:
            song = self.displayed_songs[selected_index[0]]  # Use displayed_songs instead of self.songs
            self.display_song_details(song)

    def display_song_details(self, song):
        try:
            pil_image = Image.open(song['image_path'])
            aspect_ratio = pil_image.width / pil_image.height
            new_height = 240
            new_width = int(aspect_ratio * new_height)
            if new_height > 240:
                new_height = 240
                new_width = int(aspect_ratio * new_height)

            pil_image = pil_image.resize((new_width, new_height), Image.Resampling.LANCZOS)
            track_img = ImageTk.PhotoImage(pil_image)

            self.image_label.config(image=track_img)
            self.image_label.image = track_img
            self.image_label.config(width=new_width, height=new_height)
        except Exception as e:
            print(f"Error loading image: {e}")
            self.image_label.config(image='', bg="white", width=15, height=7)

        self.song_details_label.config(
            text=f"Name: {song['name']}\nArtist: {song['artist']}\n"
        )

    def playlist_button_clicked(self):
        if False:
            messagebox.showinfo(title="Error", message="Playlist still in development!")
        else:
            self.clear_frame()
            PlaylistManager()

    


if __name__ == "__main__":
    window = tk.Tk()
    app = Main(window)
    window.mainloop()