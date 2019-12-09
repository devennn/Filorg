import os

class Main_process:

    def __init__(self, allFile=[], dirToAccess="", ext="", newName="new"):
        self.allFile = allFile
        self.dirToAccess = dirToAccess
        self.ext = ext
        self.newName = newName

    # Create folder based on file extension and move all file into folder
    def process_file(self):
        for _file in self.allFile:
            _dir = os.path.join(self.dirToAccess, _file)
            _filename, _file_extension = os.path.splitext(_dir)
            if(_file_extension != ""):
                _file_extension = _file_extension.strip('.')
                _newFileName = ("%s_file" %_file_extension)
                _newFilePath = os.path.join(self.dirToAccess, _newFileName)
                try:
                    os.mkdir(_newFilePath)
                except FileExistsError:
                    pass
                _newFilePath = os.path.join(_newFilePath, _file)
                os.rename(_dir, _newFilePath)

    def rename_files(self):
        _i = 1;
        _dir = self.dirToAccess + str("/")
        for _file in self.allFile:
            _filename, _file_extension = os.path.splitext(_file)
            _file = dir + _file
            _newName = dir + str('rename_{}'.format(_i)) + _file_extension
            os.rename(_file, _newName)
            _i += 1

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
