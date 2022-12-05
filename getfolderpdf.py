import subprocess as sub

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

    folder = []
    pdfs = []

    # Separate files with ending from folders
    for item in list:
        for i in range(len(item)):
            if item[i] == ".":
                pdfs.append(item)
                break
            else:
                if i == len(item)-1:
                    folder.append(item)

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

    folder.sort()
    pdfs.sort()

    for item in pdfs:
        folder.append(item)

    return(folder)