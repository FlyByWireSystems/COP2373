import re

def extract_sentences(text):
    # Extracts the sentences from the given text.

    # The Pattern allows A-Z or digits at start, matches until ., !, or ? occurs
    pattern = r'([A-Z0-9][^.!?]*[.!?])'

    # Find all matches using the pattern
    sentences = re.findall(pattern, text, flags=re.DOTALL)

    # Strip whitespace/blank from each sentence and return the list
    return [s.strip() for s in sentences]

def display_sentences(sentences):
    # Prints each sentence and the total count of the sentences

    # Iterates over sentences and print each one with a number, to count them.
    for i, sentence in enumerate(sentences, start=1):
        print(f"{i}. {sentence}")

    # Print total number of sentences
    print(f"\nTotal sentences: {len(sentences)}")

def main():
    # Prompt the user to enter a paragraph
    paragraph = input("Enter a paragraph: ")

    # Extracts each sentence from the paragraph
    sentences = extract_sentences(paragraph)

    # Display the sentences and count
    display_sentences(sentences)

# Calls the functions
main()