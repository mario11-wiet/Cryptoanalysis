
class PasswordRule:
    def __init__(self, transformation_function, weight=1):
        self.transformation_function = transformation_function
        self.weight = weight


class PasswordRules:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.initialize_rules()
        return cls._instance

    def initialize_rules(self):
        self.rules = [
            PasswordRule(self.rule_add_uppercase),
            PasswordRule(self.rule_add_suffix),
            PasswordRule(self.rule_add_number),
            PasswordRule(self.rule_replace_letter),
            PasswordRule(self.rule_remove_letter),
            PasswordRule(self.rule_reverse_letters),
            PasswordRule(self.rule_uppercase_letters),
            PasswordRule(self.rule_lowercase_letters),
            PasswordRule(self.rule_remove_digits),
            PasswordRule(self.rule_replace_spaces)
        ]

    @staticmethod
    def rule_add_uppercase(word):
        return word.capitalize()

    @staticmethod
    def rule_add_suffix(word, suffix='a'):
        return word + suffix

    @staticmethod
    def rule_add_number(word, number=1):
        return word + str(number)

    @staticmethod
    def rule_replace_letter(word, old_letter='q', new_letter='a'):
        return word.replace(old_letter, new_letter)

    @staticmethod
    def rule_remove_letter(word, letter='a'):
        return word.replace(letter, '')

    @staticmethod
    def rule_reverse_letters(word):
        return word[::-1]

    @staticmethod
    def rule_uppercase_letters(word):
        return word.upper()

    @staticmethod
    def rule_lowercase_letters(word):
        return word.lower()

    @staticmethod
    def rule_remove_digits(word):
        return ''.join(char for char in word if not char.isdigit())

    @staticmethod
    def rule_replace_spaces(word):
        return word.replace(' ', '_')