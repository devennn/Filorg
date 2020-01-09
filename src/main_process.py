import os
from logs.set_logger import set_logger

logger = set_logger(level='Info')

class Arrange:

    def __init__(self, allFile=[], dirToAccess="", ext=""):
        self.allFile = allFile
        self.dirToAccess = dirToAccess
        self.ext = ext

    # Create folder based on file extension and move all file into folder
    def process_file(self):
        logger.info('=== Start process_file ===')
        for file in self.allFile:
            dir = os.path.join(self.dirToAccess, file)
            filename, file_extension = os.path.splitext(dir)
            if(file_extension != ""):
                file_extension = file_extension.strip('.')
                _newFileName = ("%s_file" %file_extension)
                _newFilePath = os.path.join(self.dirToAccess, _newFileName)
                try:
                    os.mkdir(_newFilePath)
                except FileExistsError:
                    pass
                _newFilePath = os.path.join(_newFilePath, file)
                os.rename(dir, _newFilePath)

class Rename:

    def __init__(self, allFile=[], dirToAccess="", ext=""):
        self.allFile = allFile
        self.dirToAccess = dirToAccess
        self.ext = ext

    # Renaming files
    def rename_files(self, newName):
        logger.info('=== Start rename_files ===')
        _i = 1;
        dir = self.dirToAccess + "/"
        err = self._check_requirements(path=dir)
        if(err == -1):
            return -1
        for file in self.allFile:
            filename, file_extension = os.path.splitext(file)
            file = dir + file
            _newName = dir + str('{}_{}'.format(newName, _i)) + file_extension
            os.rename(file, _newName)
            _i += 1

    def _check_requirements(self, path):
        if(os.path.exists(path) == True):
            return
        else:
            return -1
