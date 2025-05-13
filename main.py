from stats import get_word_count
from stats import get_character_count


def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    num_words = get_word_count(text)
    char_dict = get_character_count(text)
    print(f"{num_words} words found in the document")
    print(char_dict)


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


main()
