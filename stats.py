def count_words(book):
    return len(book.split())

def count_chars(file_path):
    char_dict = {}
    with open(file_path) as f:
        chars = f.read().lower()
    for char in chars:
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    return char_dict

def sort_char_dict(char_dict):
    sorted_dicts = []
    for key, value in char_dict.items():
        sorted_dicts.append({"char": key, "num": value })
    sorted_dicts.sort(reverse=True, key=sort_on )    
    return sorted_dicts

def sort_on(dict):
    return dict["num"]