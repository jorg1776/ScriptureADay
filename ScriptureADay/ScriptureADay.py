import json

try:
    with open('Scriptures/book-of-mormon.json', 'r') as file:
        bom = json.load(file) 
except ValueError:
    print("Error loading JSON")

#Prints 1 Nephi 3:7
book = bom["books"][0]
chapter = book["chapters"][2] 
verse = ["verses"][6]["text"]
print(verse)