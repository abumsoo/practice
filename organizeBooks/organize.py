#!/usr/bin/env python

import json
import requests

apiSearch = "http://openlibrary.org/search.json?title="


def searchBook(title):
    search = apiSearch + title.replace(' ', '+')
    response = requests.get(search)
    data = response.json()
    docs = data["docs"]

    newest = ''
    for doc in docs:
        if newest == '':
            newest = doc
        elif newest["publish_year"] < doc["publish_year"]:
            newest = doc
            
        
    print(mostRecent)


def enterBook():
    with open('books', 'a') as f:
        title = input("Enter the title of the book: ")
        f.write(title + '\n')

def readList():
    with open('books') as f:
        for line in f:
            print(line, end = '')

def main():
    choice = None
    while choice != 'q':
        print("(e)nter a book")
        print("show book (l)ist")
        print("(s)earch for a title")
        print("(q)uit")
        choice = input()
        if choice == 'q':
            break
        elif choice == 'e':
            enterBook()
        elif choice == 'l':
            readList()
        elif choice == 's':
            title = input("Enter a title: ")
            searchBook(title)
        else:
            print("Not a valid option.")


main()
