
# Compile python to exe
pyinstaller.exe --onefile --windowed --icon=icon.ico gui.py -n File-Organizer

# Remove build Folder
rm -r Build
