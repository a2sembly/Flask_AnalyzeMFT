from celery import Celery
import hashlib
import os
import pandas as pd
import shutil
import subprocess
import time
from flask import render_template, request, make_response, jsonify, Flask, abort, redirect, flash, url_for
import convert
import csv
import pathlib

root_dir = os.path.dirname(os.path.abspath(__file__))
BROKER_URL = 'redis://192.168.22.129:6379/0'
CELERY_RESULT_BACKEND = 'redis://192.168.22.129:6379/0'
app = Celery('charts', broker=BROKER_URL, backend=CELERY_RESULT_BACKEND)

@app.task
def parser_extension(file):
    f = open(file,'r',encoding='latin1')
    rdr = csv.reader(f)
    ext_list = []
    ext_count = []
    count = {}

    for line in csv:
        if line[3] == 'Folder':
            continue
        
        path = pathlib.Path(line[7])
        ext = ''.join(path.suffixes)
        if ext in "/" or ext in "Users" or ext in "AppData":
            continue
        else:
            ext_count.append(ext)

    for i in ext_count:
        try: count[i] += 1
        except: count[i]=1

    count = sorted(count.items(), key=lambda x:x[1], reverse=True)
    print(count[1:11])
    #f.close()
