from os.path import splitext
import cv2
from moviepy.editor import VideoFileClip

suffixes = ['.mp4', '.avi', '.vob', '.mkv', '.VOB', '.flv', '.wmv', '.mov', '.rmvb', '.ts', '.mpg', '.webm']


def isVideo(file):
    if not splitext(file)[1].lower() in suffixes:
        return False
    try:
        fps = cv2.VideoCapture(file).get(cv2.CAP_PROP_FPS)
        print(fps)
        if fps <= 0:
            VideoFileClip(file)
    except Exception as e:
        print(e)
        return False
    return True


def isVideoDamaged(file):
    if not splitext(file)[1].lower() in suffixes:
        return False
    return not isVideo(file)
