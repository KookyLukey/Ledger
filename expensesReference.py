import sys
import pickle

def addExpense():
    expenseDescription = raw_input('Enter a description: ')
    amount = raw_input('Enter an amount: ')

    #load saved dict
    expenses = loadExpenses()

    #add to loaded dict and run saveExpenses
    expenses[expenseDescription] = amount
    saveExpenses(expenses)

def saveExpenses(expenses):
    file_Name = "expensesFile.txt"
    # open the file for writing
    fileObject = open(file_Name,'wb')

    # write and close file
    pickle.dump(expenses,fileObject)
    fileObject.close()

def loadExpenses():
    file_Name = "expensesFile.txt"
    fileObject = open(file_Name,'r')
    # load the object from the file into var b
    try:
        b = pickle.load(fileObject)
    except EOFError:
        pass
    else:
        return b

def printExpenses():
    dictExpenses = loadExpenses()
    for i in dictExpenses:
        print i, dictExpenses[i]
    print ""

def getTotalExpenses():
    expenses = loadExpenses()
    total = 0.0

    for val in expenses.values():
        total += float(val)

    return total

def removeExpense():
    toBeDel = raw_input('Enter description of the expense you want to remove: ')
    expenses = loadExpenses()

    del expenses[toBeDel]
    saveExpenses(expenses)
