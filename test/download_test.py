#coding: utf-8

import unittest
from rangelmusic.download import Downloader

class DownloaderTest(unittest.TestCase):
    def setUp(self):
        self.downloader = Downloader('pbR605pYo8', 'tituló: O menor video', 'artista: desconhecido', 'genero: sl', 'album: nao tem')

    def test(self):
        self.assertTrue(isinstance(self.downloader, Downloader))


if __name__ == "__main__":
    unittest.main()
