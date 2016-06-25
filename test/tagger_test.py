#coding: utf-8

from pydub import AudioSegment
import unittest
import os.path
import eyed3
import pafy
from gansomusic.tagger import Tagger 

class TaggerTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        path = 'audio_test.mp3'
        #download an audio for test
        audio = pafy.new('_pbR605pYo8').getbestaudio()
        file = audio.download()
        mp3_audio = AudioSegment.from_file(file, audio.extension)
        mp3_audio.export(path, format='mp3')

        self.path = path
        self.title = 'título'
        self.artist = 'artista'
        self.genre = 'genero'
        self.album = 'album'
        self.tagger = Tagger(self.path, self.title, self.artist, self.genre, self.album)
        self.tagger.editTags()

    @classmethod
    def tearDownClass(cls):
        audios = filter(lambda file: file.endswith(('.mp3','.webm')), os.listdir('.'))
        for audio in audios:
            os.remove(audio)

    def test(self):
        self.assertIsInstance(self.tagger, Tagger)

    def test_set_correct_tags(self):
        mp3 = eyed3.load(self.path)
        self.assertEqual(self.title, mp3.tag.title)
        self.assertEqual(self.artist, mp3.tag.artist)
        self.assertEqual(self.genre, mp3.tag.genre.name)
        self.assertEqual(self.album, mp3.tag.album)

    def test_set_id3_version2_3(self):
        mp3 = eyed3.load(self.path)
        self.assertEqual(mp3.tag.version, eyed3.id3.ID3_V2_3)

    def test_set_correct_lyric(self):
        mp3 = eyed3.load(self.path)
        self.assertEqual('', mp3.tag.lyrics[0].text)

        tagger = Tagger(self.path, 'Ela me Faz', 'Rael', self.genre, self.album)
        tagger.editTags()
        mp3 = eyed3.load(self.path)
        self.assertNotEqual('', mp3.tag.lyrics[0].text)

        #reset tagged audio, remove 'Ela me Faz' and 'Rael'
        self.tagger = Tagger(self.path, self.title, self.artist, self.genre, self.album)
        self.tagger.editTags()

if __name__ == "__main__":
    unittest.main()
