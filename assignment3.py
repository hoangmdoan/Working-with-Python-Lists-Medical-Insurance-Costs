import re

def get_file_name():
    """Prompts the user for a file name and returns it."""
    while True:
        try:
            file_name = input("Enter the name of the input file: ")
            with open(file_name, 'r') as f:
                return file_name
        except FileNotFoundError:
            print(f"File not found: '{file_name}'. Please try again.")

def read_file(file_name):
    """Reads the file, cleans words, and returns a list of words."""
    with open(file_name, 'r') as file:
        text = file.read()
        # Remove punctuation using regular expression and split into words
        words = re.findall(r'\b\w+\b', text.lower()) 
        return words

def setup_word_dictionary(words):
    """Creates a dictionary with unique words as keys and count initialized to 0."""
    word_count = {}
    for word in words:
        word_count[word] = 0
    return word_count

def count_words(words, word_count):
    """Counts the occurrences of each word in the dictionary."""
    for word in words:
        if word in word_count:  # Handle potential KeyError
            word_count[word] += 1
        else:
            print(f"Unexpected word '{word}' not found in dictionary.")

def display_results(word_count):
    """Displays the words and their counts in a formatted way."""
    print("\nWords and Occurrences")
    print("-" * 50)
    for word, count in word_count.items():
        print(f"{word:<15} {count}")

def main():
    """Main function to orchestrate the word counting process."""
    try:
        file_name = get_file_name()
        words = read_file(file_name)
        word_count = setup_word_dictionary(words)
        count_words(words, word_count)
        display_results(word_count)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
