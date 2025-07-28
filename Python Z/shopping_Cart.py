# Define a class to represent the shopping cart
class ShoppingCart:
    # Constructor to initialize the cart with an empty list
    def __init__(self):
        self.items = []

    # Add an item to the cart
    def add_item(self, name, quantity):
        item = (name, quantity)
        self.items.append(item)

    # Remove an item from the cart by item name
    def remove_item(self):
        # Ask the user for the item name to remove
        name = input("Enter the name of the item to remove: ")

        # Create a new list to store items after removing the specified one
        updated_items = []

        found = False  # To check if item was found

        for item in self.items:
            if item[0] != name:
                updated_items.append(item)
            else:
                found = True

        self.items = updated_items

        if found:
            print(f"'{name}' has been removed from the cart.")
        else:
            print(f"Item '{name}' not found in the cart.")

    # Calculate and return total quantity
    def total_quantity(self):
        total = 0
        for item in self.items:
            total += item[1]
        return total

# ---------- Using the ShoppingCart class ----------

# Create a cart
cart = ShoppingCart()

# Add items
cart.add_item("Papaya", 100)
cart.add_item("Guava", 200)
cart.add_item("Orange", 150)

# Show items
print("\nItems in the cart:")
for item in cart.items:
    print(item[0], "-", item[1])

# Show total quantity
print("Total Quantity:", cart.total_quantity())

# Remove an item (user input)
cart.remove_item()

# Show updated cart
print("\nUpdated cart:")
for item in cart.items:
    print(item[0], "-", item[1])

# Show updated total
print("Total Quantity:", cart.total_quantity())
