class Book:
    def __init__(self, title, author, genre, is_available=True):
        self.title = title
        self.author = author
        self.genre = genre
        self.is_available = is_available

    def display_info(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Genre:", self.genre)
        availability = "Available" if self.is_available else "Not Available"
        print("Availability:", availability)
        print()


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, genre, is_available=True):
        book = Book(title, author, genre, is_available)
        self.books.append(book)
        print("Book added successfully.")

    def delete_book(self, title):
        found_books = []
        for book in self.books:
            if book.title.lower() == title.lower():
                found_books.append(book)

        if not found_books:
            print("No book with the given title found.")
        else:
            for book in found_books:
                self.books.remove(book)
            print("Book(s) deleted successfully.")

    def display_books(self):
        if not self.books:
            print("No books in the library.")
            return

        print("Books in the library:")
        for book in self.books:
            book.display_info()

    def search_book(self, title):
        found_books = []
        for book in self.books:
            if book.title.lower() == title.lower():
                found_books.append(book)

        if not found_books:
            print("No book with the given title found.")
        else:
            print("Found book(s):")
            for book in found_books:
                book.display_info()


# Creating library instance
library = Library()

while True:
    print("\nLibrary Management System Menu:")
    print("1. Add a book")
    print("2. Delete a book")
    print("3. Display all books")
    print("4. Search for a book")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        title = input("Enter the title of the book: ")
        author = input("Enter the author of the book: ")
        genre = input("Enter the genre of the book: ")
        availability = input("Is the book available? (yes/no): ")
        is_available = availability.lower() == 'yes'
        library.add_book(title, author, genre, is_available)
    elif choice == '2':
        title = input("Enter the title of the book to delete: ")
        library.delete_book(title)
    elif choice == '3':
        library.display_books()
    elif choice == '4':
        search_title = input("Enter the title of the book to search: ")
        library.search_book(search_title)
    elif choice == '5':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")
