import os
import shutil


class file:
    def __init__(self, aFile):
        self.name, dotExtention = os.path.splitext(aFile)
        self.extention = None
        if dotExtention:
            self.extention = dotExtention[1:]

    def isFile(self):
        if self.extention:
            return True
        return False

    def getExtention(self):
        return self.extention

    def getName(self):
        return self.name


class fileOrganiser:
    def __init__(self):
        self.targetDirectory = input('\nEnter target directory: ')
        os.chdir(self.targetDirectory)

    def getFiles(self):
        self.files = os.listdir()
        return self.files

    def iterate(self):
        allFiles = self.getFiles()
        for aFile in allFiles:
            aFile = file(aFile)
            if aFile.isFile():
                print(aFile.getName(), aFile.getExtention())


run = fileOrganiser()
print(run.iterate())
