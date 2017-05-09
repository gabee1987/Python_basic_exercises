from basics_20_25 import *


def main():
    result_translate = translate("happy new year and merry christmas")
    print("Result of translate: %s" % result_translate)

    result_char_freq = char_freq("abbabcbdbabdbdbabababcbcbab")
    print("Result of char_freq: %s" % result_char_freq)


if __name__ == "__main__":
    main()