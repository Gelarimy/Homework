#Write a Python program to print all unique values of all dictionaries in a list.

def sort_values(dic: dict):
    return list(set(dic.values()))

if __name__ == '__main__':
    dic = {'Kaleb': 20, 'Alisa': 18, 'Jo': 18, 'Wensday': 25}

    print(sort_values(dic))