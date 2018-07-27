import json
import mysql.connector
import databaseconfig as dbconfig

try:
    connection = mysql.connector.connect(
        user=dbconfig.mysql['user'], password=dbconfig.mysql['password'], 
        host=dbconfig.mysql['host'], database=dbconfig.mysql['database'])
except InterfaceError:
    print("Could not connect to database")


try:
    with open('Scriptures/book-of-mormon.json', 'r') as file:
        bom = json.load(file) 
except ValueError:
    print("Error loading JSON")

def DisplayBoM(bookNum, chapterNum, verseNum):
    #Prints 1 Nephi 3:7
    book = bom["books"][bookNum]
    chapter = book["chapters"][chapterNum - 1] 
    verse = chapter["verses"][verseNum - 1]["text"]
    print(verse)

DisplayBoM(0, 3, 7)

#connection.close()