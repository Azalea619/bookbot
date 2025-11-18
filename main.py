import sys
if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(book_file_path):
    with open(book_file_path) as f:
        book_text = f.read()
    return book_text

from stats import get_num_words, get_num_characters, sort_character_count

def main():
    #print (get_book_text("books/frankenstein.txt"))
    #print (get_num_words("books/frankenstein.txt"))
    character_counts = get_num_characters(sys.argv[1]) # replaced hardcoded filepath with second argument of sys.argv as this is filepath
    #print(character_counts)
    sorted_counts = sort_character_count(character_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(get_num_words(sys.argv[1]))
    print("--------- Character Count -------")
    for item in sorted_counts:
        ch = item["char"]
        if ch.isalpha():
            print(f"{ch}: {item['num']}") # single quotes in double quotes
    print("============= END ===============")

main()