# Library Book Inventory Manager

library = {}

def add_book():
    book_id = input("Enter Book ID: ")
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")
    
    library[book_id] = {"Title": title, "Author": author}
    print("Book added successfully!\n")

def view_books():
    if not library:
        print("Library is empty.\n")
    else:
        print("Books in Library:")
        for book_id, details in library.items():
            print(f"ID: {book_id}, Title: {details['Title']}, Author: {details['Author']}")
        print()

def search_book():
    book_id = input("Enter Book ID to search: ")
    if book_id in library:
        details = library[book_id]
        print(f"Book Found - Title: {details['Title']}, Author: {details['Author']}\n")
    else:
        print("Book not found.\n")

def remove_book():
    book_id = input("Enter Book ID to remove: ")
    if book_id in library:
        del library[book_id]
        print("Book removed successfully.\n")
    else:
        print("Book not found.\n")

while True:
    print("Library Book Inventory Manager")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Remove Book")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        view_books()
    elif choice == "3":
        search_book()
    elif choice == "4":
        remove_book()
    elif choice == "5":
        print("Exiting program.")
        break
    else:
        print("Invalid choice.\n")