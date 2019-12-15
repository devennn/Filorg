import PySimpleGUI as sg
import sys
from directory_process import *

def run_gui():
    sg.ChangeLookAndFeel('Reddit')
    layout = [
        [sg.Text('File Organizer 1.0', size=(30, 1), justification='center',
            font=("Arial", 25), relief=sg.RELIEF_GROOVE)],
        [sg.Text('_'  * 80)],
        [sg.Text('Choose Options', size=(20, 1), justification='left',
            font=("Arial", 15))],
        [sg.Checkbox('Rearrange', size=(10,1)),  sg.Checkbox('Rename')],
        [sg.Text('_'  * 80)],
        [sg.InputText('Choose A Folder'), sg.FolderBrowse()],
        [sg.Submit(tooltip='Click to submit this window'), sg.Cancel()]
    ]

    window = sg.Window(
        'File Organizer 1.0', layout, default_element_size=(40, 1),
        grab_anywhere=False, icon='icon.ico'
    )
    event, values = window.read()

    ## For debugging. Comment if for actual app
    # sg.popup('The results of the window.',
    #             'Value 1', values[0],
    #             'Value 2', values[1],
    #             'Value 3', values[2])

    # Only check up to values 1 because values 2 is the folder path
    chosen = [i for i in range(len(values) - 1) if values[i] == True]
    if not values[2]:
        # sg.popup("Cancel", "No Folder supplied")
        raise SystemExit("Cancelling: no Folder supplied")
    try:
        return values[2], chosen[0]
    except IndexError:
        raise SystemExit("Cancelling: Index Error")

def main():
    folder_path, process_chosen = run_gui()
    err = access_dir(folder_path, process_chosen)
    if(err != 0):
        sg.popup("Process error")
    else:
        sg.popup("Done All!")

if __name__ == '__main__':
    main()
