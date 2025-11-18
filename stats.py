def get_num_words(book_file_path):
    with open(book_file_path) as f:
        #return type(f)
        book_text = f.read()
        num_words = len(book_text.split())
    return (f"Found {num_words} total words")

def get_num_characters(book_file_path):
    with open(book_file_path) as f:
        book_text = f.read()
        character_count = {}
        for i in book_text.lower():
            if i in character_count:
                character_count[i] += 1
            else:
                character_count[i] = 1
    return character_count

def sort_on(d):
    return d["num"]

def sort_character_count(character_count):
    sorted_character_count = []
    for c in character_count:
        item = {"char": c, "num": character_count[c]}
        sorted_character_count.append(item)
    sorted_character_count.sort(key=sort_on, reverse=True)
    return sorted_character_count