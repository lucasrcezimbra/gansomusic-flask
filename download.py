#coding: utf-8

import pafy
from pydub import AudioSegment
import eyed3
from vagalume import lyrics

#fix encoding
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class Downloader:
    def __init__(self, url, title, artist, gender, album):
        self.url = url
        self.title = title
        self.artist = artist
        self.gender = gender
        self.album = album

    def download(self):
        audio = pafy.new(self.url).getbestaudio()
        file = audio.download();

        self.__convertToMp3(file, audio)
        self.__editTags(audio)

    def __convertToMp3(self, file, audio):
        mp3_audio = AudioSegment.from_file(file, audio.extension)
        mp3_audio.export(audio.title + '.mp3', format='mp3')

    def __editTags(self, audio):
        mp3 = eyed3.load(audio.title + ".mp3")
        mp3.tag.title = unicode(self.title)
        mp3.tag.artist = unicode(self.artist)
        mp3.tag.genre = unicode(self.gender)
        mp3.tag.album = unicode(self.album)
        mp3.tag.lyrics.set(unicode(self.__getLyrics()))
        mp3.tag.save(version=eyed3.id3.ID3_V2_3)
        mp3.rename(self.artist + ' - ' + self.title)

    def __getLyrics(self):
        return lyrics.find(self.artist, self.title).song.lyric

if __name__ == "__main__":
    main()
