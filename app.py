from flask import Flask, render_template, request, send_from_directory
from download import Downloader

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/download", methods=['POST'])
def download(url='', title='', artist='', gender='', album=''):
    url = request.form['url']
    title = request.form['title']
    artist = request.form['artist']
    gender = request.form['gender']
    album = request.form['album']
    print url+' '+title+' '+ artist+' '+gender+' '+album
    downloader = Downloader(url, title, artist, gender, album)
    downloader.download()
    return send_from_directory('.', downloader.getPath())

if __name__ == "__main__":
    app.debug = True
    app.run()
