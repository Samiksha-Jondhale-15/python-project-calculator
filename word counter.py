def word_counter(filename):
    try:
        # Open and read the file
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()

        # Split into words (by whitespace)
        words = content.split()

        # Count words
        word_count = len(words)

        print(f"Total number of words in '{filename}': {word_count}")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Example usage
filename = "sample.txt"  # Replace with your file name
word_counter(filename)
