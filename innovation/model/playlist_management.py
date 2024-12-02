import os
import csv
import tkinter as tk
from tkinter import messagebox

class PlaylistManagement:

    def __init__(self):
        self.script_dir = os.path.dirname(__file__)
        self.csv_path = os.path.join(self.script_dir, "../utils/playlists.csv")

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
        return playlists

    def load_playlist_songs(self, instance, playlist_name):
        instance.playlist_song_listbox.delete(0, tk.END)
        if os.path.exists(self.csv_path):
            with open(self.csv_path, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if row['name'] == playlist_name:
                        songs = row['songs'].split(';') if row['songs'] else []
                        for song in songs:
                            instance.playlist_song_listbox.insert(tk.END, song)

    def add_playlist(self, instance, playlist_name):
        if not playlist_name or not playlist_name.strip():
            tk.messagebox.showwarning("Warning", "Playlist name cannot be empty.")
            return

        playlist_name = playlist_name.strip()

        if playlist_name in self.get_playlists():
            tk.messagebox.showwarning("Warning", f"The playlist '{playlist_name}' already exists.")
            return

        if not os.path.exists(self.csv_path):
            with open(self.csv_path, 'w', newline='') as csvfile:
                fieldnames = ['name', 'songs']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()

        with open(self.csv_path, 'a', newline='') as csvfile:
            fieldnames = ['name', 'songs']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'name': playlist_name, 'songs': ''})

        instance.load_playlists()

    def remove_playlist(self, instance, playlist_name):
        playlists = []
        if os.path.exists(self.csv_path):
            with open(self.csv_path, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if row['name'] != playlist_name:
                        playlists.append(row)
        with open(self.csv_path, 'w', newline='') as csvfile:
            fieldnames = ['name', 'songs']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(playlists)

    def add_song_to_playlist(self, playlist_name, song):
        if not os.path.exists(self.csv_path):
            tk.messagebox.showerror("Error", "Playlist file not found.")
            return

        with open(self.csv_path, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            rows = list(reader)

        updated = False
        for row in rows:
            if row['name'] == playlist_name:
                songs = row['songs'].split(';') if row['songs'] else []
                song_str = f"{song['name']} - {song['artist']}"
                if song_str not in songs:
                    songs.append(song_str)
                    row['songs'] = ';'.join(songs)
                    updated = True
                    break

        if updated:
            with open(self.csv_path, 'w', newline='') as csvfile:
                fieldnames = ['name', 'songs']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(rows)
        else:
            tk.messagebox.showinfo("Info", "Song is already in the playlist.")

    def remove_song_from_playlist(self, playlist_name, song_to_remove):
        if not os.path.exists(self.csv_path):
            tk.messagebox.showerror("Error", "Playlist file not found.")
            return

        with open(self.csv_path, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            rows = list(reader)

        updated = False
        for row in rows:
            if row['name'] == playlist_name:
                songs = row['songs'].split(';') if row['songs'] else []
                if song_to_remove in songs:
                    songs.remove(song_to_remove)
                    row['songs'] = ';'.join(songs)
                    updated = True
                    break

        if updated:
            with open(self.csv_path, 'w', newline='') as csvfile:
                fieldnames = ['name', 'songs']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(rows)
        else:
            tk.messagebox.showinfo("Info", "Song not found in the playlist.")
