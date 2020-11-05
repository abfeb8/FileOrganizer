import os
import shutil

# function to create folder if it does not exist
def createDir(folderName):
    try:
        os.mkdir(folderName)
        print("New directory "+folderName+" is created")
    except Exception:
        pass

# getting custom folder name form user
# function return a dictionary with extention as key and name as value
def getCustomFolderNames():
    customNames = dict()
    print("Enter in the format 'Extension:Folder_Name'")
    print("Note: to add more than one extension name use ',' to seperat them \neg: jpg:Image,png:Image,dox:document")
    userEntry = input()
    allFiles = userEntry.split(',')
    for fileName in allFiles:
        ext, nam = fileName.split(':')
        customNames[ext.strip()] = nam.strip()

    return customNames

# function to decide what name should a folde have
def decideFolderName(extentionName):
    if extentionName in userDefineNames:
        return userDefineNames[extentionName]
    else:
        return extentionName


userDefineNames = dict()
excludeFile = set()

# for testing purpose only
userDefineNames['py'] = 'Python'
excludeFile.add('pdf')

# getting the target directory
targetDirectory = input("Enter target directory: ")

# changing the working directory to the target directory
os.chdir(targetDirectory)

# iterating over all the file in the target directory
for file in os.listdir():
    # extracting fileName and extention from each file
    name, extention = os.path.splitext(file)

    # checking if the file is a folder or not
    if extention:
        extentionName = extention.split('.')[1]

        # checking of the file is mentioned in the exclude list
        if extentionName in excludeFile:
            continue

        # picking name for the folder
        folderName = decideFolderName(extentionName)

        # creating the directory for files
        createDir(folderName)

        # moving file to the desgneted folder
        shutil.move(file, folderName)

        # printing the action performed
        print(file+" is moved to "+folderName)
