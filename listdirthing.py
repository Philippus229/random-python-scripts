import os
from tkinter.filedialog import askdirectory

def printPart(path, depth):
    for f in os.listdir(path):
        print(' '*depth + f)
        if os.path.isdir(os.path.join(path, f)):
            printPart(os.path.join(path, f), depth+1)

printPart(askdirectory(), 0)
