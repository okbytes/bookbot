def get_num_words(text: str):
    words = text.split()
    return len(words)


def get_character_counts(text: str):
    dict = {}

    for word in text.split():
        for char in word:
            letter = char.lower()
            if letter in dict:
                dict[letter] += 1
            else:
                dict[letter] = 1

    return dict


def sort_on(items):
    return items["num"]


def sorted_chars(dict: dict[str, int]) -> list:
    list = []
    for key in dict.keys():
        list.append({"char": key, "num": dict[key]})

    list.sort(reverse=True, key=sort_on)
    return list
