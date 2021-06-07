from re import split


def reverse_words(input: str):
    return " ".join(reversed(split("\s+", input)))
