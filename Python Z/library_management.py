library = {}

while True:
    print("\n--- Library Management System ---")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Exit")
    
    choice = input("Enter your choice: ")

    if choice == "1":
        title = input("Enter the book title: ")
        copies = int(input("Enter the number of copies: "))
        if title in library:
            library[title] += copies
        else:
            library[title] = copies
        print(f"'{title}' has been added with {copies} copies.")

    elif choice == "2":
        if not library:
            print("No books available in the library.")
        else:
            print("Available books:")
            for title, copies in library.items():
                print(f"{title} - {copies} copies")

    elif choice == "3":
        title = input("Enter the book title to borrow: ")
        if title not in library:
            print(f"Sorry, '{title}' is not available in the library.")
        elif library[title] == 0:
            print(f"Sorry, all copies of '{title}' are currently borrowed.")
        else:
            library[title] -= 1
            print(f"You have borrowed '{title}'.")

    elif choice == "4":
        title = input("Enter the book title to return: ")
        if title in library:
            library[title] += 1
            print(f"'{title}' has been returned. Thank you!")
        else:
            print(f"'{title}' does not belong to this library. But we will add it to our collection.")
            library[title] = 1

    elif choice == "5":
        print("Exiting the Library Management System. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
