import sqlite3

con=sqlite3.connet("database/surver.py")
cur = con.connect()

#incomeHead table commands
# insertion incomeHead

def insertIncomeHead(incomeHeadName,frequency):
    cur.execute("SELECT MAX(incomeHeadId) FROM incomeHead;")
    result= int(cur.fetchall()[0][0])
    incomeHeadId = result+1
    cur.execute(f"INSERT INTO incomeHead VALUES({incomeHeadId},'{incomeHeadName}','{frequency}');")
    
    
def removeIncomeHead(incomeHeadId: int):
    cur.execute(f"DELETE FROM incomeHead WHERE incomeHeadId = '{incomeHeadId}';")


def alterIncomeHeadDetails(incomeHeadId, columnName, newValue):
    cur.execute(f"UPDATE incomeHead SET {columnName} = '{newValue}' WHERE incomeHeadId = '{incomeHeadId}';")


def displayIncomeHead():
    cur.execute("SELECT *FROM incomeHead;")
    display = cur.fetchall()[0][0]
    return display


#income tabale commands

def insertIncome(incomeDate,incomeHeadName,incomeAmount,incomeDescription):
    cur.execute("SELECT MAX(incomeId) FROM incomeId;")
    result= int(cur.fetchall()[0][0])
    incomeId = result+1
    cur.execute(f"INSERT INTO income VALUES({incomeId},'{incomeDate}'{incomeHeadName}','{incomeAmount}','{incomeDescription}');")
    
    
def removeIncome(incomeId: int):
    cur.execute(f"DELETE FROM income WHERE incomeId = '{incomeId}';")


def alterIncomeDetails(incomeId, columnName, newValue):
    cur.execute(f"UPDATE income SET {columnName} = '{newValue}' WHERE incomeId = '{incomeId}';")


def displayIncome():
    cur.execute("SELECT *FROM income;")
    displayIncome = cur.fetchall()[0][0]
    return displayIncome

#expenseHaed table command


def insertExpenseHead(expenseHeadName,frequency):
    cur.execute("SELECT MAX(expenseHeadId) FROM expenseHead;")
    result= int(cur.fetchall()[0][0])
    expenseHeadId = result+1
    cur.execute(f"INSERT INTO expenseHead VALUES({expenseHeadId},'{expenseHeadName}','{frequency}');")
    
    
def removeExpenseHead(expenseHeadId: int):
    cur.execute(f"DELETE FROM expenseHead WHERE expenseHeadId = '{expenseHeadId}';")


def alterExpenseHeadDetails(expenseHeadId, columnName, newValue):
    cur.execute(f"UPDATE expenseHead SET {columnName} = '{newValue}' WHERE expenseHeadId = '{expenseHeadId}';")


def displayExpenseHead():
    cur.execute("SELECT *FROM expenseHead;")
    displayExpenseHead = cur.fetchall()[0][0]
    return displayExpenseHead

#ecpense table commands

def insertExpense(expenseDate,expenseHeadId,expenseAmount,expenseDescription):
    cur.execute("SELECT MAX(expenseId) FROM expense;")
    result= int(cur.fetchall()[0][0])
    expenseId = result+1
    cur.execute(f"INSERT INTO expense VALUES({expenseId},'{expenseDate}','{expenseHeadId}','{expenseAmount}',{expenseDescription}');")
    
    
def removeExpense(expenseId: int):
    cur.execute(f"DELETE FROM expense WHERE expenseId = '{expenseId}';")


def alterExpenseDetails(expenseId, columnName, newValue):
    cur.execute(f"UPDATE expense SET {columnName} = '{newValue}' WHERE expenseId = '{expenseId}';")


def displayExpense():
    cur.execute("SELECT *FROM expense;")
    displayExpense = cur.fetchall()[0][0]
    return displayExpense
