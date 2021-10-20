#Write a Python program to calculate the length of a string without using the `len` function.

def len_str(s: str ):
    l = 0
    for i in s:
        l+=1
    return l

if __name__== '__main__':
    string = "string for testing"
    lenght = len_str(string)
    print('The length of a string is %i' % lenght)