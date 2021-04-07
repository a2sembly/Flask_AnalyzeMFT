from flask import render_template, request, make_response, jsonify, Flask, abort, redirect
from werkzeug.utils import secure_filename
import os
import hashlib
from etc import *
import time

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['full_filepath'] = ''

@app.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        if request.form['type'] == 'Upload_file':
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
            app.config['full_filepath'] = full_filepath
            print(app.config['full_filepath'])
            return res
        elif request.form['type'] == 'Analyze_file':
            print("analyze")
            analyze()
            

    return render_template("/test.html")
    
def analyze():
        print(app.config['full_filepath'])
        while(1):
            val = Checkfile(app.config['full_filepath'])
            if val == 'progress':
               return render_template("/" + app.config['full_filepath'] + ".html")
            elif val == 'inprogress':
               continue
            else:
               get_shell_script_output_using_communicate(app.config['full_filepath'])


@app.route("/Loading", methods=["GET", "POST"])
def load():
    return render_template("/Loading.html")

@app.errorhandler(404)
def page_not_found(error):
    return render_template('/404.html'), 404

@app.errorhandler(401)
def error_401(error):
    return render_template('/401.html'), 401

@app.errorhandler(405)
def error_405(error):
    return render_template('/405.html'), 405

if __name__ == '__main__':
    #서버 실행
   app.run(debug = True)
