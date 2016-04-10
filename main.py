#coding: utf-8

import pafy
from pydub import AudioSegment
import eyed3
from vagalume import lyrics

#fix encoding
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

url = raw_input('Digite a URL da música: ')
audio = pafy.new(url).getbestaudio()
print(audio.title)
file = audio.download();
print()

mp3_audio = AudioSegment.from_file(file, audio.extension)
mp3_audio.export(audio.title + '.mp3', format='mp3')


titulo = raw_input('Titulo: ')
artista = raw_input('Artista: ')

mp3 = eyed3.load(audio.title + ".mp3")
mp3.tag.title = unicode(titulo)
mp3.tag.artist = unicode(artista)
mp3.tag.genre = unicode(raw_input('Genero: '))
mp3.tag.album = unicode(raw_input('Album: '))
letra = lyrics.find(artista, titulo).song.lyric
mp3.tag.lyrics.set(unicode(letra))
mp3.tag.save(version=eyed3.id3.ID3_V2_3)
mp3.rename(artista + ' - ' + titulo)
