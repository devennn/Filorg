import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")
import re
from main_process import *

# Access directory
def access_dir(values, process):
    folder_path = values['_folder_']
    newName = values['_newName_']
    try:
        allFile = os.listdir(folder_path)
    except FileNotFoundError:
        return -1

    if(process == 0):
        pr = Arrange(allFile=allFile, dirToAccess=folder_path)
        pr.process_file()
    elif(process == 1):
        err = check_rename_newname(str=newName)
        if(err == 0):
            pr = Rename(allFile=allFile, dirToAccess=folder_path)
            pr.rename_files(newName=newName)
        else :
            return -1
    return 0

# Check if string entered containing forbidden characters on windows
def check_rename_newname(str):
    regex = re.compile('[<>:"/\|?*]')
    if(regex.search(str) == None):
        return 0
    else:
        return -1
