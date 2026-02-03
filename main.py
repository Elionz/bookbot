import sys
from stats import get_num_words, get_chars_dict, chars_dict_to_sorted_list

def main():

    if len(sys.argv) <= 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    else:
        books = sys.argv[1]
        text = get_book_text(books)
        num_words = get_num_words(text)
        chars_dict = get_chars_dict(text)
        sorted_chars = chars_dict_to_sorted_list(chars_dict)  



    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {books}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_chars:
        ch = item["char"]
        num = item["num"]
        if ch.isalpha():
            print(f"{ch}: {num}")
    print("============= END ===============")


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    

main()