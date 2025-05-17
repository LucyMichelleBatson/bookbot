import sys
from stats import count_words, count_chars, sort_char_dict

def get_book_text(file_path):
    with open(file_path) as f:
        return count_words(f.read())

    
def main():
    if len(sys.argv) != 2:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}")
        print("----------- Word Count ----------")
        print(f"Found {get_book_text(sys.argv[1])} total words")
        print("--------- Character Count -------")
        sorted_chars = sort_char_dict(count_chars(sys.argv[1]))
        for sort in sorted_chars:
            if sort["char"].isalpha():
                print(f"{sort["char"]}: {sort["num"]}")
        print("============= END ===============")

main() 