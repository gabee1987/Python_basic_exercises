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
        print("*" * number)


def length_of_string_1(string):
    return sum(1 for letter in string)


def length_of_string_2(string):
    length = 0
    for letter in string:
        length += 1
    return length


def vowel_or_not(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    if s not in vowels:
        return False
    return True


def sum_numbers(list_of_numbers):
    sums = 0
    for number in list_of_numbers:
        sums += number
    return sums


def multiply_numbers(list_of_numbers):
    multiplies = 1
    for number in list_of_numbers:
        multiplies *= number
    return multiplies


def reverse(string):
    return string[::-1]


def reverse_2(string):
    return "".join(reversed(string))


def is_palindrome(string):
    if not string == string[::-1]:
        return False
    return True


def is_member(x, a_list):
    for item in a_list:
        if item == x:
            return True
    return False


def overlapping(list_a, list_b):
    for item in list_a:
        for item in list_b:
            if item in list_a:
                return True
    return False


def generate_n_chars(n, string):
    return n * string


def generate_n_chars_1(n, string):
    result = ""
    for i in range(n):
        result += string
    return result








