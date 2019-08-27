from tkinter import *
from tkinter import messagebox
import random
from urllib import request

tLF = request.urlopen("http://blog.joelberghoff.com/wp-content/uploads/2015/12/1990-2015-movie-titles.txt").read().decode("utf-8").split("\n")
titleList = [line.split("	")[1].split("(")[0].replace("II", "").replace("III", "").replace("IV", "") for line in tLF[:-1]]

class MainWindow:
    def __init__(self, master):
        self.master = master
        master.title("SUCCinator")
        self.randomButton = Button(master, text="Random", command=self.randomTitle)
        self.randomButton.grid(row=0, column=0, sticky=W)

    def randomTitle(self):
        messagebox.showinfo("Random Title", " ".join(titleList[random.randint(0, len(titleList)-1)].split(" ")[:-1]) + " Succ")

root = Tk()
mainWindow = MainWindow(root)
root.mainloop()
