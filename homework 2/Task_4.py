#Write a Python program to sort a dictionary by key.

def sort(dic: dict):
    sorted_dic = {}
    sorted_keys = sorted(dic.keys())

    for k in sorted_keys:
        sorted_dic[k] = dic[k]

    return sorted_dic

if __name__ == '__main__':
    dic = {'Kaleb': 20, 'Alisa': 15, 'Jo': 18, 'Wensday': 25}

    print(sort(dic))