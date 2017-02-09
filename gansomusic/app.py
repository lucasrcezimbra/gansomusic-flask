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
    try:
        path = downloader.download()
    except IOError as e:
        return str(e)
    return send_from_directory(os.path.abspath('.'), path, as_attachment=True)

@app.route("/downloadlink", methods=['POST'])
def downloadlink(url='', title='', artist='', gender='', album=''):
    cleanMp3s()
    url = request.form['url']
    title = request.form['title']
    artist = request.form['artist']
    gender = request.form['gender']
    album = request.form['album']
    downloader = Downloader(url, title, artist, gender, album)
    path = downloader.download()
    dir = 'files/'
    if not os.path.exists(dir):
            os.makedirs(dir)
    newpath = dir + path
    os.rename(path, newpath)
    return '<a href="/' + newpath + '">' + newpath + '</a>'

@app.route("/files/<file>", methods=['GET'])
def files(file):
    return send_from_directory(os.path.abspath('files'), file, as_attachment=True)

def cleanMp3s():
    mp3s = filter(lambda file: file.endswith('.mp3'), os.listdir('.'))
    for mp3 in mp3s:
        os.remove(mp3)


if __name__ == "__main__":
    app.debug = True
    app.run()
