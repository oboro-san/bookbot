import sys
from stats import (
    count_words,
    count_characters,
    char_dict_to_sorted_list,
)

def get_book_text(path_to_file):
    with open(path_to_file, 'r', encoding='utf-8') as file:
        return file.read()
    
def print_report(path, word_count, sorted_char_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path} ...")
    print("------------ Word Count ------------")
    print(f"Found {word_count} total words.")
    print("----------- Character Count -------------")
    for item in sorted_char_list:
        if not item['char'].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")
    
    print("============= END ==============")
            
    
def main():
    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_text = get_book_text(path)
    total_words = count_words(book_text)
    dict_chars = count_characters(book_text)
    chars_sorted_list = char_dict_to_sorted_list(dict_chars)
    print_report(path, total_words, chars_sorted_list)
    
main()