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
    
    def getFolderName(self,extention):
        return extention

    def createDir(self, folderName):
        try:
            os.mkdir(folderName)
            print("New directory '" + folderName + "' is created")
        except Exception:
            pass

    def moveFile(self, aFile, toFolder):
        shutil.move(aFile, toFolder)
        print(aFile + ' is moved to ' + toFolder)

    def iterate(self):
        allFiles = self.getFiles()
        for aFile in allFiles:
            currentFile = file(aFile)
            if not currentFile.isFolder():
                name = currentFile.getName()
                extention = currentFile.getExtention()
                folderName = self.getFolderName(extention)
                self.createDir(folderName)
                self.moveFile(aFile,folderName)

Organiser = fileOrganiser()
print(Organiser.iterate())
