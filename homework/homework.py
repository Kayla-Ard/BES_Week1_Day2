# Lesson 3: Assignment | Linked List

# Implementing a BookInventory Linked List in Python
# Task 1: Create a class named Book with attributes for title, author, genre, ISBN, and quantity.
class Book:
    def __init__(self, title, author, genre, isbn, quantity):
        self.title = title
        self.author = author
        self.genre = genre
        self.isbn = isbn
        self.quantity = quantity


# Task 2: Create a class named Node to represent nodes in the linked list. Each node will store a book object.
class Node:
    def __init__(self, book = None):
        self.book = book
        self.next = None


# Task 3: Implement a class named InventoryManager to manage the inventory using a linked list.

# Task 4:Implement the following methods in the `InventoryManager`** class:
    # add_book(title, author, genre, isbn, quantity): Adds a new book to the inventory.
    # remove_book(isbn): Removes a book from the inventory based on its ISBN.
    # display_inventory(): Displays the current inventory.
    
class InventoryManager:
    def __init__(self):
        self.head = None  
    
    def add_book(self, title, author, genre, isbn, quantity):
        new_book = Book(title, author, genre, isbn, quantity)
        new_node = Node(new_book)
        
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        print(f"Added '{title}' to inventory.")
    
    def remove_book(self, isbn):
        if not self.head:
            print("Inventory is empty.")
            return
        
        if self.head.book.isbn == isbn:
            self.head = self.head.next
            print(f"Book with ISBN {isbn} removed from inventory.")
            return
        
        current = self.head
        while current.next:
            if current.next.book.isbn == isbn:
                current.next = current.next.next
                print(f"Book with ISBN {isbn} removed from inventory.")
                return
            current = current.next
        
        print(f"Book with ISBN {isbn} not found in inventory.")
    
    def display_inventory(self):
        if not self.head:
            print("Inventory is empty.")
            return
        
        print("Current Inventory:")
        current = self.head
        while current:
            book = current.book
            print(f"Title: {book.title}, Author: {book.author}, Genre: {book.genre}, ISBN: {book.isbn}, Quantity: {book.quantity}")
            current = current.next