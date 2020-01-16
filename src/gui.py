import PySimpleGUI as sg
import sys
from process import *
from pathlib import Path
import os

def run_gui():
    sg.ChangeLookAndFeel('Reddit')
    layout = [
        [sg.Text('File Organizer', size=(35, 1), justification='center',
            font=("Arial", 20), relief=sg.RELIEF_GROOVE)],
        [sg.Text('_'  * 80)],
        [sg.Text('Choose Options', size=(20, 1), justification='left',
            font=("Arial", 15))],
        [sg.Checkbox('Rearrange', size=(10,1), key='_0_')],
        [sg.Checkbox('Rename', size=(10,1), key='_1_'),
            sg.InputText('New_Filename', key='_newName_')],
        [sg.Text('_'  * 80)],
        [sg.InputText('Choose A Folder', key='_folder_'), sg.FolderBrowse()],
        [sg.Submit(tooltip='Click to submit this window'), sg.Cancel()]
    ]
    path = Path('.').parent.absolute()
    path = os.path.join(path, 'dist', 'icon.ico')
    window = sg.Window(
        'File Organizer', layout, default_element_size=(40, 1),
        grab_anywhere=False, icon=path
    )
    event, values = window.read()
    chosen = check_options_chosen(values)
    if(chosen == -1):
        return values, chosen
    return values, chosen

def check_options_chosen(values):
    options_chosen = False
    if(values['_0_'] == True):
        return 0
    if(values['_1_'] == True):
        return 1
    if(options_chosen == False):
        return -1

if __name__ == '__main__':
    values, process_chosen = run_gui()
    if(process_chosen != -1):
        err = access_dir(values, process_chosen)
        if(err != 0):
            sg.popup("Process error")
        else:
            sg.popup("Done All!")
