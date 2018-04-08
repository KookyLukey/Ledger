import sys
import pickle

def setIncome():
    amount = raw_input('Enter monthly income: ')

    #load saved dict
    totalIncome = loadIncome()

    #add to loaded dict and run saveExpenses
    totalIncome["Income"] = amount
    saveIncome(totalIncome)

def saveIncome(totalIncome):
    file_Name = "incomeFile.txt"
    # open the file for writing
    fileObject = open(file_Name,'wb')

    # write and close file
    pickle.dump(totalIncome,fileObject)
    fileObject.close()

def loadIncome():
    file_Name = "incomeFile.txt"
    fileObject = open(file_Name,'r')
    # load the object from the file into var b
    try:
        b = pickle.load(fileObject)
    except EOFError:
        return {}
    else:
        return b

def getIncome():
    totalIncome = loadIncome()

    return totalIncome["Income"]
