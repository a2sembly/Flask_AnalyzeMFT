import hashlib
import os
import subprocess
from subprocess import Popen, PIPE
from subprocess import check_output
root_dir = os.path.dirname(os.path.abspath(__file__))

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
    file_ = os.path.basename(filename) #파일명만 추출
    print(filename)
    subp_arg = root_dir + '\\test.bat ' + filename + ' ' + file_
    print(subp_arg)
    subprocess.call(subp_arg)