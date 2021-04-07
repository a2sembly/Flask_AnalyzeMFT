import hashlib
import os
import subprocess
from subprocess import Popen, PIPE
from subprocess import check_output
import pandas as pd
root_dir = os.path.dirname(os.path.abspath(__file__))


def Checkfile(file_):
    csv_ = file_ + '.csv'
    html = file_ + '.html'
    file = os.path.isfile(csv_)
    html_ = os.path.isfile(html)
    print(html_)
    print(csv_)
    if file == True:
        if html == True:
            print(os.path.getsize(csv_))
            if os.path.getsize(csv_) > 10 :
                csv_to_html(csv_)
                return 'progress'
        else:
            csv_to_html(csv_)
            return 'inprogress'
    else:
        return 'Fail'

def csv_to_html(file_CSV):
    df = pd.read_csv(root_dir + '\\' + file_CSV)
    r_name = os.path.basename(file_CSV)
    df.to_html(r_name.replace('.csv','.html'))

def calc_file_hash(data):
    hash = hashlib.md5(data).hexdigest()
    return hash

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)

def get_shell_script_output_using_communicate(filename):
    # file_ = os.path.basename(filename) #파일명만 추출
    # print(filename)
    subp_arg = root_dir + '\\test.bat ' + filename + ' ' + filename
    print(subp_arg)
    subprocess.call(subp_arg)