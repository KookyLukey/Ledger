import sys
import pickle
from expensesReference import *
from incomeReference import *
from monthlySummary import *
from summaryReference import *


def startup():

    print "Welcome to Luke\'s Ledger"
    print "What would you like to do?"
    print ""
    print "1. Add Expense"
    print "2. Remove Expense"
    print "3. Print Previous Month Summary"
    print "4. Print Current Month Summary"
    print "5. Print Expenses"
    print "6. Change Monthly Income"
    print "7. Add End of Month Statement"
    print "8. Exit"
    print ""

    menuDecision = raw_input()
    print ""

    if menuDecision == "1":
        addExpense()
    elif menuDecision == "2":
        removeExpense()
    elif menuDecision == "3":
        pass #TODO add this
    elif menuDecision == "4":
        printShortSummary()
    elif menuDecision == "5":
        printExpenses()
    elif menuDecision == "6":
        setIncome()
    elif menuDecision == "7":
        createMonthlySummary()
    elif menuDecision == "8":
        sys.Exit(0)

    startup()

def printShortSummary():
    prevMonths = loadPrevMonths()
    startingBalance = float(prevMonths[-1].actualBalance)
    maxBalance = startingBalance + float(getIncome())
    total = maxBalance - (getTotalExpenses() + 900)
    print "Expected end of month balance: $" + str(total)
    print ""

def createMonthlySummary():
    month = raw_input('Enter Month: ')
    year = raw_input('Enter Year: ')
    expected = float(getIncome()) - float(getTotalExpenses())
    actual = raw_input('Actual Balance Remaining: ')

    monthYearSumm = MonthSummary(month, year, expected, actual)
    prevMonths = loadPrevMonths()
    prevMonths.append(monthYearSumm)
    saveSummary(prevMonths)

startup()
