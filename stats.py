def get_word_count(text):
    num_words = text.split()
    max_words = float("-inf")
    word_count = 0
    for i in range(0, len(num_words)):
        if i > max_words:
            word_count = i + 1
    return word_count


def get_character_count(text):
    characters = {}
    for char in text:
        lowered = char.lower()
        if lowered in characters:
            characters[lowered] += 1
        else:
            characters[lowered] = 1
    return characters


def sort_dict(dict):
    char_list = []
    for key in dict:
        value = dict[key]
        if key.isalpha():
            count_dict = {"char": key, "num": value}
            char_list.append(count_dict)
    char_list.sort(reverse=True, key=sort_on)
    return char_list


def sort_on(dict_item):
    return dict_item["num"]
