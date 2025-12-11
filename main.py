import sys
from stats import (
    get_num_words,
    chars_dict_to_sorted_list,
    get_chars_dict,
)

def get_book_text(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: File not found at '{path}'")
        sys.exit(1) 


def print_report(book_path, num_words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    # Note: The filtering for isalpha() is usually done inside 
    # chars_dict_to_sorted_list to keep print_report cleaner, 
    # but it works here as well. We'll leave it as you wrote it.
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")


def main():
    # sys.argv[0] is the script name; we expect length 2 (script name + 1 argument)
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    # 2. GET THE BOOK PATH FROM COMMAND LINE ARGUMENT
    book_path = sys.argv[1]

    # 3. Process the book
    text = get_book_text(book_path)
    
    # NOTE: The imports use 'get_num_words' and 'get_chars_dict'. 
    # Ensure your stats.py functions match these names.
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    
    # 4. Sort and Print Report
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)
    print_report(book_path, num_words, chars_sorted_list)


if __name__ == "__main__":
    main()