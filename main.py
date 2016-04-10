#coding: utf-8

import pafy
from pydub import AudioSegment
import eyed3
from vagalume import lyrics

#fix encoding
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

def main():
    url = raw_input('Digite a URL da música: ')
    audio = pafy.new(url).getbestaudio()
    file = audio.download();

    convertToMp3(file, audio)

    print()
    title = raw_input('Titulo: ')
    artist = raw_input('Artista: ')
    gender = raw_input('Genero: ')
    album = raw_input('Album: ')

    editTags(audio, title, artist, gender, album)

def convertToMp3(file, audio):
    mp3_audio = AudioSegment.from_file(file, audio.extension)
    mp3_audio.export(audio.title + '.mp3', format='mp3')

def editTags(audio, title, artist, gender, album):
    mp3 = eyed3.load(audio.title + ".mp3")
    mp3.tag.title = unicode(title)
    mp3.tag.artist = unicode(artist)
    mp3.tag.genre = unicode(gender)
    mp3.tag.album = unicode(album)
    mp3.tag.lyrics.set(unicode(getLyrics(artist, title)))
    mp3.tag.save(version=eyed3.id3.ID3_V2_3)
    mp3.rename(artist + ' - ' + title)

def getLyrics(artist, title):
    return lyrics.find(artist, title).song.lyric

if __name__ == "__main__":
    main()
