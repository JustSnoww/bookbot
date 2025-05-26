from stats import get_word_count
from stats import get_character_count
from stats import sort_dict


def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    num_words = get_word_count(text)
    char_dict = get_character_count(text)
    sort = sort_dict(char_dict)
    print(f"{num_words} words found in the document")
    print(sort)


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


main()
