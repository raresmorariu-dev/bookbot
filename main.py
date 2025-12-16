from stats import get_num_words
from stats import get_char_stat
from stats import dict_list
import sys

def main():
    if len(sys.argv) != 2: 
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    letter_dict = get_char_stat(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words.")
    print("--------- Character Count -------")
    char_dict_list = dict_list(letter_dict)
    for char_dict in char_dict_list: 
        print(f"{char_dict["char"]}: {char_dict["num"]}")
    print("============= END ===============")
def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
