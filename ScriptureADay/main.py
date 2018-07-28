import json
import mysql.connector
import databaseconfig as dbconfig
from win10toast import ToastNotifier

def GetRandomScriptureFromDB(dbcursor):
    sql = "SELECT * FROM scriptures ORDER BY RAND() LIMIT 1"
    dbcursor.execute(sql)
    result = dbcursor.fetchone()
    return result

def GetBookName(bookID, dbcursor):
    sql = "SELECT bookName FROM books WHERE bookID = " + str(bookID)
    dbcursor.execute(sql)
    result = dbcursor.fetchone()
    bookName = result[0]
    return bookName

def GetSubBookNumber(subBook, bookID, dbcursor):
    sql = "SELECT subBookID FROM subbooks WHERE bookID = " + str(bookID) + " AND subBookName = '" + subBook + "'"
    dbcursor.execute(sql)
    result = dbcursor.fetchone()
    subBookNum = result[0]
    return subBookNum

def DisplayScripture(bookFile, subBookNum, chapter, verseNum):
    book = bookFile["books"][subBookNum]
    chapter = book["chapters"][chapter - 1]
    reference = chapter["verses"][verseNum - 1]["reference"]
    verse = chapter["verses"][verseNum - 1]["text"]
    notification = ToastNotifier()
    notification.show_toast(reference, verse)

try:
    connection = mysql.connector.connect(
        user=dbconfig.mysql['user'], password=dbconfig.mysql['password'], 
        host=dbconfig.mysql['host'], database=dbconfig.mysql['database'])
except InterfaceError:
    print("Could not connect to database")

dbcursor = connection.cursor()
randomScripture = GetRandomScriptureFromDB(dbcursor)
bookNum = randomScripture[0]
bookName = GetBookName(bookNum, dbcursor)
subBook = randomScripture[1]
subBookNum = GetSubBookNumber(subBook, bookNum, dbcursor)
chapter = randomScripture[2]
verseNum = randomScripture[3]

jsonPath = "Scriptures/" + bookName + ".json"
try:
    with open(jsonPath, 'r') as file:
        bookFile = json.load(file) 
except ValueError:
    print("Error loading JSON")

DisplayScripture(bookFile, subBookNum, chapter, verseNum)

connection.close()