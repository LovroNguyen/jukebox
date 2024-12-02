import os
import csv
import tkinter as tk
from tkinter import messagebox

class PlaylistManagement:

    def __init__(self):
        self.script_dir = os.path.dirname(__file__)
        self.csv_path = os.path.join(self.script_dir, "../utils/playlists.csv")

        # Ensure the CSV file exists and has the correct structure
        if not os.path.exists(self.csv_path):
            with open(self.csv_path, 'w', newline='') as csvfile:
                fieldnames = ['name', 'songs']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()


    def get_playlists(self):
        playlists = []
        if os.path.exists(self.csv_path):
            with open(self.csv_path, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if 'name' in row and row['name'].strip():
                        playlists.append(row['name'])
                    else:
                        print(f"Skipping malformed row: {row}")  # Debug output
        print(f"Retrieved playlists: {playlists}")  # Debug output
        return playlists


    def load_playlist_songs(self, instance, playlist_name):
        instance.playlist_song_listbox.delete(0, tk.END)
        if os.path.exists(self.csv_path):
            with open(self.csv_path, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if row['name'] == playlist_name:
                        try:
                            songs = row['songs'].split(';')
                        except KeyError:
                            songs = []
                        for song in songs:
                            instance.playlist_song_listbox.insert(tk.END, song)


    def add_playlist(self, instance, playlist_name):
        if not playlist_name or not playlist_name.strip():
            tk.messagebox.showwarning("Warning", "Playlist name cannot be empty.")
            return  # Prevent adding empty or whitespace-only names

        playlist_name = playlist_name.strip()  # Remove leading/trailing whitespace

        # Check for duplicates
        if playlist_name in self.get_playlists():
            tk.messagebox.showwarning("Warning", f"The playlist '{playlist_name}' already exists.")
            return

        # Ensure the CSV exists and has a valid header
        if not os.path.exists(self.csv_path):
            with open(self.csv_path, 'w', newline='') as csvfile:
                fieldnames = ['name', 'songs']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()

        # Append the new playlist to the CSV
        with open(self.csv_path, 'a', newline='') as csvfile:
            fieldnames = ['name', 'songs']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'name': playlist_name, 'songs': ''})

        # Refresh the listbox
        instance.load_playlists()


    def remove_playlist(self, instance, playlist_name):
        playlists = []
        if os.path.exists(self.csv_path):
            with open(self.csv_path, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if row['name'] != playlist_name:
                        playlists.append(row)
        if not os.path.exists(self.csv_path):
            with open(self.csv_path, 'w', newline='') as csvfile:
                fieldnames = ['name', 'songs']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
        else:
            with open(self.csv_path, 'w', newline='') as csvfile:
                fieldnames = ['name', 'songs']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(playlists)

    def add_song_to_playlist(self, playlist_name, song):
        if not os.path.exists(self.csv_path):
            tk.messagebox.showerror("Error", "Playlist file not found.")
            return

        # Read all rows from the CSV
        with open(self.csv_path, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            rows = list(reader)

        # Find the playlist and update its song list
        updated = False
        for row in rows:
            if row['name'] == playlist_name:
                songs = row['songs'].split(';') if row['songs'] else []
                song_str = f"{song['name']} - {song['artist']}"
                if song_str not in songs:  # Avoid duplicate songs
                    songs.append(song_str)
                    row['songs'] = ';'.join(songs)
                    updated = True
                    break

        # Write the updated rows back to the CSV
        if updated:
            with open(self.csv_path, 'w', newline='') as csvfile:
                fieldnames = ['name', 'songs']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(rows)
            print(f"Song '{song['name']}' added to playlist '{playlist_name}'.")
        else:
            tk.messagebox.showinfo("Info", "Song is already in the playlist.")

    def remove_song_from_playlist(self, playlist_name, song_to_remove):
        if not os.path.exists(self.csv_path):
            tk.messagebox.showerror("Error", "Playlist file not found.")
            return

        # Read all rows from the CSV
        with open(self.csv_path, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            rows = list(reader)

        # Find the playlist and update its song list
        updated = False
        for row in rows:
            if row['name'] == playlist_name:
                songs = row['songs'].split(';') if row['songs'] else []
                if song_to_remove in songs:
                    songs.remove(song_to_remove)
                    row['songs'] = ';'.join(songs)
                    updated = True
                    break

        # Write the updated rows back to the CSV
        if updated:
            with open(self.csv_path, 'w', newline='') as csvfile:
                fieldnames = ['name', 'songs']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(rows)
            print(f"Song '{song_to_remove}' removed from playlist '{playlist_name}'.")
        else:
            tk.messagebox.showinfo("Info", "Song not found in the playlist.")
