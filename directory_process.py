import os
from main_process import *

# Access directory
def access_dir(folder_path, process):
    try:
        allFile = os.listdir(folder_path)
    except FileNotFoundError:
        return 1

    pr = Main_process(allFile=allFile, dirToAccess=folder_path)
    if(process == 0):
        pr.process_file()
    elif(process == 1):
        pr.rename_files()
    return 0
