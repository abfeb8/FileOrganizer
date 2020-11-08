import os
import shutil


class file:
    def __init__(self, aFile):
        self.name, dotExtention = os.path.splitext(aFile)
        self.extention = None
        if dotExtention:
            self.extention = dotExtention[1:]

    def isFolder(self):
        if self.extention:
            return False
        return True

    def getExtention(self):
        return self.extention

    def getName(self):
        return self.name


class fileOrganiser:
    def __init__(self):
        targetDirectory = input('\nEnter target directory: ')
        os.chdir(targetDirectory)

    def getFiles(self):
        files = os.listdir()
        return files

    def iterate(self):
        allFiles = self.getFiles()
        for aFile in allFiles:
            aFile = file(aFile)
            if not aFile.isFolder():
                print(aFile.getName(), aFile.getExtention())


Organiser = fileOrganiser()
print(Organiser.iterate())
