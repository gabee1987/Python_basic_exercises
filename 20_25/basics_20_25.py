def translate(words):  # 20.
    lexicon = {
                "merry": "god",
                "christmas": "jul",
                "and": "och",
                "happy": "gott",
                "new": "nytt",
                "year": "år"
                }
    translated_string = ""
    for word in words.split(' '):
        if word in lexicon:
            translated_string += lexicon.get(word) + ' '
        else:
            translated_string += word + ' '
    return translated_string


def char_freq(string):  # 21.
    char_frequency = {}
    for letter in string:
        keys = char_frequency.keys()
        if letter in keys:
            char_frequency[letter] += 1
        else:
            char_frequency[letter] = 1
    return char_frequency



