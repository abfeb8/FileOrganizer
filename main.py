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
def getCustomFolderNames():
    customNames = dict()
    print("Enter in the format 'Extension:Folder_Name'")
    print("Note: to add more than one extension name use ',' to seperat them \neg: jpg:Image,png:Image,dox:document")
    userEntry = input()
    allFiles = userEntry.split(',')
    for fileName in allFiles:
        ext,nam = fileName.split(':')
        customNames[ext.strip()]=nam.strip()
    
    return customNames


# getting the target directory 
targetDirectory = input("Enter target directory: ")

# changing the working directory to the target directory
os.chdir(targetDirectory)

# iterating over all the file in the target directory 
for file in os.listdir():
    name,extention = os.path.splitext(file)
    if extention: 
        folderName = extention.split('.')[1]
        createDir(folderName)
        shutil.move(file,folderName)
        print(file+" is moved to "+folderName)


