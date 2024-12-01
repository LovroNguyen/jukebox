import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import csv
import webbrowser

class Helper:    
    @staticmethod
    def clear_frame():
        for widget in Helper.window.winfo_children():
            widget.destroy()

    @staticmethod
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

        
    @staticmethod
    def search_song(instance, event):
        query = instance.search_var.get().strip().lower()
        filtered_songs = [song for song in instance.songs if query in song['name'].lower() or query in song['artist'].lower()]
        instance.update_song_listbox(filtered_songs)

    @staticmethod
    def play_song(instance):
        selected_index = instance.song_listbox.curselection()
        if selected_index:
            song = instance.displayed_songs[selected_index[0]]  # Use displayed_songs instead of self.songs
            webbrowser.open(song['youtube_link'])
        else:
            messagebox.showwarning(title="Warning", message="Please choose a song from the list !")

    @staticmethod
    def display_song_details(instance, song):
        """Display details and image of the selected song."""
        try:
            # Load and resize the image
            pil_image = Image.open(song['image_path'])
            aspect_ratio = pil_image.width / pil_image.height
            new_height = 240
            new_width = int(aspect_ratio * new_height)

            pil_image = pil_image.resize((new_width, new_height), Image.LANCZOS)
            track_img = ImageTk.PhotoImage(pil_image)

            # Update image_label in the instance
            instance.image_label.config(image=track_img)
            instance.image_label.image = track_img
            instance.image_label.config(width=new_width, height=new_height)
        except (FileNotFoundError, OSError) as e:
            print(f"Error loading image: {e}")
            # Reset image label if error occurs
            instance.image_label.config(image='', bg="white", width=15, height=7)

        # Update song details label
        instance.song_details_label.config(
            text=f"Name: {song['name']}\nArtist: {song['artist']}\n"
        )

