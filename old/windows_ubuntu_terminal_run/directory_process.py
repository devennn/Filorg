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
            print(dir + ":::" + newFilePath)
            os.rename(dir, newFilePath)


# Access directory
def access_dir(input, userName):
    # r is to produce a raw string
    print(userName)
    base = os.path.join("/mnt/c/Users/", userName)
    print(base)
    options = [
        r"/Desktop/",
        r"/Documents/",
        r"/Downloads/"
    ]
    dirToAccess = base + options[input]
    print(dirToAccess)
    try:
        allFile = os.listdir(dirToAccess)
    except FileNotFoundError:
        print("File Not found")
        return 1
    process_file(dirToAccess, allFile)
    return 0


# Entry get input from gui
def get_gui_input(arg):
    for value in arg:
        try:
            buf = int(value)
            print(buf, userName)
            err = access_dir(buf, arg[0])
            if(err != 0):
                return 1
        except ValueError:
            continue

    return 0