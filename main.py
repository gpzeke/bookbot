def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = number_of_words(text)
    num_characters = number_of_characters(text)
    sort_dict = sort_dictionary(num_characters)
    print(f"---Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()
    for d in sort_dict:
        character = d["character"]
        total = d["count"]
        if character.isalpha():
            print(f"The '{character}' character was found {total} times")
        continue
    
    print("--- End Report ---")
    


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def number_of_words(text):
    words = text.split()
    return len(words)

def number_of_characters(text):
    character_totals = {}
    for char in text:
        char = char.lower()
        if char in character_totals:
            character_totals[char] += 1
        else:
            character_totals[char] = 1
    return character_totals

def sort_dictionary(dict):
    
    def sort_on(dict):
        return dict["count"]
    
    chars = []
    for d in dict:
        chars.append({"character": d, "count": dict[d]})
    chars.sort(reverse=True, key=sort_on)
    return chars


main()
