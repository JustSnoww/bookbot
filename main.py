import sys
from stats import get_word_count
from stats import get_character_count
from stats import sort_dict


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path = sys.argv[1]
    text = get_book_text(path)
    num_words = get_word_count(text)
    char_dict = get_character_count(text)
    sort = sort_dict(char_dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count -----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count ---------")
    for items in sort:
        characters = items["char"]
        number = items["num"]
        print(f"{characters}: {number}")

    print("============= END ===============")


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


main()
