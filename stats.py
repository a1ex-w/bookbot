def get_words_in_string(file_contents:str) -> int:
    count = 0
    book_split_by_word = file_contents.split()
    for _ in book_split_by_word:
        count += 1
    return count

def get_character_frequency(file_contents:str) -> dict:
    my_dict = {}
    for char in file_contents:
        lower_case = char.lower()
        if lower_case in my_dict:
            my_dict[lower_case] += 1
        else:
            my_dict[lower_case] = 1
    return my_dict

def sort_on(d):
    return d["num"]

def chars_dict_to_sotred_list(frequency_count:dict) -> list:
    sorted_list = []
    for char in frequency_count:
        sorted_list.append({"char": char, "num": frequency_count[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list




