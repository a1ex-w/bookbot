from os import read

def words_in_string(file_contents:str) -> int:
    count = 0
    book_split_by_word = file_contents.split()
    for word in book_split_by_word:
        count += 1

    return count


def get_book_text(filepath:str) -> str:
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    FILEPATH = "books/frankenstein.txt"
    book_string = get_book_text(FILEPATH)

    word_count = words_in_string(book_string)
    print (f"Found {word_count} total words")

main()
