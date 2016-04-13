#coding: utf-8

import pafy
from pydub import AudioSegment
import eyed3
from vagalume import lyrics
import os

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
        file = audio.download()

        self.__convertToMp3(file, audio)
        os.remove(file)
        return self.__editTags(audio)

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
        return self.__renameFile(mp3, audio)

    def __renameFile(self, mp3, audio):
        if self.title and self.artist:
            if os.path.isfile(self.getPath()):
                os.remove(self.getPath())
            mp3.rename(self.getName())
            return self.getPath()
        else:
            return audio.title + '.mp3'

    def getName(self):
        return self.artist+' - '+self.title

    def getPath(self):
        return self.getName()+'.mp3'

    def __getLyrics(self):
        result = lyrics.find(self.artist, self.title)
        if result.is_not_found():
            return ''
        else:
            return result.song.lyric


if __name__ == "__main__":
    main()
