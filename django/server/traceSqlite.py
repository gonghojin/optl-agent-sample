import sqlite3

from sqlite3 import Error
from opentelemetry.instrumentation.sqlite3 import SQLite3Instrumentor

SQLite3Instrumentor().instrument()
def sql_connection():
    try:

        # con = sqlite3.connect('mydatabase.db')
        con = sqlite3.connect('mydatabase.db')

        return con

    except Error:

        print(Error)


def sql_table(con):
    cursorObj = con.cursor()

    cursorObj.execute(
        "CREATE TABLE employees(id integer PRIMARY KEY, name text, salary real, department text, position text, hireDate text)")

    con.commit()


def sql_insert(con):
    cursorObj = con.cursor()

    cursorObj.execute("INSERT INTO employees VALUES(1, 'John', 700, 'HR', 'Manager', '2017-01-04')")

    con.commit()

def sql_update(con):

    cursorObj = con.cursor()

    cursorObj.execute('UPDATE employees SET name = "Rogers" where id = 1')

    con.commit()

def sql_select(con):

    cursorObj = con.cursor()

    cursorObj.execute('SELECT * FROM employees ')

    con.commit()

def sql_drop(con):

    cursorObj = con.cursor()

    cursorObj.execute('DROP table if exists employees')

    con.commit()

con = sql_connection()

sql_table(con)
sql_insert(con)
sql_update(con)
sql_select(con)
sql_drop(con)