thing = []
addprice = {}

# Start
while(True):
    print("\n SuperMarket Billing System")
    print("1. Add Items")
    print("2. Add Quantity and price of Items")
    print("3. Edit the bill")
    print("4. View The Bill")
    print("5. Remove Items")
    print("6. Exit")

    options = int(input("Enter Options: "))

    # Option 1: Add Items
    if(options == 1):
        print("You Want Items please Enter Name:")
        item = input()
        if item in thing:
            print(f"{item} is already in the list!")
        else:
            thing.append(item)

    # Option 2: Add Quantity and Price
    elif(options == 2):
        if len(thing) == 0:
            print("No items are present.")
        else:
            for i in range(len(thing)):
                # Add Quantity
                print("Enter quantity of the", thing[i], ":")
                quantity = int(input())
                print(thing[i], "-", quantity)

                # Add Price
                print("Enter Price of the", thing[i], "- Quantity:", quantity)
                price = float(input())
                addprice[thing[i]] = {"quantity": quantity, "price": price}
                print(thing[i], "-", quantity, "-Rs", price)

    # Option 3: Edit the Bill
    elif(options == 3):
        if len(thing) != 0:
            edit = True
            while edit:
                print("\n1.Add New items ")
                print("2.Edit Price and Quantity")
                print("3.Exit")
                choice = int(input("Enter Choice: "))

                if choice == 1:
                    # Add New Item
                    print("You Want Items please Enter Name:")
                    item = input()
                    if item in thing:
                        print(f"{item} is already in the list!")
                    else:
                        thing.append(item)
                        print("Enter quantity of the", item, ":")
                        quantity = int(input())
                        print(item, "-", quantity)

                        print("Enter Price of the", item, "- Quantity:", quantity)
                        price = float(input())
                        addprice[item] = {"quantity": quantity, "price": price}
                        print(item, "-", quantity, "-Rs", price)

                elif choice == 2:
                    # Edit Existing Item
                    print("Edit the Bill enter Items Name:")
                    item = input()
                    if item in thing:
                        print("Enter quantity of the", item, ":")
                        quantity = int(input())
                        print(item, "-", quantity)

                        print("Enter Price of the", item, "- Quantity:", quantity)
                        price = float(input())
                        addprice[item] = {"quantity": quantity, "price": price}
                        print(item, "-", quantity, "-Rs", price)
                    else:
                        print(f"{item} is not in the list!")

                elif choice == 3:
                    edit = False

            # Display Updated Bill
            if len(thing) != 0:
                print("\nUpdated Bill")
                print("Items  Quantity  Price")
                total = 0
                for item in thing:
                    print(item, "\t", addprice[item]["quantity"], "\t", addprice[item]["price"])
                    total += addprice[item]["price"]
                print("      Total  = Rs", total)

    # Option 4: View the Bill
    elif(options == 4):
        if len(thing) != 0:
            print("\nDisplay Bill")
            print("Items  Quantity  Price")
            total = 0
            for item in thing:
                print(item, "\t", addprice[item]["quantity"], "\t", addprice[item]["price"])
                total += addprice[item]["price"]
            print("      Total  = Rs", total)
        else:
            print("No Items Added. Please Check.")

    # Option 5: Remove Items
    elif(options == 5):
        print("Remove Items Please Enter Name:")
        item = input()
        if item in thing:
            thing.remove(item)
            addprice.pop(item)

            # Display Updated Bill
            if len(thing) != 0:
                print("\nUpdated Bill")
                print("Items  Quantity  Price")
                total = 0
                for item in thing:
                    print(item, "\t", addprice[item]["quantity"], "\t", addprice[item]["price"])
                    total += addprice[item]["price"]
                print("      Total  = Rs", total)
            else:
                print("No Items Added. Please Check.")
        else:
            print(f"{item} is not in the list!")

    # Option 6: Exit
    elif(options == 6):
        print("Thank you! Welcome Again...")
        break

    # Invalid Option
    else:
        print("Invalid option! Please try again.")
