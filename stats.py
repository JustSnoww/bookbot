def get_word_count(filepath):
    num_words = filepath.split()
    max_words = float("-inf")
    word_count = 0
    for i in range(0, len(num_words)):
        if i > max_words:
            word_count = i + 1
    return f"{word_count} words found in the document"


def get_character_count(filepath):
    characters = {}
    for char in filepath:
        lowered = char.lower()
        if lowered in characters:
            characters[lowered] += 1
        else:
            characters[lowered] = 1
    return characters


def sort_dict(dict):
    pass
