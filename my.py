
def display_trains():
    print("Available Trains:")
    for train in trains:
        print(f"Train Number: {train['train_number']}, Train Name: {train['train_name']}, Source: {train['source']}, Destination: {train['destination']}, Seats Available: {train['seats_available']}")

def reserve_ticket(train_number, passenger_name, num_tickets):
    for train in trains:
        if train['train_number'] == train_number:
            if train['seats_available'] >= num_tickets:
                # Generate a random PNR (Passenger Name Record)
                pnr = random.randint(1000, 9999)
                reservation = {
                    "train_number": train_number,
                    "passenger_name": passenger_name,
                    "num_tickets": num_tickets,
                }
                reservations[pnr] = reservation
                train['seats_available'] -= num_tickets
                print(f"Reservation successful! PNR: {pnr}")
            else:
                print("Seats not available.")
            return

    print("Train not found.")
while True:
    print("\nRailway Ticket Reservation System")
    print("1. Display Available Trains")
    print("2. Reserve a Ticket")
    print("3. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        display_trains()
    elif choice == "2":
        train_number = input("Enter the train number: ")
        passenger_name = input("Enter passenger name: ")
        num_tickets = int(input("Enter the number of tickets: "))
        reserve_ticket(train_number, passenger_name, num_tickets)
    elif choice == "3":
        print("Thank you for using the Railway Ticket Reservation System.")
        break
    else:
        print("Invalid choice. Please try again.")