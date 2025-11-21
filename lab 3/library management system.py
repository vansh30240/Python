# Libray Managemt System
# Author: Vansh Nibhoria
# Date: 20 November 2025
# Course: Programming for Problem Solving using Python

import json
import os

# Task 1 — Book Class

class Book:
    def __init__(self, title, author, isbn, status="available"):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.status = status

    def issue(self):
        if self.status == "available":
            self.status = "issued"
            return True
        return False

    def return_book(self):
        self.status = "available"

    def is_available(self):
        return self.status == "available"

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "status": self.status
        }

    def __str__(self):
        return f"{self.title} by {self.author} | ISBN: {self.isbn} | Status: {self.status}"

# Task 2 — Inventory Manager

class LibraryInventory:
    def __init__(self, filename="books.json"):
        self.filename = filename
        self.books = []
        self.load_data()

    def add_book(self, book):
        self.books.append(book)
        self.save_data()

    def search_by_title(self, title):
        return [b for b in self.books if title.lower() in b.title.lower()]

    def search_by_isbn(self, isbn):
        for b in self.books:
            if b.isbn == isbn:
                return b
        return None

    def display_all(self):
        for b in self.books:
            print(b)

 # Task 3 — File Handling (JSON)

    def save_data(self):
        try:
            data = [b.to_dict() for b in self.books]
            with open(self.filename, "w") as f:
                json.dump(data, f, indent=4)
        except Exception as e:
            print("Error saving file:", e)

    def load_data(self):
        if not os.path.exists(self.filename):
            return
        try:
            with open(self.filename, "r") as f:
                data = json.load(f)
                for d in data:
                    self.books.append(Book(d["title"], d["author"], d["isbn"], d["status"]))
        except:
            print("Error loading file. Starting fresh.")

# Task 4 — Menu (CLI)

def menu():
    inv = LibraryInventory()

    while True:
        print("\n=== Library Menu ===")
        print("1. Add Book")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. View All Books")
        print("5. Search Book")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            title = input("Title: ")
            author = input("Author: ")
            isbn = input("ISBN: ")

            inv.add_book(Book(title, author, isbn))
            print("Book added!")

        elif choice == "2":
            isbn = input("Enter ISBN to issue: ")
            book = inv.search_by_isbn(isbn)
            if book:
                if book.issue():
                    inv.save_data()
                    print("Book issued.")
                else:
                    print("Book already issued.")
            else:
                print("Book not found.")

        elif choice == "3":
            isbn = input("Enter ISBN to return: ")
            book = inv.search_by_isbn(isbn)
            if book:
                book.return_book()
                inv.save_data()
                print("Book returned.")
            else:
                print("Book not found.")

        elif choice == "4":
            inv.display_all()

        elif choice == "5":
            t = input("Search title: ")
            results = inv.search_by_title(t)
            if results:
                for b in results:
                    print(b)
            else:
                print("No match found.")

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Try again.")


# Start Program
menu()