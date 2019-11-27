import os

# Create folder based on file extension and move all file into folder
def process_file(dirToAccess, allFile):
    for file in allFile:
        dir = os.path.join(dirToAccess, file)
        filename, file_extension = os.path.splitext(dir)
        if(file_extension != ""):
            file_extension = file_extension.strip('.')
            newFileName = ("%s_file" %file_extension)
            newFilePath = os.path.join(dirToAccess, newFileName)
            try:
                os.mkdir(newFilePath)
            except FileExistsError:
                pass
            newFilePath = os.path.join(newFilePath, file)
            os.rename(dir, newFilePath)


# Access directory
def access_dir(folder_path):
    try:
        allFile = os.listdir(folder_path)
    except FileNotFoundError:
        return 1
    process_file(folder_path, allFile)
    return 0
