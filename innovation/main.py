import tkinter as tk
from view.library_ui import LibraryUI

if __name__ == "__main__":
    window = tk.Tk()
    app = LibraryUI(window)
    window.mainloop()


    # def clear_frame(self):
    #     for widget in self.window.winfo_children():
    #         widget.destroy()

    # def load_songs(self):
    #     script_dir = os.path.dirname(__file__)
    #     csv_path = os.path.join(script_dir, "songs.csv") 
    #     self.songs = []
    #     with open(csv_path, newline='') as csvfile:
    #         reader = csv.DictReader(csvfile)
    #         for row in reader:
    #             song = {
    #                 'name': row['name'],
    #                 'image_path': os.path.join(script_dir, row['image']),
    #                 'artist': row['artist'],
    #                 'youtube_link': row['youtube_link']
    #             }
    #             self.songs.append(song)
    #     self.update_song_listbox(self.songs)

    # def update_song_listbox(self, songs):
    #     self.song_listbox.delete(0, tk.END)
    #     self.displayed_songs = songs  # Update the displayed songs
    #     for song in songs:
    #         self.song_listbox.insert(tk.END, f"{song['name']} - {song['artist']}")

    # def search_song(self, event):
    #     query = self.search_var.get().strip().lower()
    #     filtered_songs = [song for song in self.songs if query in song['name'].lower() or query in song['artist'].lower()]
    #     self.update_song_listbox(filtered_songs)

    # def play_song(self):
    #     selected_index = self.song_listbox.curselection()
    #     if selected_index:
    #         song = self.displayed_songs[selected_index[0]]  # Use displayed_songs instead of self.songs
    #         webbrowser.open(song['youtube_link'])
    #     else:
    #         messagebox.showwarning(title="Warning", message="Please choose a song from the list !")

    # def on_song_select(self, event):
    #     selected_index = self.song_listbox.curselection()
    #     if selected_index:
    #         song = self.displayed_songs[selected_index[0]]  # Use displayed_songs instead of self.songs
    #         self.display_song_details(song)

    # def display_song_details(self, song):
    #     try:
    #         pil_image = Image.open(song['image_path'])
    #         aspect_ratio = pil_image.width / pil_image.height
    #         new_height = 240
    #         new_width = int(aspect_ratio * new_height)
    #         if new_height > 240:
    #             new_height = 240
    #             new_width = int(aspect_ratio * new_height)

    #         pil_image = pil_image.resize((new_width, new_height), Image.Resampling.LANCZOS)
    #         track_img = ImageTk.PhotoImage(pil_image)

    #         self.image_label.config(image=track_img)
    #         self.image_label.image = track_img
    #         self.image_label.config(width=new_width, height=new_height)
    #     except Exception as e:
    #         print(f"Error loading image: {e}")
    #         self.image_label.config(image='', bg="white", width=15, height=7)

    #     self.song_details_label.config(
    #         text=f"Name: {song['name']}\nArtist: {song['artist']}\n"
    #     )

    # def playlist_button_clicked(self):
    #     self.clear_frame()
