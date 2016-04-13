from flask import Flask, render_template, request, send_from_directory
from download import Downloader
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/download", methods=['POST'])
def download(url='', title='', artist='', gender='', album=''):
    cleanMp3s()
    url = request.form['url']
    title = request.form['title']
    artist = request.form['artist']
    gender = request.form['gender']
    album = request.form['album']
    downloader = Downloader(url, title, artist, gender, album)
    path = downloader.download()
    return send_from_directory(os.path.abspath('.'), path, as_attachment=True)

def cleanMp3s():
    mp3s = filter(lambda file: file.endswith('.mp3'), os.listdir('.'))
    for mp3 in mp3s:
        os.remove(mp3)


if __name__ == "__main__":
    app.debug = True
    app.run()
