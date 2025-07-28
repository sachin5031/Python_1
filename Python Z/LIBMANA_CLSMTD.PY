class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            return f"You have borrowed '{self.title}' by {self.author}."
        else:
            return f"Sorry, '{self.title}' is already borrowed."

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            return f"'{self.title}' has been returned successfully."
        else:
            return f"'{self.title}' is already in the library."

    def display(self):
        status = "Available" if not self.is_borrowed else "Not Available"
        return f"Title: {self.title}, Author: {self.author}, Status: {status}"


def main():
    library = {}

    num_books = int(input("Enter the number of books to add: "))
    for i in range(num_books):
        title = input(f"Enter title of book {i + 1}: ")
        author = input(f"Enter author of book {i + 1}: ")
        library[title] = Book(title, author)

    while True:
        print("\nChoose an option:")
        print("1. Borrow a book")
        print("2. Return a book")
        print("3. Display all books")
        print("4. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == "1":
            title = input("Enter the title of the book to borrow: ")
            if title in library:
                print(library[title].borrow())
            else:
                print("Book not found in the library.")
        
        elif choice == "2":
            title = input("Enter the title of the book to return: ")
            if title in library:
                print(library[title].return_book())
            else:
                print("Book not found in the library.")
        
        elif choice == "3":
            for book in library.values():
                print(book.display())
        
        elif choice == "4":
            print("Exiting the system. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
