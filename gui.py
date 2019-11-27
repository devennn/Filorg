import PySimpleGUI as sg
import sys
from directory_process import *

def run_gui():
    if len(sys.argv) == 1:
        folder_path = sg.PopupGetFolder('Select Folder to Open')
    else:
        folder_path = sys.argv[1]

    if not folder_path:
        sg.popup("Cancel", "No Folder supplied")
        raise SystemExit("Cancelling: no Folder supplied")
    else:
        sg.popup('Folder Path: \n', folder_path)

    return folder_path

def main():
    folder_path = run_gui()
    err = access_dir(folder_path)
    if(err != 0):
        sg.popup("Process error")

if __name__ == '__main__':
    main()
