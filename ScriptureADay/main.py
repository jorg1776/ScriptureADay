import json
import mysql.connector
import databaseconfig as dbconfig
from win10toast import ToastNotifier

#def DisplayBoM(bookNum, chapterNum, verseNum):
#    #Prints 1 Nephi 3:7
#    book = bom["books"][bookNum]
#    chapter = book["chapters"][chapterNum - 1] 
#    verse = chapter["verses"][verseNum - 1]["text"]
#    notification = ToastNotifier()
#    notification.show_toast("1 Nephi 3:7", verse)

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

try:
    connection = mysql.connector.connect(
        user=dbconfig.mysql['user'], password=dbconfig.mysql['password'], 
        host=dbconfig.mysql['host'], database=dbconfig.mysql['database'])
except InterfaceError:
    print("Could not connect to database")

dbcursor = connection.cursor()
randomScripture = GetRandomScriptureFromDB(dbcursor)
bookID = randomScripture[0]
bookName = GetBookName(bookID, dbcursor)

try:
    with open('Scriptures/book-of-mormon.json', 'r') as file:
        bom = json.load(file) 
except ValueError:
    print("Error loading JSON")


connection.close()