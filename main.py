from stats import count_words, count_chars

def get_book_text(file_path):
    with open(file_path) as f:
        print(f"{count_words(f.read())} words found in the document")
    
def main():
    get_book_text("./books/frankenstein.txt")

main()        
count_chars("./books/frankenstein.txt")