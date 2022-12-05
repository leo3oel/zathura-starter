import subprocess as sub

def getFolders(path):
    command_result = sub.run(["ls", path], capture_output=True, encoding='UTF-8')
    str_result = command_result.stdout

    list = []
    temp = ""

    # Make list with Folder & Filenames
    for i in range(len(str_result)):
        if str_result[i] == "\n":
            list.append(temp)
            temp = ""
        else:
            temp += str_result[i]

    folder = [".."]

    # Separate files with ending from folders
    for item in list:
        for i in range(len(item)):
            if item[i] == ".":
                break
            else:
                if i == len(item)-1:
                    folder.append(item)

    folder.sort()
    return(folder)

# return files list
def getFiles(path):
    command_result = sub.run(["ls", path], capture_output=True, encoding='UTF-8')
    str_result = command_result.stdout

    list = []
    temp = ""

    # Make list with Folder & Filenames
    for i in range(len(str_result)):
        if str_result[i] == "\n":
            list.append(temp)
            temp = ""
        else:
            temp += str_result[i]

    pdfs = []

    # Separate files with ending from folders
    for item in list:
        for i in range(len(item)):
            if item[i] == ".":
                pdfs.append(item)
                break
            else:
                if i == len(item)-1:
                    break

    # count unnecessary items
    delete = []
    for i in range(len(pdfs)):
        item = pdfs[i]
        if item[-4:] == ".pdf":
            pass
        else:
            delete.append(i)

    # delete unnecessary items
    offset = 0
    for i in range(len(delete)):
        pdfs.pop(delete[i]-offset)
        offset+=1

    pdfs.sort()

    return(pdfs)

    def openFile():
        sub.run(["ls", path], capture_output=True, encoding='UTF-8')