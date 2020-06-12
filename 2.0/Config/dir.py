import os

workDir = os.getcwd()
workDir = r'H:\OneDrive - revolutionize B2C bandwidth\视频教程\Adobe\AU+AE+PR+C4D_2019\PR2019\2.中级教程\04.视频特效及转场处理\教程素材'


def getWorkDir():
    return workDir


def setWorkDir(dir):
    global workDir
    workDir = dir
