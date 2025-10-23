from os import read
from stats import get_character_frequency, chars_dict_to_sotred_list, get_words_in_string

def get_book_text(filepath:str) -> str:
    with open(filepath, "r") as file:
        file_contents = file.read()
    return file_contents

def main():
    FILEPATH = "books/frankenstein.txt"
    book_string = get_book_text(FILEPATH)
    word_count = get_words_in_string(book_string)
    character_analysis = get_character_frequency(book_string)
    sort_structure = chars_dict_to_sotred_list(character_analysis)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {FILEPATH}...")
    print("----------- Word Count ----------")
    print (f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in sort_structure:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()
