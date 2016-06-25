#coding: utf-8

import pafy
from pydub import AudioSegment
import os
from slugify import Slugify
from tagger import Tagger

#fix encoding
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class Downloader:
    def __init__(self, url, title, artist, genre, album):
        self.url = url
        self.title = title
        self.artist = artist
        self.genre = genre
        self.album = album
        self.slugify = Slugify(separator=' ', safe_chars='-.&:\'', translate=None)

    def download(self):
        audio = pafy.new(self.url).getbestaudio()
        file = audio.download()

        self.newtitle = self.slugify(audio.title)
        self.__convertToMp3(file, audio.extension)
        tagger = Tagger(self.newtitle + '.mp3', self.title, self.artist, self.genre, self.album)
        mp3 = tagger.editTags()
        return self.__renameFile(mp3)

    def __convertToMp3(self, file, extension):
        mp3_audio = AudioSegment.from_file(file, extension)
        mp3_audio.export(self.newtitle + '.mp3', format='mp3')

    def __renameFile(self, mp3):
        if self.newtitle != self.getName():
            if self.title and self.artist:
                if os.path.isfile(self.getPath()):
                    os.remove(self.getPath())
                mp3.rename(self.getName())
                return self.getPath()

        return self.newtitle + '.mp3'

    def getName(self):
        return self.slugify(self.artist+' - '+self.title)

    def getPath(self):
        return self.slugify(self.getName()+'.mp3')
