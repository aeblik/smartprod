from flask import Flask, request, render_template, redirect, url_for

#####
from storage import upload_to_minio
from database import insert_file_metadata, get_all_files

app = Flask(__name__)

@app.route('/')
def index():
    files = get_all_files()
    return render_template('upload.html', files=files)

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    if file:
        file_url = upload_to_minio(file)
        insert_file_metadata(file.filename, file_url)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')