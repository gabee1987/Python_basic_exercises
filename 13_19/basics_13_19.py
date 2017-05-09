def max_in_list(list_of_numbers):  # 13.
    maximum_result = 0
    for number in list_of_numbers:
        if number > maximum_result:
            maximum_result = number
    return maximum_result


def length_of_string_2(string):
    length = 0
    for letter in string:
        length += 1
    return length


def map_of_words(list_of_words):  # 14.
    result = []
    for word in list_of_words:
        result.append(length_of_string_2(word))
    return result


def find_longest_word(list_of_words):  # 15.
    result = []
    for word in list_of_words:
        result.append(length_of_string_2(word))
    return max(result)


def filter_long_words(list_of_words, n):  # 16.
    result = []
    for word in list_of_words:
        if length_of_string_2(word) >= n:
            result.append(word)
    return result


def phrase_palindrome(phrase):  # 17.
    phrase_letters = []
    for letter in phrase.lower():
        if letter.isalpha():
            phrase_letters.append(letter)
    if phrase_letters == phrase_letters[::-1]:
        return True
    return False


def pangram_checker(sentence):  # 18.
    abc = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g',
        'h', 'i', 'j', 'k', 'l', 'm', 'n',
        'o', 'p', 'q', 'r', 's', 't', 'u',
        'v', 'w', 'x', 'y', 'z'
        ]
    for letter in sentence:
        if letter in abc:
            abc.remove(letter)
    if len(abc) == 0:
        return True
    return False


def song_99_bottles():  # 19.
    verse = """\
                {bottles} bottles of beer on the wall {bottles} bottles of beer
                Take one down, pass it around {bottle} bottles of beer on the wall
            """
    for bottles in range(99, 0, -1):
        print(verse.format(bottles=bottles, bottle=bottles-1))






