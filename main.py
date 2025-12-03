import stats
import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = stats.get_num_words(text)
    char_dict = stats.get_char_count(text)
    sorted_char_list = stats.chars_dict_to_sorted_list(char_dict)
    print_report(book_path, num_words, sorted_char_list)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def print_report(book_path, num_words, sorted_char_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in sorted_char_list:
        if i["char"].isalpha():
            print(f"{i["char"]}: {i["num"]}")
    print("============= END ===============")

main()