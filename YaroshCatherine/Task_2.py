# Write a Python program to count the number of characters (character frequency) in a string (ignore case of letters).

def count_characters(s: str):
    dict_characters = dict()
    for i in enumerate(s.lower()):
        dict_characters[i[1]] = s.lower().count(i[1])
    return dict_characters


if __name__== '__main__':
    string = "What kind of characters here?"
    print(count_characters(string))


