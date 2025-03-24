import os

def load_books():
    if not os.path.exists("library_catalogue.txt"):
        open("library_catalogue.txt", "w").close()
        print("No existing catalogue found. A new one has been created.")
    with open("library_catalogue.txt", "r") as f:
        return [line.strip() for line in f.readlines()]

def save_books(books):
    with open("library_catalogue.txt", "w") as f:
        for book in books:
            f.write(book + "\n")

def personal_library():
    books = load_books()
    print("Welcome to your Personal Library Catalogue!")

    while True:
        print("\nPlease choose an option:")
        print("1 - Add a New Book")
        print("2 - List All Books")
        print("3 - Search for a Book")
        print("4 - Remove a Book")
        print("0 - Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter the book title: ")
            author = input("Enter the author's name: ")
            year = input("Enter the year of publication: ")
            books.append(f"{title} by {author}, Published in {year}")
            save_books(books)
            print("Book added successfully!")
        elif choice == '2':
            print("\nLibrary Catalogue:")
            for i, book in enumerate(books, 1):
                print(f"{i}. {book}")
        elif choice == '3':
            search = input("Enter title or author to search: ").lower()
            results = [b for b in books if search in b.lower()]
            print("\nSearch Results:")
            for book in results:
                print(book)
        elif choice == '4':
            title = input("Enter the title of the book to remove: ")
            removed = False
            for book in books:
                if title.lower() in book.lower():
                    books.remove(book)
                    save_books(books)
                    print("Book removed.")
                    removed = True
                    break
            if not removed:
                print("Book not found.")
        elif choice == '0':
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

personal_library()
