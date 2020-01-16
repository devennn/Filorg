
# Compile python to exe
pyinstaller.exe --onefile --windowed --icon=dist/icon.ico gui.py -n Filorg

# Remove build Folder
rm -r Build
