import sys
import pickle
from expensesReference import *
from incomeReference import *

def startup():

    print "Welcome to Luke\'s Ledger"
    print "What would you like to do?"
    print ""
    print "1. Add Expense"
    print "2. Remove Expense"
    print "3. Print Short Summary"
    print "4. Print Expenses"
    print "5. Change Monthly Income"
    print "6. Exit"
    print ""

    menuDecision = raw_input()
    print ""

    if menuDecision == "1":
        addExpense()
    elif menuDecision == "2":
        removeExpense()
    elif menuDecision == "3":
        print float(getIncome()) - float(getTotalExpenses())
    elif menuDecision == "4":
        printExpenses()
    elif menuDecision == "5":
        setIncome()
    elif menuDecision == "6":
        sys.Exit(0)

    startup()

startup()
