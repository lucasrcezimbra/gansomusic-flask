#coding: utf-8

from vagalume import lyrics
import eyed3

#fix encoding
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class Tagger:
    def __init__(self, path, title, artist, genre, album):
        self.path = path
        self.title = title
        self.artist = artist
        self.genre = genre
        self.album = album

    def editTags(self):
        mp3 = eyed3.load(self.path)
        mp3.tag.title = unicode(self.title)
        mp3.tag.artist = unicode(self.artist)
        mp3.tag.genre = unicode(self.genre)
        mp3.tag.album = unicode(self.album)
        mp3.tag.lyrics.set(unicode(self.__getLyrics()))
        mp3.tag.save(version=eyed3.id3.ID3_V2_3)
        return mp3

    def __getLyrics(self):
        try:
            result = lyrics.find(self.artist, self.title)
            if result.is_not_found():
                return ''
            else:
                return result.song.lyric
        except:
            return ''
