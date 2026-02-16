TOTAL_CAPACITY = 350

tickets_sold = 0
total_bookings = 0
rejected_bookings = 0

print("--- Theatre Booking System (12+ Only) ---")

while tickets_sold < TOTAL_CAPACITY:
    user_input = input(f"\nEnter number of tickets (1-15) or 0 to exit [Remaining: {TOTAL_CAPACITY - tickets_sold}]: ")
    num_tickets = int(user_input)

    if num_tickets == 0:
        break

    if num_tickets < 1 or num_tickets > 15:
        print("Invalid number of tickets. Please choose between 1 and 15.")
        continue

    if tickets_sold + num_tickets > TOTAL_CAPACITY:
        print(f"Not enough seats! Only {TOTAL_CAPACITY - tickets_sold} remaining.")
        continue

    all_ages_valid = True
    for i in range(1, num_tickets + 1):
        age = int(input(f"  Enter age for person {i}: "))
        if age < 12:
            all_ages_valid = False
            break 

    if all_ages_valid:
        tickets_sold += num_tickets
        total_bookings += 1
        print(f"BOOKING CONFIRMED - {num_tickets} tickets.")
    else:
        rejected_bookings += 1
        print("BOOKING REJECTED - Age restriction (12+ only).")

print("\n" + "="*30)
print("FINAL REPORT")
print(f"Total Bookings: {total_bookings}")
print(f"Total Tickets Sold: {tickets_sold}")
print(f"Rejected Bookings: {rejected_bookings}")
print(f"Remaining Seats: {TOTAL_CAPACITY - tickets_sold}")
print("="*30)