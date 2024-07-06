import sqlite3
con = sqlite3.connect("database/surver.db")
cur = con.cursor()
#creation of Table(incomeHead)
cur.execute("CREATE TABLE incomeHead(incomeHeadId int(10),incomeHeadName varchar(50),frequency varchar(30));")
cur.execute("CREATE TABLE income(incomeId int(10),incomeDate DATE,incomeHeadId int(10),incomeAmount int(20),incomeDescription varchar(200));")
cur.execute("CREATE TABLE expenceHead(expenceHeadId int(10),expenceHeadName varchar(50),freaquency varchar(50));")
cur.execute("CREATE TABLE expense(expenseId int(10),expenseDate DATE,expenseHeadId int(10),expenseAmount int(20),expenseDescription varchar(200));")
