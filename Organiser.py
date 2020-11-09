import os
import shutil
from termcolor import colored


class File:
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


class FileOrganiser:
    def __init__(self):
        targetDirectory = input('\nEnter target directory: ')
        os.chdir(targetDirectory)

    def getFiles(self):
        files = os.listdir()
        return files

    def getFolderName(self, extention):
        return extention

    def createDir(self, folderName):
        try:
            os.mkdir(folderName)
            print(colored("New directory '{}' is created".format(folderName), 'blue'))
        except Exception:
            pass

    def moveFile(self, aFile, toFolder):
        try:
            shutil.move(aFile, toFolder)
            print(colored("'{}' is moved to '{}'".format(aFile,toFolder), 'green'))
        except Exception:
            print(colored("ERROR in moving file '{}'".format(aFile), 'red'))

    def iterate(self):
        allFiles = self.getFiles()
        for aFile in allFiles:
            currentFile = File(aFile)
            if not currentFile.isFolder():
                name = currentFile.getName()
                extention = currentFile.getExtention()
                folderName = self.getFolderName(extention)
                self.createDir(folderName)
                self.moveFile(aFile, folderName)


if __name__ == "__main__":
    Organiser = FileOrganiser()
    Organiser.iterate()