class HotelManagementSystem:
    def __init__(self):
        self.rooms = {101: None, 102: None, 103: None, 104: None, 105: None}  # Room numbers and their occupants

    def display_rooms(self):
        print("\nRoom Availability:")
        for room, guest in self.rooms.items():
            status = "Available" if guest is None else f"Booked by {guest}"
            print(f"Room {room}: {status}")

    def book_room(self):
        name = input("Enter guest name: ")
        self.display_rooms()
        try:
            room_number = int(input("Enter room number to book: "))
        except ValueError:
            print("Invalid input. Please enter a valid room number.")
            return

        if room_number in self.rooms and self.rooms[room_number] is None:
            self.rooms[room_number] = name
            print(f"Room {room_number} has been successfully booked for {name}.")
        else:
            print("Room is either unavailable or already booked. Please choose a different room.")

    def checkout(self):
        self.display_rooms()
        try:
            room_number = int(input("Enter room number to check out: "))
        except ValueError:
            print("Invalid input. Please enter a valid room number.")
            return

        if room_number in self.rooms and self.rooms[room_number] is not None:
            print(f"Room {room_number} checked out. Goodbye, {self.rooms[room_number]}!")
            self.rooms[room_number] = None
        else:
            print("Invalid room number or the room is already vacant.")

    def view_bookings(self):
        print("\nBooking Details:")
        for room, guest in self.rooms.items():
            if guest is not None:
                print(f"Room {room} is booked by {guest}.")
        if not any(guest is not None for guest in self.rooms.values()):
            print("No rooms are currently booked.")

    def menu(self):
        while True:
            print("\nHotel Management System")
            print("1. Display Rooms")
            print("2. Book a Room")
            print("3. Check Out")
            print("4. View Bookings")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.display_rooms()
            elif choice == '2':
                self.book_room()
            elif choice == '3':
                self.checkout()
            elif choice == '4':
                self.view_bookings()
            elif choice == '5':
                print("Thank you for using the Hotel Management System. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

# Create an instance of the system and start the menu
if __name__ == "__main__":
    system = HotelManagementSystem()
    system.menu()
