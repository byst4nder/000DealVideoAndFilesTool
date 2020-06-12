from os import remove


def removeFiles(files):
    for f in files:
        try:
            remove(f)
        except Exception as e:
            print(e)