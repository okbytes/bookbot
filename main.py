import sys

from stats import get_character_counts, get_num_words, sorted_chars


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()

    return file_contents


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]

    text = get_book_text(path)
    num_words = get_num_words(text)
    char_count = get_character_counts(text)
    char_list = sorted_chars(char_count)

    print(f"""
============ BOOKBOT ============
Analyzing book found at {path}...
----------- Word Count ----------
Found {num_words} total words
--------- Character Count -------""")

    for item in char_list:
        char = item["char"]
        if char.isalpha():
            print(f"{char}: {item['num']}")

    print("============= END ===============")


main()
