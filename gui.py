import PySimpleGUI as sg
import directory_process as dp

layout = [
    [sg.Text('eg: Directory: c/Users/mypc | Username: mypc')],
    [sg.Text('Enter Username:')],
    [sg.Input(key='-IN-')],
    [sg.Text('Choose Folder to organize:')],
    [sg.Checkbox('Desktop', size=(10,1)),
        sg.Checkbox('Documents', size=(10,1)),
        sg.Checkbox('Downloads', size=(10,1))],
    [sg.Button('Start organize'), sg.Button('Exit'),
        sg.Text('', size=(15,1), key='-OUTPUT-')],
]

window = sg.Window('File Organizer', layout)
arg = [
    "Empty",
    "Empty",
    "Empty",
    "Empty",
]

while True:  # Event Loop
    event, values = window.Read()
    if event is None or event == 'Exit':
        break
    if event == 'Start organize':
        # Get input
        arg[0] = values['-IN-']
        for i in values:
            if(values[i] == True):
                arg[i+1] = i
        # Run Engine Here
        status = dp.get_gui_input(arg)
        # Engine return value
        if(status == 0):
            window['-OUTPUT-'].Update("Done...")
        else:
            window['-OUTPUT-'].Update("Process Error...")
        # Clear arg
        for i in range(4):
            arg[i] = "Empty"
window.Close()
