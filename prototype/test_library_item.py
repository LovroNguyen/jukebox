import pytest
from library_item import LibraryItem


def test_library_item_info():
    item = LibraryItem("Test Track", "Test Artist", 5)
    assert item.info() == "Test Track by Test Artist, Rating: 5"

def test_library_item_stars():
    item = LibraryItem("Movie Title", "Director Name", rating=5)
    assert item.stars() == "*****"

def test_library_item_update_rating():
    item = LibraryItem("Test Track", "Test Artist", 3)
    item.rating = 4
    assert item.rating == 4

def test_library_item_play_count():
    item = LibraryItem("Movie Title", "Director Name")
    item.play_count += 1
    assert item.play_count == 1

def test_library_item_creation():
    item = LibraryItem("Test Track", "Test Artist", 5)
    assert item.name == "Test Track"
    assert item.artist == "Test Artist"
    assert item.rating == 5

def test_library_item_invalid_rating():
    with pytest.raises(ValueError):
        LibraryItem("Test Track", "Test Artist", 6)

def test_library_item_invalid_update_rating():
    item = LibraryItem("Test Track", "Test Artist", 3)
    with pytest.raises(ValueError):
        item.rating = 6

def test_library_item_str():
    item = LibraryItem("Test Track", "Test Artist", 5)
    assert str(item) == "Test Track by Test Artist, Rating: 5"

if __name__ == "__main__":
    pytest.main()