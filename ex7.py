# Purpose: 

def get_input():
    print("Please enter some text...")
    user_input = ""
    while True:
        new_input = input(">>> ")
        if new_input == "":
            break
        user_input = user_input + "\n" + new_input
    return user_input

def count_lines(str):
    return len(str.split("\n"))

def count_words(str):
    words = {}
    str = str.replace("\n", " ")
    str = str.replace(",", " ")
    str = str.replace(".", " ")
    str_words = str.split()
    for word in str_words:
        words.setdefault(word, 0)
        words[word] = words[word] + 1
    return words

def count_letters(str):
    all_letters = "abcdefghijklmmopqrstuvwxyz"
    letters = {}
    for letter in str.lower():
        if letter in all_letters:
            letters.setdefault(letter, 0)
            letters[letter] = letters[letter] + 1
    return letters

def dict_max(d):
    max_key = None
    max_value = 0
    for key in d.keys():
        if d[key] > max_value:
            max_key = key
            max_value = d[key]
    return max_key


user_input = get_input()
print("Number of lines: ", count_lines(user_input))
print("Most Common word: ", dict_max(count_words(user_input)))
print("Most Common letter: ", dict_max(count_letters(user_input)))
