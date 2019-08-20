"""
This program checks if two files with the same name have a different modified last date.
If they do, it replaces the oldest one with the newest one.

Future exercises: Try and break this up into multiple functions
"""
import os, shutil, fnmatch, filecmp, re

# r's needed to transforms into raw string

path1 = r"PythonTest1"
path2 = r"PythonTest2"
originalFullPath = []
compareFullPath = []

originalFileNames = []
compareFileNames = []

originalDir = []
oDirName = []
compareDir = []
cDirName = []


def dirLists(pathOriginal, pathCompare):
    for root, dirs, files in os.walk(pathOriginal):
        for name in files:
            originalFullPath.append(os.path.join(root, name))
            originalFileNames.append(os.path.join(name))

        # return names of directories only
        for name in dirs:
            originalDir.append(os.path.join(root, name))
            oDirName.append((os.path.join(name)))

    for root, dirs, files in os.walk(pathCompare):
        for name in files:
            compareFullPath.append(os.path.join(root, name))
            compareFileNames.append(os.path.join(name))

        # return names of directories only
        for name in dirs:
            compareDir.append(os.path.join(root, name))
    # print(oDirName)  # just directory names
    # print(originalDir)  #  directory paths


dirLists(path1, path2) # calls dirLists function

"""
# creates missing directories
for x in range(len(originalDir)):  # for the length of the originalDir array
        shutil.copytree(path2, originalDir[x])

# deals with the individual files
for i in range(len(originalFullPath)):  # for the amt of elements in the selected list

    if originalFileNames[i] in compareFileNames:
        # print("outermost IF")
        # print(originalFileNames)
        #   if the time last modified is greater in the original directory, copy the file over
        if os.path.getmtime(originalFullPath[i]) > os.path.getmtime(compareFullPath[i]):
            # print(originalFileNames[i])
            shutil.copy(originalFullPath[i], compareFullPath[i])

    # If file is not in the directory to be update, copies the file over
    elif originalFileNames[i] not in compareFileNames:
        shutil.copy(originalFullPath[i], compareFullPath[i])

# Needs to be able to delete anything that is NOT in the original directory but is in the original
"""


