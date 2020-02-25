import os

from logs.set_logger import set_logger
logger = set_logger(level='Info')

class Arrange:

    def __init__(self, allFile=[], dirToAccess=""):
        logger.info('=== Initializing class: Arrange ===')
        self.allFile = allFile
        self.dirToAccess = dirToAccess

    # Create folder based on file extension and move all file into folder
    def process_file(self):
        logger.info('=== Start process_file ===')
        for file in self.allFile:
            dir = os.path.join(self.dirToAccess, file)
            filename, file_extension = os.path.splitext(dir)
            if(file_extension != ""):
                file_extension = file_extension.strip('.')
                new_fname = ("%s_file" %file_extension)
                new_fpath = os.path.join(self.dirToAccess, new_fname)
                try:
                    os.mkdir(new_fpath)
                except FileExistsError:
                    pass
                new_fpath = os.path.join(new_fpath, file)
                os.rename(dir, new_fpath)

class Rename:

    def __init__(self, allFile=[], dirToAccess=""):
        logger.info('=== Initializing class: Rename ===')
        self.allFile = allFile
        self.dirToAccess = dirToAccess

    # Renaming files
    def rename_files(self, new_name):
        logger.info('=== Start rename_files ===')
        i = 1;
        dir = self.dirToAccess + "/"
        for file in self.allFile:
            filename, file_extension = os.path.splitext(file)
            file = os.path.join(dir, file)
            new_path = dir + str('{}_{}'.format(new_name, i)) + file_extension
            os.rename(file, new_path)
            logger.info('=== os.rename: {} -> {}'.format(file, new_path))
            i += 1
