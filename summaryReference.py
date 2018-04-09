import sys
import pickle

def saveSummary(monSummary):
    file_Name = "prevMonths.txt"
    # open the file for writing
    fileObject = open(file_Name,'wb')

    # write and close file
    pickle.dump(monSummary,fileObject)
    fileObject.close()

def loadPrevMonths():
    file_Name = "prevMonths.txt"
    fileObject = open(file_Name,'r')
    # load the object from the file into var b
    try:
        b = pickle.load(fileObject)
    except EOFError:
        return []
    else:
        return b
