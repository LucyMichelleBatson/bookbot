def count_words(book):
    return len(book.split())

def count_chars(file_path):
    char_dict = {}
    with open(file_path) as f:
        chars = [*f.read().lower().split()]
        print(chars)
    for char in chars:
        if char not in char_dict:
            char_dict[char] = 0
        else:
            char_dict[char] += 1
    print(char_dict)        