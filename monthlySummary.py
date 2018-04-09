import sys

class MonthSummary:
    monthCount = 0

    def __init__(self, name, year, expectedBalance, actualBalance):
        self.name = name
        self.year = year
        self.expectedBalance = expectedBalance
        self.actualBalance = actualBalance
        MonthSummary.monthCount += 1

    def getMonthName():
        return self.name

    def getYear():
        return self.year

    def getExpectedBalance():
        return self.expectedBalance

    def getActualBalance():
        return self.actualBalance
