#coding: utf-8

import pafy
from pydub import AudioSegment
import eyed3
from bs4 import BeautifulSoup
import requests

url = raw_input('Digite a URL da música: ')
audio = pafy.new(url).getbestaudio()
print(audio.title)
file = audio.download();
print()

mp3_audio = AudioSegment.from_file(file, audio.extension)
mp3_audio.export(audio.title + '.mp3', format='mp3')

mp3 = eyed3.load(audio.title + ".mp3")
mp3.tag.title = unicode(raw_input('Titulo: '))
mp3.tag.artist = unicode(raw_input('Artista: '))
mp3.tag.genre = unicode(raw_input('Genero: '))
mp3.tag.album = unicode(raw_input('Album: '))
mp3.tag.lyrics.set(unicode(raw_input('Letra: ')))
mp3.tag.save()

r = requests.get('https://www.letras.mus.br/rael-da-rima/ela-me-faz/')
soup = BeautifulSoup(r.text)
print soup.find(itemprop='description').find_all('p')
print soup.find_all('h1')[1].string
