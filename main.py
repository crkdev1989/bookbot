import sys
from stats import word_count, char_count, sort_chars_dict

def get_book_text(path):
    with open(path, "r", encoding="utf-8") as f:
        book_text = f.read()
        return book_text
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    book_text = get_book_text(path)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")

    total_words = word_count(book_text)
    print(f"Found {total_words} total words")

    print("-------- Character Count -------")
    chars = char_count(book_text)
    sorted_report = sort_chars_dict(chars)

    for item in sorted_report:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("----------- End ------------")
#    print(chars)
#   print(sorted_report)

if __name__ == "__main__":
    main()


