def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    chars = {}
    for char in text:
        lower_char = char.lower()
        if lower_char in chars:
            chars[lower_char] += 1
        else:
            chars[lower_char] = 1
    return chars

def sort_on(d):
    return d["num"]

def char_dict_to_sorted_list(char_dict):
    sorted_list = []
    for char in char_dict:
        sorted_list.append({"char": char, "num": char_dict[char]})
    sorted_list.sort(key=sort_on, reverse=True)
    return sorted_list

def report_statistics(word_count, characters):
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("------------ Word Count ------------")
    print(f"Found {word_count} total words.")
    print(f"----------- Character Count -------------")
    sorted_chars = dict(sorted(characters.items()))
    for char in sorted_chars:
        print(f"'{char}: {sorted_chars[char]}'")