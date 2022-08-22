from ast import Return
from curses.panel import bottom_panel
from gettext import install
from multiprocessing.connection import wait
from tkinter import *
import os

#Download Function
def getPack():
    packIdVar = idText.get()
    #("java -jar curseforge-cli.jar --args modpack install " + idText)

    os.system("java -jar curseforge-cli.jar --args modpack install " + str(packIdVar))

#Make Window
root = Tk()  # create a root widget
root.title("Modpack Installer 2.1.22")
root.geometry("700x500+50+50")  # width x height + x + y

#Title
downloadTitle = Label(root, text="Download from Mod ID")
downloadTitle.pack()

#Modpack Id Text entry
idText = Entry (root)
idText.pack()

#Modpack Id Conf
conf = Button(root, text="Download Pack", command=getPack)
conf.pack()

#credits
downloadTitle = Label(root, text="Thanks to https://github.com/North-West-Wind/CurseForge-CLI")
downloadTitle.pack(side=BOTTOM)

#keep screen open
root.mainloop()


##Experimental Feature/s

#Installed Mods
#installedTitle = Label(root, text="Installed Mods")
#installedTitle.pack()
#installedList = Label(root, text=(os.system("java -jar curseforge-cli.jar --args list")))