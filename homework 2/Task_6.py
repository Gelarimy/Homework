#Write a Python program to convert a given tuple of positive integers into an integer.

def convert_to_int(tupl: tuple):
    string = ''
    for i in tupl:
        string = string + str(i)
    return int(string)

if __name__ == '__main__':
    tupl = (1,2,5,7,35)
    print(convert_to_int(tupl))
