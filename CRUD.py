import mysql.connector
import sqlite3
import psycopg2


def createBDsqlite3():
    myconect = sqlite3.connect("./BBDD_sqlite3")
    miCursor = myconect.cursor()

    miCursor.close()
    myconect.close()

def createBDmySQL():
    myconect = mysql.connector.connect(host='localhost', database='Personas', user='root', password='porter1986')
    miCursor = myconect.cursor()

    miCursor.close()
    myconect.close()


def createBDpostgres():
    myconect = psycopg2.connect(host='localhost', database='Personas', user='postgres', password='Porter1986')
    miCursor = myconect.cursor()

    miCursor.close()
    myconect.close()

