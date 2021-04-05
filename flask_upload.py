from flask import render_template, request, make_response, jsonify, Flask
from werkzeug.utils import secure_filename
import os
import hashlib
from etc import *
import time

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
    
#C:\Users\rever\AppData\Local\Programs\Python\Python37\python.exe
#파일 업로드 처리
@app.route('/fileUpload', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      #저장할 경로 + 파일명
      f.save(secure_filename(f.filename))
      return 'uploads 디렉토리 -> 파일 업로드 성공!'

@app.route("/upload", methods=["GET", "POST"])
def upload_video():
    if request.method == "POST":

        file = request.files["file"]
        print("File uploaded")
        res = make_response(jsonify({"message": "File uploaded"}), 200)
        hash_val = calc_file_hash(file.read())
        createFolder(os.path.join(app.config['UPLOAD_FOLDER'], hash_val))
        full_dirpath = os.path.join(app.config['UPLOAD_FOLDER'], hash_val)
        print(full_dirpath)
        time.sleep(1)
        full_filepath = full_dirpath + '\\' + secure_filename(hash_val)
        file.seek(0) # hash 계산으로 file offest 위치가 마지막이므로 처음으로 옮김
        file.save(full_filepath)
        print(full_filepath)
        get_shell_script_output_using_communicate(full_filepath)
        return res

    return render_template("/test.html")

if __name__ == '__main__':
    #서버 실행
   app.run(debug = True)
