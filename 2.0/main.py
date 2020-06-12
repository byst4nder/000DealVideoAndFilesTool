from Config.api import getWorkDir
from Path.api import getFiles, removeFiles
from Video.api import isVideoDamaged



if __name__ == '__main__':
    err = []
    print(getWorkDir())
    for i in getFiles():
        b = isVideoDamaged(i)
        if b:
            err.append(i)
            print(i)
    print(err)
    # removeFiles(err)

