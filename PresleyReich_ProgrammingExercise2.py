# This program is dedicated to analyzing emails for spam.

# Constant list of 30 common spam words/phrases
SPAM_WORDS = [
    "free", "winner", "click here", "buy now", "limited time",
    "urgent", "act now", "risk-free", "money back", "guarantee",
    "cash", "bonus", "special promotion", "lowest price",
    "no cost", "credit card", "pre-approved", "congratulations",
    "exclusive deal", "earn money", "work from home", "free membership",
    "double your income", "100% free", "cheap", "gift card",
    "limited offer", "make money fast", "extra cash"
]

# This function is used to calculate the spam score
def calculate_spam_score(message):
    # Initialize score and triggered words list
    score = 0
    triggered = []

    # Convert the message to ensure all letters are the same for matching.
    lower_message = message.lower()

    # Check each keyword in the list, starts up the loop to check for keywords.
    for word in SPAM_WORDS:

        # If keyword is present, count occurrences and update score, adds word to the list using append
        if word in lower_message:
            score += lower_message.count(word)
            triggered.append(word)

    return score, triggered


def determine_spam_likelihood(score):
    if score == 0:
        return "Not Spam"

    elif score <= 3:
        return "Low likelihood of Spam"

    elif score <= 6:
        return "Moderate likelihood of Spam"

    elif score <= 9:
        return "High likelihood of Spam"

    else:
        return "Very high likelihood of Spam"


def main():
    # Asks the person for the email
    message = input("Please put in the email you want to scan: ")

    # Calculate the spam score and find triggered words
    score, triggered = calculate_spam_score(message)

    # Display the results of the scan
    display_report(score, triggered)


def display_report(score, triggered):
    # Determine likelihood rating
    likelihood = determine_spam_likelihood(score)

    # Print the formatted report
    print(f"Spam Score: {score}")
    print(f"Likelihood of spam: {likelihood}")

    # Show which words triggered the spam detection software
    if triggered:
        print("Triggered Keywords/Phrases:")
        for word in set(triggered):
            print(f" --- {word}")
    else:
        print("No suspicious words were detected.")

# Starts the file up
main()