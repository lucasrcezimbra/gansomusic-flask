import pafy
from pydub import AudioSegment

url = raw_input('Digite a URL da musica: ')
audio = pafy.new(url).getbestaudio()
file = audio.download();

mp3_audio = AudioSegment.from_file(file, audio.extension)
mp3_audio.export(audio.title + '.mp3', format='mp3')
