# Create a program that asks the user for a number and then prints out a list of all the [divisors] of that number.

def devisors(num: int):
    lst = []

    for i in range(1, num):
        if num % i == 0:
            lst.append(i)
        else:
            continue

    return lst


if __name__ == '__main__':
    num = 50
    print(devisors(num))

