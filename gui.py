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

def choose_process():

    layout = [
        [sg.Text('What to do with them:')],
        [sg.Checkbox('Rearrange'), sg.Checkbox('Rename')],
        [sg.OK()]
    ]
    windows = sg.Window('Choose Process').Layout(layout)
    button, values = windows.Read()
    chosen = [i for i in range(len(values)) if values[i] == True]
    return chosen[0]

def main():
    folder_path = run_gui()
    chosen = choose_process()
    err = access_dir(folder_path, chosen)
    if(err != 0):
        sg.popup("Process error")
    else:
        sg.popup("Done All!")

if __name__ == '__main__':
    main()
