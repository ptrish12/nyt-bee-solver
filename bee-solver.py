from itertools import product
from nltk.corpus import words


word_list = set(words.words())


def get_perms_from_letters(letters: str):
    """
    Use itertools cartesian product method to get every possible word from a string of letters.

    :param letters: String of all seven letters in the bee
    :return all_letter_combos: List of strings.
    """
    word_length = 4  # set minimum word length required
    all_letter_combos = []
    while word_length < 10:
        first_set = []
        for x in product(letters, repeat=word_length):
            wd = ''.join(x)
            first_set.append(wd)
        for n in range(0, len(first_set)):
            all_letter_combos.append(first_set[n])
        word_length += 1
    return all_letter_combos


def is_it_a_word(list_of_perms: list, english_corpus: list):
    """
    Removes letter combinations that are not valid English words.

    :param list_of_perms: list of permutations of letters
    :param english_corpus: list of all valid English words
    :return valid_words: list of possible bee answers that are valid in English
    """
    valid_words =[]
    for word in list_of_perms:
        if word in english_corpus:
            valid_words.append(word)
    return valid_words


step_1 = get_perms_from_letters('aerc')
print(step_1)
step_3 = is_it_a_word(step_1, word_list)
print(step_3)


# TODO
# check for center letter
# find better corpus
# add user input
