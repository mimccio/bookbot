def main():
    print("--- Begin report of books/frankenstein.txt ---")
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    chars_dict = get_chars_dict(text)
    get_char_report(chars_dict)
    print("--- End report ---")

def get_char_report(chars_dict):
    chars_list = list(chars_dict.items())
    chars_list.sort()
    for c in chars_list:
      if c[0].isalpha():
        print(f"The {c[0]} character was found {c[1]} times")

def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
