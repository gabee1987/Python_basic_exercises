import basics_1_to_12


def main():
    result_max = basics_1_to_12.maximum(2, 6)
    print("result_max: %s" % result_max)

    result_max_3 = basics_1_to_12.maximum_of_three(10, -5, 32)
    print("result_max_3: %s" % result_max_3)

    result_max_list = basics_1_to_12.max_of_list([3, 5, 9, 12, 45])
    print("result_max_list: %s" % result_max_list)

    result_length_of_string_1 = basics_1_to_12.length_of_string_1("hello")
    result_length_of_string_2 = basics_1_to_12.length_of_string_2("hello")
    print("result_length_of_string_1: %s" % result_length_of_string_1)
    print("result_length_of_string_2: %s" % result_length_of_string_2)

    result_histogram = basics_1_to_12.histogram([3, 5, 7, 5, 3])
    print("result_histogram: %s" % result_histogram)

    result_vowel_or_not = basics_1_to_12.vowel_or_not("b")
    print("result_vowel_or_not: %s" % result_vowel_or_not)

    result_sum_numbers = basics_1_to_12.sum_numbers([1, 2, 3, 4, 5])
    print("result_sum_numbers: %s" % result_sum_numbers)

    result_multiply_numbers = basics_1_to_12.multiply_numbers([1, 2, 3, 4, 5])
    print("result_multiply_numbers: %s" % result_multiply_numbers)

    result_reverse = basics_1_to_12.reverse("hello")
    result_reverse_2 = basics_1_to_12.reverse_2("hello")
    print("result_reverse: %s" % result_reverse)
    print("result_reverse_2: %s" % result_reverse_2)

    result_is_palindrome = basics_1_to_12.is_palindrome("abba")
    print("result_is_palindrome: %s" % result_is_palindrome)

    result_is_member = basics_1_to_12.is_member("c", ["a", "b", "c", "d"])
    print("result_is_member: %s" % result_is_member)

    result_overlapping = basics_1_to_12.overlapping(["string", "someword", "hello"], ["frog", "fox", "string"])
    print("result_overlapping: %s" % result_overlapping)

    result_generate_n_chars = basics_1_to_12.generate_n_chars(5, "c")
    result_generate_n_chars_1 = basics_1_to_12.generate_n_chars_1(5, "c")
    print("result__generate_n_chars: %s" % result_generate_n_chars)
    print("result__generate_n_chars_1: %s" % result_generate_n_chars_1)

if __name__ == "__main__":
    main()