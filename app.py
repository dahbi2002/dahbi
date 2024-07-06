from flask import Flask, render_template, request, send_file
import os
import pytube

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    url = request.form['url']
    yt = pytube.YouTube(url)
    stream = yt.streams.get_highest_resolution()
    video_path = stream.download(output_path='downloads')

    return send_file(video_path, as_attachment=True)

if __name__ == '__main__':
    if not os.path.exists('downloads'):
        os.makedirs('downloads')
    app.run(debug=True)
