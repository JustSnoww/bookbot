def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def main():
    book_text = get_book_text("books/frankenstein.txt")
    print(book_text)


def get_word_count():
    num_words = get_book_text("books/frankenstein.txt").split()
    max_words = float("-inf")
    word_count = 0
    for i in range(0, len(num_words)):
        if i > max_words:
            word_count = i + 1
            # print(f"{word_count} words found in the document")
    return f"{word_count} words found in the document"


main()
print(get_word_count())
