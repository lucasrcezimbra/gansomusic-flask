#coding: utf-8

import unittest
import os.path
from rangelmusic.download import Downloader

class DownloaderTest(unittest.TestCase):
    def setUp(self):
        self.url = '_pbR605pYo8'
        self.title = 'título'
        self.artist = 'artista'
        self.gender = 'genero'
        self.album = 'album'
        self.downloader = Downloader(self.url, self.title, self.artist, self.gender, self.album)

    def test(self):
        self.assertTrue(isinstance(self.downloader, Downloader))

    def test_remove_downloaded_audio(self):
        self.downloader.download()
        self.assertFalse(os.path.isfile('O menor video do youtube-Han....m4a'))

    def test_convert_to_mp3(self):
        self.downloader.download()
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



if __name__ == "__main__":
    unittest.main()
