def maximum(n1, n2):
    if n1 > n2:
        return n1
    elif n1 < n2:
        return n2


def maximum_of_three(n1, n2, n3):
    result = n1
    if n2 > result:
        result = n2
    if n3 > result:
        result = n3
    return result


def max_of_list(list_of_numbers):
    result = 0
    for number in list_of_numbers:
        if number > result:
            result = number
    return result


def histogram(list_of_numbers):
    for number in list_of_numbers:
        print("*" + '\n') in range(number)



