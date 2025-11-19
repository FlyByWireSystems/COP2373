import sqlite3
import random
import matplotlib.pyplot as plt


# This function creates the database, creates the table,
# and inserts the 2023 starting population data.
def create_database():
    # Connects to the database file. If it doesn't exist, it's created.
    conn = sqlite3.connect("population_PR.db")
    cursor = conn.cursor()

    # Creates the population table with city, year, and population columns.
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS population (
            city TEXT,
            year INTEGER,
            population INTEGER
        )
    """)

    # IMPORTANT FIX:
    # Clears old data so your program doesn't keep adding new cities every run.
    cursor.execute("DELETE FROM population")

    # Initial Florida city populations (estimates)
    initial_data = {
        "Hialeah": 221000,
        "Cape Coral": 216000,
        "Port St. Lucie": 238000,
        "Lakeland": 115000,
        "Palm Bay": 121000,
        "Melbourne": 86000,
        "Naples": 21000,
        "Bradenton": 57000,
        "Punta Gorda": 20000,
        "Daytona Beach": 72000,
    }

    # Insert each city’s 2023 data into the table.
    for city, pop in initial_data.items():
        cursor.execute("INSERT INTO population VALUES (?, ?, ?)", (city, 2023, pop))

    conn.commit()   # Saves the data
    conn.close()    # Always close the database when done


# This function generates future population numbers for 20 years
# and inserts them into the database.
def simulate_population():
    conn = sqlite3.connect("population_PR.db")
    cursor = conn.cursor()

    # Fetch all cities and their 2023 populations from the database.
    cursor.execute("SELECT city, population FROM population WHERE year = 2023")
    rows = cursor.fetchall()

    # Loop through every city to simulate 20 years of new data
    for city, starting_pop in rows:
        pop = starting_pop  # Begin with the 2023 population

        # Generate populations for years 2024 through 2043
        for year in range(2024, 2044):

            # A smaller and less random growth rate (adjust if needed):
            # Between -1% decline and +2% growth each year
            growth_rate = random.uniform(-0.01, 0.02)

            # New population after applying the growth rate
            pop = int(pop * (1 + growth_rate))

            # Insert the new population for that year into the table
            cursor.execute("INSERT INTO population VALUES (?, ?, ?)", (city, year, pop))

    conn.commit()
    conn.close()



# This function shows the population trend for a city using a matplotlib graph.
def plot_city_population():
    conn = sqlite3.connect("population_PR.db")
    cursor = conn.cursor()

    # Get a list of all cities available in the table
    cursor.execute("SELECT DISTINCT city FROM population")
    cities = [row[0] for row in cursor.fetchall()]

    # Prints the options so the user can choose a valid city to type
    print("\nAvailable Cities:")
    for c in cities:
        print("-", c)

    # Asks the user which city's population chart they want to see
    choice = input("\nEnter any city name to view its population growth graph: ")

    # Fetches all population data for that city, ordered by year
    cursor.execute("SELECT year, population FROM population WHERE city = ? ORDER BY year", (choice,))
    data = cursor.fetchall()

    # If no data is returned, the user typed the city wrong
    if not data:
        print("City not found. Please run the program again.")
        return

    # Split data into two lists: years and population numbers to form x and y axis
    years = [row[0] for row in data]
    populations = [row[1] for row in data]

    # Creates the line plot showing population over time
    plt.figure(figsize=(9, 6))
    plt.plot(years, populations, marker="o")
    plt.title(f"Population Growth for {choice}")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.grid(True)
    plt.show()

    conn.close()


# The main function runs the whole program in order.
def main():
    create_database()       # Step 1: Create DB + insert 2023 data
    simulate_population()   # Step 2: Simulate 20 years of changes
    plot_city_population()  # Step 3: Ask user to pick a city & graph it



main()