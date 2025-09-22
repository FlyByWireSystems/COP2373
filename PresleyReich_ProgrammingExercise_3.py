from functools import reduce  # imports the tools needed to do the operations. ie reduce


def main():

    # Store the expenses as lists so we can make a list out of them.
    expenses = []

    #Asks for the expense list, and also has a exception to prevent user error
    print("Enter your monthly expenses (type 'done' when you are finished entering expenses).")
    while True:
        expense_type = input("Expense type (or 'done'): ")

        if expense_type.lower() == "done":
            break  # Exit the loop if the user is finished entering info

        #floats the values to provide decimals
        try:
            amount = float(input(f"Amount for {expense_type}: "))
            expenses.append((expense_type, amount))  # Adds the expense to the list
        except ValueError:
            print("Invalid amount, try again.")  # Handles any non-numeric input with error code

    if not expenses:
        print("No expenses entered.")
        return


    # Reduce calculates total, highest, and lowest in one calculation using lambda functions
    total, highest, lowest = reduce(
        lambda acc, x: (
            acc[0] + x[1],                      # Adds to total amount of expenses
            x if x[1] > acc[1][1] else acc[1],  # Updates the highest value if larger than previous
            x if x[1] < acc[2][1] else acc[2]   # Updates the lowest if smaller than previous
        ),
        expenses[1:],                           # Remaining expenses
        (expenses[0][1], expenses[0], expenses[0])  # Initial values
    )

    # Display results, in normal 2 decimal format for money
    print("\nFinal Expenses Report \n---------------------------------")
    print(f"Total Expense: ${total:.2f}")
    print(f"Highest Expense: {highest[0]} (${highest[1]:.2f})")
    print(f"Lowest Expense: {lowest[0]} (${lowest[1]:.2f})")


main()