import os
from Config.api import getWorkDir

files = []
dirs = []


def init():
    files.clear()
    dirs.clear()
    for root, ds, fs in os.walk(getWorkDir()):
        for i in fs:
            temp = root + '\\' + i
            files.append(temp)
        for i in ds:
            temp = root + '\\' + i
            dirs.append(temp)


def getFiles(initFlag=True):
    if initFlag:
        init()
    return files


def getDirs(initFlag=True):
    if initFlag:
        init()
    return dirs
