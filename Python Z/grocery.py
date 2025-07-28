
# Create an empty dictionary to store groceries and their prices
grocery_list = {}

while True:
        # Display menu options
        print("\nOptions:")
        print("1. Display Grocery List with Prices")
        print("2. Add Item with Price")
        print("3. Remove Item")
        print("4. Update Item Price")
        print("5. Exit")
        
        # Get user's choice
        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '1':
            # Display the current grocery list with prices
            if grocery_list:
                print("Current grocery list with prices:")
                for item, price in grocery_list.items():
                    print(f"- {item}: ${price}")
            else:
                print("Your grocery list is empty.")

        elif choice == '2':
            # Add an item with price to the grocery list
            item = input("Enter an item to add to the grocery list: ")
            try:
                price = float(input(f"Enter the price for {item}: $"))
                grocery_list[item] = price
                print(f"{item} with price ${price} has been added to the list.")
            except ValueError:
                print("Invalid price entered. Please enter a valid number.")

        elif choice == '3':
            # Remove an item from the grocery list
            item = input("Enter an item to remove from the grocery list: ")
            if item in grocery_list:
                del grocery_list[item]
                print(f"{item} has been removed from the list.")
            else:
                print(f"{item} is not in the grocery list.")

        elif choice == '4':
            # Update the price of an existing item
            item = input("Enter the item you want to update the price for: ")
            if item in grocery_list:
                try:
                    new_price = float(input(f"Enter the new price for {item}: $"))
                    grocery_list[item] = new_price
                    print(f"The price of {item} has been updated to ${new_price}.")
                except ValueError:
                    print("Invalid price entered. Please enter a valid number.")
            else:
                print(f"{item} is not in the grocery list.")

        elif choice == '5':
            # Exit the program
            print("Exiting program.")
            break

        else:
            # Handle invalid choices
            print("Invalid choice, please try again.")

