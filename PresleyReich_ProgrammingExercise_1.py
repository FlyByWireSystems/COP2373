# Function to get the number of tickets a buyer wants to buy
def get_tickets(tickets_left_over):
    # Loop until the user provides a number of tickets they can actually buy
    while True:
        # Ask the user for the number of tickets they want
        num_str = input(f"Welcome to the ticket seller: How many tickets would you like to buy? (1-4, {tickets_left_over} remaining): ")

        # Check if the input is a numeric value
        if num_str.isnumeric():
            num = int(num_str)  # Convert the string input to an integer, since you can't buy half of a ticket

            # Check if the number is within allowed range and does not exceed tickets left over available to buy
            if 1 <= num <= 4 and num <= tickets_left_over:
                return num  # Valid input, return the number of tickets
            else:
                # Input is a number but not within the allowed limits
                print(
                    f"Invalid input. You can only buy up to 4 tickets, but no more than {tickets_left_over} remaining. This event is limited to 20 tickets.")
        else:
            # Input is not a number
            print("Invalid input. Please enter a number.")


# Function to process the purchase and update ticket count
def process_purchase(tickets_left_over, customers_count):
    # Get the number of tickets the current customer wants
    tickets_sold = get_tickets(tickets_left_over)

    # Update remaining tickets after purchase
    tickets_left_over -= tickets_sold

    # Increase the total number of customers for every purchase made
    customers_count += 1

    # Show the purchase summary to the customer
    print(f"You bought {tickets_sold} tickets. {tickets_left_over} tickets are remaining.\n")

    # Return updated tickets and customer count
    return tickets_left_over, customers_count


# Function to display the final summary when all tickets are sold
def display_summary(customers_count):
    print(f"All tickets were sold! We are now sold out! Total customers: {customers_count}")


# Main program function
def main():
    # Initialize total tickets available and customer count
    total_tickets = 10
    customers = 0

    # Loop until all tickets are sold
    while total_tickets > 0:
        total_tickets, customers = process_purchase(total_tickets, customers)

    # Display final summary after all tickets are sold
    display_summary(customers)


# Call the main function to run whole program

main()
