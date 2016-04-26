#coding: utf-8

import unittest
import os.path
import eyed3
from gansomusic.download import Downloader

class DownloaderTest(unittest.TestCase):
    def setUp(self):
        self.url = '_pbR605pYo8'
        self.title = 'título'
        self.artist = 'artista'
        self.genre = 'genero'
        self.album = 'album'
        self.video_title = 'O menor video do youtube-Han...'
        self.downloader = Downloader(self.url, self.title, self.artist, self.genre, self.album)
        self.mp3_path = self.downloader.download()

    def test(self):
        self.assertIsInstance(self.downloader, Downloader)

    def test_remove_downloaded_audio(self):
        self.assertFalse(os.path.isfile('O menor video do youtube-Han....m4a'))
        self.assertFalse(os.path.isfile(self.video_title+'.m4a'))

    def test_convert_to_mp3(self):
        self.assertTrue(os.path.isfile('artista - título.mp3'))
        self.assertTrue(os.path.isfile(self.artist+' - '+self.title+'.mp3'))

    def test_getname_and_getpath(self):
        name = self.artist+' - '+self.title
        path = self.artist+' - '+self.title+'.mp3'
        path2 = self.downloader.getName()+'.mp3'

        self.assertEqual(self.downloader.getName(), name)
        self.assertEqual(self.downloader.getPath(), path)
        self.assertEqual(self.downloader.getPath(), path2)

    def test_delete_existing_mp3_file(self):
        self.downloader.download()
        self.downloader.download()

    def test_not_rename_with_dont_have_title_and_artist(self):
        self.downloader = Downloader(self.url, '', self.artist, self.genre, self.album)
        self.downloader.download()
        self.assertTrue(os.path.isfile(self.video_title+'.mp3'))

        self.downloader = Downloader(self.url, self.title, '', self.genre, self.album)
        self.downloader.download()
        self.assertTrue(os.path.isfile(self.video_title+'.mp3'))

        self.downloader = Downloader(self.url, '', '', self.genre, self.album)
        self.downloader.download()
        self.assertTrue(os.path.isfile(self.video_title+'.mp3'))

    def test_set_correct_tags(self):
        mp3 = eyed3.load(self.mp3_path)
        self.assertEqual(self.title, mp3.tag.title)
        self.assertEqual(self.artist, mp3.tag.artist)
        self.assertEqual(self.genre, mp3.tag.genre.name)
        self.assertEqual(self.album, mp3.tag.album)

    def test_set_id3_version2_3(self):
        mp3 = eyed3.load(self.mp3_path)
        self.assertEqual(mp3.tag.version, eyed3.id3.ID3_V2_3)

    def test_set_correct_lyric(self):
        self.downloader = Downloader(self.url, '', '', self.genre, self.album)
        mp3_path = self.downloader.download()
        mp3 = eyed3.load(mp3_path)
        self.assertEqual('', mp3.tag.lyrics[0].text)

        self.downloader = Downloader(self.url, 'Ela Me Faz', 'Rael', self.genre, self.album)
        mp3_path = self.downloader.download()
        mp3 = eyed3.load(mp3_path)
        self.assertNotEqual('', mp3.tag.lyrics[0].text)

if __name__ == "__main__":
    unittest.main()
