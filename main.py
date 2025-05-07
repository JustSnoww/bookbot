from stats import get_word_count

path = "books/frankenstein.txt"


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def main():
    book_text = get_book_text("books/frankenstein.txt")
    print(book_text)


main()
print(get_word_count(get_book_text(path)))
