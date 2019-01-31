#!/usr/bin/env python

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
        print("(q)uit")
        choice = input()
        if choice == 'q':
            break
        elif choice == 'e':
            enterBook()
        elif choice == 'l':
            readList()
        else:
            print("Not a valid option.")


main()
