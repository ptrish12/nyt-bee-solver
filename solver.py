from nltk.corpus import words


def load_word_list():
    word_list = set(words.words())
    return word_list


def get_letter_inputs():
    center_letter = str(input("What is the center letter? "))
    other_letters = str(input("What are the outer letters? "))
    return center_letter, other_letters


def get_words_from_dictionary(word_list, center_letter, other_letters):
    all_letters = center_letter + other_letters
    valid_words = []
    for wd in word_list:
        valid = True
        if center_letter in wd:
            for k in wd:
                if k not in all_letters:
                    valid = False
            if valid:
                if len(wd) > 3:
                    valid_words.append(wd)
    return sorted(valid_words)


def main():
    center_letter, other_letters = get_letter_inputs()
    word_list = load_word_list()
    results = get_words_from_dictionary(word_list, center_letter, other_letters)
    print("Possible words are:")
    print(*results, sep="\n")


if __name__ == "__main__":
    main()

# TODO
# find better corpus
# write tests

