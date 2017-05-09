from basics_13_19 import *


def main():
    result_of_max_in_list = max_in_list([3, 5, 9, 12, 45, 135, 5248, 1, -58, 658])
    print("Result of max_in_list: %s" % result_of_max_in_list)

    result_of_map_of_words = map_of_words(["Fear", "is", "the", "path", "to", "the", "dark", "side"])
    print("Result of map_of_words: %s" % result_of_map_of_words)

    result_of_find_longest_word = find_longest_word(["I", "am", "your", "father"])
    print("Result of find_longest_word: %s" % result_of_find_longest_word)

    result_of_filter_long_words = filter_long_words(["These", "are", "not", "the", "droids", "you", "are", "looking", "for..."], 4)
    print("Result of filter_long_words: %s" % result_of_filter_long_words)

    result_of_phrase_palindrome = phrase_palindrome("Dammit, I'm mad!")
    print("Result of phrase_palindrome: %s" % result_of_phrase_palindrome)

    result_of_pangram_checker = pangram_checker("The quick brown fox jumps over the lazy dog.")
    print("Result of pangram_checker: %s" % result_of_pangram_checker)

    result_of_99_bottles = song_99_bottles()
    print(result_of_99_bottles)


if __name__ == "__main__":
    main()