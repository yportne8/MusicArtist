import tracemalloc
import unittest
from music_artist.artist import MusicArtist


NAME = "Twenty One Pilots"
tracemalloc.start() # unclosed socket in ytmusicapi pkg


class TestYouTubeMusic(unittest.TestCase):
    
    def test_albums(self):
        artist = MusicArtist(NAME)
        albums = artist.albums()
        self.assertTrue(type(albums) == list)

    def test_singles(self):
        artist = MusicArtist(NAME)
        singles = artist.singles()
        self.assertTrue(type(singles) == list)

class TestITunes(unittest.TestCase):
    
    def test_genres(self):
        artist = MusicArtist(NAME)
        genres = artist.genres()
        self.assertTrue(type(genres) == list)

    def test_tophits(self):
        artist = MusicArtist(NAME)
        tophits = artist.tophits()
        self.assertTrue(type(tophits) == list)


class TestAllMusic(unittest.TestCase):
    
    def test_similar(self):
        artist = MusicArtist(NAME)
        similar_artists = artist.similar()
        self.assertTrue(type(similar_artists) == list)


    
if __name__ == '__main__':
    unittest.main()