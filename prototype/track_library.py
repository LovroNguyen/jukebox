from library_item import LibraryItem

library = {}
library["01"] = LibraryItem("On The Ground", "Rosé", 5, "https://www.youtube.com/watch?v=CKZvWhCqx1s")
library["02"] = LibraryItem("Rise", "Jonas Blue, Jack & Jack", 4, "https://www.youtube.com/watch?v=Dh-ULbQmmF8")
library["03"] = LibraryItem("Legends Never Die", "League of Legends", 4, "https://www.youtube.com/watch?v=r6zIGXun57U")
library["04"] = LibraryItem("Shape of You", "Ed Sheeran", 1, "https://www.youtube.com/watch?v=JGwWNGJdvx8")
library["05"] = LibraryItem("Someone Like You", "Adele", 3, "https://www.youtube.com/watch?v=hLQl3WQQoQ0")
library["06"] = LibraryItem("Attention", "New Jeans", 5, "https://www.youtube.com/watch?v=U7mPqycQ0tQ")
library["07"] = LibraryItem("APT", "Rosé, Bruno Mars", 5, "https://www.youtube.com/watch?v=ekr2nIex040")
library["08"] = LibraryItem("Die with a Smile", "Lady Gaga, Bruno Mars", 5, "https://www.youtube.com/watch?v=example_link_die_with_a_smile")

def list_all():
    output = ""
    for key in library:
        item = library[key]
        output += f"{key} {item.info()}\n"
    return output

def get_name(key):
    try:
        item = library[key]
        return item.name
    except KeyError:
        return None

def get_artist(key):
    try:
        item = library[key]
        return item.artist
    except KeyError:
        return None

def get_rating(key):
    try:
        item = library[key]
        return item.rating
    except KeyError:
        return -1

def set_rating(key, rating):
    try:
        item = library[key]
        item.rating = rating
    except KeyError:
        return

def get_play_count(key):
    try:
        item = library[key]
        return item.play_count
    except KeyError:
        return -1

def increment_play_count(key):
    try:
        item = library[key]
        item.play_count += 1
    except KeyError:
        return

def get_youtube_link(key):
    try:
        item = library[key]
        return item.youtube_link
    except KeyError:
        return None
