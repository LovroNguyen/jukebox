from model.library_item import LibraryItem

library = []

def list_all():
    output = ""
    for key in library:
        item = library[key]
        output += f"{key}. {item.info()}\n"
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

def get_youtube_link(key):
    try:
        item = library[key]
        return item.youtube_link
    except KeyError:
        return None
