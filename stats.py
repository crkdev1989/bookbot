def word_count(book_text):
    words = book_text.split()
    return len(words)
def char_count(book_text):
    book_text = book_text.lower()
    chars = {}
    for char in book_text:
        if char in chars:
            chars[char] += 1
        else:
             chars[char] = 1
    return chars
   
def sort_chars_dict(chars_dict):
    char_list = []
    for char, num in chars_dict.items():
        char_list.append({"char": char, "num": num})
    def sort_on(dict_item):
        return dict_item["num"]
    char_list.sort(key=sort_on, reverse=True)
    return char_list
    
