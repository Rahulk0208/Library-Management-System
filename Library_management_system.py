books = [
    "Python",
    "Java",
    "C++",
    "HTML",
    "SQL"
]

def show_books():
    print("\n--- Books Available ---")

    if len(books) == 0:
        print("No books available!")

    else:
        for book in books:
            print("-", book)

def issue_book():
    book = input("Enter book you want to issue: ")

    if book in books:
        books.remove(book)
        print(book, "has been issued successfully!")

    else:
        print("Book not available!")

def return_book():
    book = input("Enter book you want to return: ")

    if book in books:
        print("This book is already in the library!")

    else:
        books.append(book)
        print(book, "has been returned successfully!")

def add_book():
    book = input("Enter new book name: ")

    if book in books:
        print("Book already exists!")

    else:
        books.append(book)
        print(book, "added to the library!")

while True:

    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Show Books")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Add Book")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        show_books()

    elif choice == "2":
        issue_book()

    elif choice == "3":
        return_book()

    elif choice == "4":
        add_book()

    elif choice == "5":
        print("Thank you for using the Library Management System!")
        break

    else:
        print("Invalid choice! Please try again.")
