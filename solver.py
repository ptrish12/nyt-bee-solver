from itertools import product
from nltk.corpus import words


word_list = set(words.words())


def get_perms_from_letters(letters: str):
    """
    Use itertools cartesian product method to get every possible word from a string of letters.

    :param letters: String of all seven letters in the bee
    :return all_letter_combos: List of strings.
    """
    word_length = 4  # set min word length required
    word_length_max = 10  # set max word length to look for
    all_letter_combos = []
    while word_length < word_length_max:
        for x in product(letters, repeat=word_length):
            all_letter_combos.append(x)
        word_length += 1
    all_letter_combos = set(all_letter_combos)  # remove duplicates so it can handle double letters
    return all_letter_combos


def must_have_center_letter(all_perms: list, center_letter: str):
    combos_with_center_letter = []
    for wd in all_perms:
        if center_letter in wd:
            y = ''.join(wd)
            combos_with_center_letter.append(y)
    return combos_with_center_letter


def is_it_a_word(list_of_perms: list, english_corpus: list):
    """
    Removes letter combinations that are not valid English words.

    :param list_of_perms: list of permutations of letters
    :param english_corpus: list of all valid English words
    :return valid_words: list of possible bee answers that are valid in English
    """
    valid_words = []
    for word in list_of_perms:
        if word in english_corpus:
            valid_words.append(word)
    return valid_words


def main():
    center_letter = str(input("What is the center letter? "))
    other_letters = str(input("What are the outer letters? "))
    all_letters = center_letter + other_letters
    print(f'''Possible words are:
''', is_it_a_word(must_have_center_letter(get_perms_from_letters(all_letters),center_letter), word_list))


if __name__ == "__main__":
    main()


# TODO
# find better corpus
# make less slow
# write tests

