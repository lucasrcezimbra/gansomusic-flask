import pafy

url = raw_input('Digite a URL da musica: ')
audio = pafy.new(url).getbestaudio()
audio.download();
