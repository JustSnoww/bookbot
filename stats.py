def get_word_count(filepath):
    num_words = filepath.split()
    max_words = float("-inf")
    word_count = 0
    for i in range(0, len(num_words)):
        if i > max_words:
            word_count = i + 1
    return f"{word_count} words found in the document"


def get_character_count(filepath):
    lower_case = filepath.lower()
    words = lower_case.split()
    characters = [char for word in words for char in word]
    character_dict = {}
    for character in characters:
        if character in character_dict:
            character_dict[character] += 1
        else:
            character_dict[character] = 1
    return character_dict
