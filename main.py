def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def main():
    book_text = get_book_text("books/frankenstein.txt")
    print(book_text)


def get_word_count():
    num_words = get_book_text("books/frankenstein.txt").split

    return num_words


main()
