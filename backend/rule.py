def rule_add_uppercase(word):
    return word.capitalize()


def rule_add_suffix(word, suffix='a'):
    return word + suffix


def rule_add_number(word, number=1):
    return word + str(number)


def rule_replace_letter(word, old_letter='q', new_letter='a'):
    return word.replace(old_letter, new_letter)


def rule_remove_letter(word, letter='a'):
    return word.replace(letter, '')


def rule_reverse_letters(word):
    return word[::-1]


def rule_uppercase_letters(word):
    return word.upper()


def rule_lowercase_letters(word):
    return word.lower()


def rule_remove_digits(word):
    return ''.join(char for char in word if not char.isdigit())


def rule_replace_spaces(word):
    return word.replace(' ', '_')