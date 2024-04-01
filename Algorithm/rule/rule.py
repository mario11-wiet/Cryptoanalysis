import string
import random

from Algorithm.rule.constants import SIMILAR_CHARACTERS, SPECIAL_CHARACTERS


class PasswordRules:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.initialize_rules()
        return cls._instance

    def initialize_rules(self):
        self.rules = [
            AddUppercaseRule(),
            ReverseLettersRule(),
            UppercaseLettersRule(),
            LowercaseLettersRule(),
            RemoveDigitsRule(),
            ReplaceSpacesRule(),
            DuplicateFirstCharacterRule(),
            DuplicateLastCharacterRule(),
            DuplicateEveryCharacterRule(),
            ToggleCaseAtRandomPositionRule(),
            DuplicateWordReversedRule(),
            DeleteFirstCharacterRule(),
            DeleteLastCharacterRule(),
            AddSpecialCharacterAtEndRule(),
            AddSpecialCharacterAtStartRule(),
            AddPrefixRule(),
            AddSuffixRule(),
            AddNumberRule(),
            AddNumberAtStartRule(),
            ReplaceLetterRule(),
            AddNumberAtRandomPositionRule(),
            RemoveLetterRule(),
            RotateWordLeftRule(),
            RotateWordRightRule(),
            InsertCharacterAtRandomPositionRule(),
            DeleteCharacterAtRandomPositionRule(),
            AddSpecialCharacterAtRandomPositionRule()
        ]

    def sort_rules(self):
        sorted_rules = sorted(self.rules, key=lambda rule: rule.weight / max(rule.counter, 1))
        return sorted_rules


class PasswordRule:
    def __init__(self, weight=0):
        self.weight = weight
        self.counter = 0
        self.is_repeatedly = True
        self.rules = {}

    def add_rule(self, rule):
        if rule not in self.rules:
            self.rules[rule] = 1
        else:
            self.rules[rule] += 1

    def __str__(self):
        return self.__class__.__name__

    def __repr__(self):
        return self.__class__.__name__

    def most_common_rules(self, number):
        sorted_rules = sorted(self.rules.items(), key=lambda x: x[1], reverse=True)
        best_rules = [rule[0] for rule in sorted_rules[:number]]
        return best_rules

    def execute(self, word):
        self.counter += 1
        return word


# is_repeatedly = False

class AddUppercaseRule(PasswordRule):
    def __init__(self, weight=1):
        super().__init__(weight)
        self.is_repeatedly = False

    def execute(self, word):
        self.counter += 1
        return self.upload_rule(word)

    def upload_rule(self, word):
        return word.capitalize()


class ReverseLettersRule(PasswordRule):
    def __init__(self, weight=1):
        super().__init__(weight)
        self.is_repeatedly = False

    def execute(self, word):
        self.counter += 1
        return self.upload_rule(word)

    def upload_rule(self, word):
        return word[::-1]


class UppercaseLettersRule(PasswordRule):
    def __init__(self, weight=1):
        super().__init__(weight)
        self.is_repeatedly = False

    def execute(self, word):
        self.counter += 1
        return self.upload_rule(word)

    def upload_rule(self, word):
        return word.upper()


class LowercaseLettersRule(PasswordRule):
    def __init__(self, weight=1):
        super().__init__(weight)
        self.is_repeatedly = False

    def execute(self, word):
        self.counter += 1
        return self.upload_rule(word)

    def upload_rule(self, word):
        return word.lower()


class RemoveDigitsRule(PasswordRule):
    def __init__(self, weight=1):
        super().__init__(weight)
        self.is_repeatedly = False

    def execute(self, word):
        self.counter += 1
        return self.upload_rule(word)

    def upload_rule(self, word):
        return ''.join(char for char in word if not char.isdigit())


class ReplaceSpacesRule(PasswordRule):
    def __init__(self, weight=1):
        super().__init__(weight)
        self.is_repeatedly = False

    def execute(self, word):
        self.counter += 1
        return self.upload_rule(word)

    def upload_rule(self, word):
        return word.replace(' ', '_')


class DuplicateFirstCharacterRule(PasswordRule):
    def __init__(self, weight=1):
        super().__init__(weight)
        self.is_repeatedly = False

    def execute(self, word):
        self.counter += 1
        return self.upload_rule(word)

    def upload_rule(self, word):
        if word:
            return word[0] + word
        else:
            return word


class DuplicateLastCharacterRule(PasswordRule):
    def __init__(self, weight=1):
        super().__init__(weight)
        self.is_repeatedly = False

    def execute(self, word):
        self.counter += 1
        return self.upload_rule(word)

    def upload_rule(self, word):
        if word:
            return word + word[-1]
        else:
            return word


class DuplicateEveryCharacterRule(PasswordRule):
    def __init__(self, weight=1):
        super().__init__(weight)
        self.is_repeatedly = False

    def execute(self, word):
        self.counter += 1
        return self.upload_rule(word)

    def upload_rule(self, word):
        return ''.join(char * 2 for char in word)


class ToggleCaseAtRandomPositionRule(PasswordRule):
    def __init__(self, weight=1):
        super().__init__(weight)
        self.is_repeatedly = False

    def execute(self, word):
        self.counter += 1
        return self.upload_rule(word)

    def upload_rule(self, word):
        if word:
            random_index = random.randint(0, len(word) - 1)
            return word[:random_index] + word[random_index].swapcase() + word[random_index + 1:]
        else:
            return word


class DuplicateWordReversedRule(PasswordRule):
    def __init__(self, weight=1):
        super().__init__(weight)
        self.is_repeatedly = False

    def execute(self, word):
        self.counter += 1
        return self.upload_rule(word)

    def upload_rule(self, word):
        return word + word[::-1]


class DeleteFirstCharacterRule(PasswordRule):
    def __init__(self, weight=1):
        super().__init__(weight)
        self.is_repeatedly = False

    def execute(self, word):
        self.counter += 1
        return self.upload_rule(word)

    def upload_rule(self, word):
        return word[1:]


class DeleteLastCharacterRule(PasswordRule):
    def __init__(self, weight=1):
        super().__init__(weight)
        self.is_repeatedly = False

    def execute(self, word):
        self.counter += 1
        return self.upload_rule(word)

    def upload_rule(self, word):
        return word[:-1]


class AddSpecialCharacterAtEndRule(PasswordRule):
    def __init__(self, weight=1):
        super().__init__(weight)
        self.is_repeatedly = False
        self.special_char = random.choice(SPECIAL_CHARACTERS)

    def execute(self, word):
        self.counter += 1
        return self.upload_rule(word)

    def upload_rule(self, word):
        return word + self.special_char


class AddSpecialCharacterAtStartRule(PasswordRule):
    def __init__(self, weight=1):
        super().__init__(weight)
        self.is_repeatedly = False
        self.special_char = random.choice(SPECIAL_CHARACTERS)

    def execute(self, word):
        self.counter += 1
        return self.upload_rule(word)

    def upload_rule(self, word):
        return self.special_char + word


class AddPrefixRule(PasswordRule):
    def __init__(self, weight=1):
        super().__init__(weight)
        self.is_repeatedly = False
        self.random_letter = self.random_letters()

    def execute(self, word):
        self.counter += 1
        return self.upload_rule(word)

    def upload_rule(self, word):
        return self.analyze_suffix(word) + word

    def analyze_suffix(self, word):
        for letter in self.random_letter:
            if letter not in word:
                return letter
        return random.choice(self.random_letter)

    @staticmethod
    def random_letters():
        all_letters = list(string.ascii_letters)
        random.shuffle(all_letters)
        random_letters = ''.join(all_letters)
        return random_letters


class AddSuffixRule(PasswordRule):
    def __init__(self, weight=1):
        super().__init__(weight)
        self.is_repeatedly = False
        self.random_letter = self.random_letters()

    def execute(self, word):
        self.counter += 1
        return self.upload_rule(word)

    def upload_rule(self, word):
        return word + self.analyze_suffix(word)

    def analyze_suffix(self, word):
        for letter in self.random_letter:
            if letter not in word:
                return letter
        return random.choice(self.random_letter)

    @staticmethod
    def random_letters():
        all_letters = list(string.ascii_letters)
        random.shuffle(all_letters)
        random_letters = ''.join(all_letters)
        return random_letters


class AddNumberRule(PasswordRule):
    def __init__(self, weight=1):
        self.is_repeatedly = False
        super().__init__(weight)

    def execute(self, word):
        self.counter += 1
        return self.upload_rule(word)

    def upload_rule(self, word):
        return word + self.analyze_number()

    def analyze_number(self):
        return str(random.randint(0, 9))


class AddNumberAtStartRule(PasswordRule):
    def __init__(self, weight=1):
        self.is_repeatedly = False
        super().__init__(weight)

    def execute(self, word):
        self.counter += 1
        return self.upload_rule(word)

    def upload_rule(self, word):
        return self.analyze_number() + word

    def analyze_number(self):
        return str(random.randint(0, 9))


# is_repeatedly = True
class ReplaceLetterRule(PasswordRule):
    def __init__(self, weight=1):
        super().__init__(weight)

    def execute(self, word):
        self.counter += 1
        return self.upload_rule(word)

    def upload_rule(self, word):
        return word.replace(*self.analyze_replace_letter(word))

    def analyze_replace_letter(self, word):
        replace_char = self.choose_random_character(word)
        similarity_dict = SIMILAR_CHARACTERS.get(replace_char.lower(), {})
        total_similarity = sum(similarity_dict.values())
        rand = random.uniform(0, total_similarity)
        return replace_char, next(
            (char for char, similarity in similarity_dict.items() if (rand := rand - similarity) < 0), replace_char)

    @staticmethod
    def choose_random_character(word):
        return random.choice(word)


class AddNumberAtRandomPositionRule(PasswordRule):
    def __init__(self, weight=1):
        super().__init__(weight)

    def execute(self, word):
        self.counter += 1
        return self.upload_rule(word)

    def upload_rule(self, word):
        random_index = random.randint(0, len(word))
        return word[:random_index] + self.analyze_number() + word[random_index:]

    def analyze_number(self):
        return str(random.randint(0, 9))


class RemoveLetterRule(PasswordRule):
    def __init__(self, weight=1):
        super().__init__(weight)

    def execute(self, word):
        self.counter += 1
        return self.upload_rule(word)

    def upload_rule(self, word):
        return word.replace(self.analyze_remove_letter(word), '')

    def analyze_remove_letter(self, word):
        return self.choose_random_character(word)

    @staticmethod
    def choose_random_character(word):
        return random.choice(word)


class RotateWordLeftRule(PasswordRule):
    def __init__(self, weight=1):
        super().__init__(weight)

    def execute(self, word):
        self.counter += 1
        return self.upload_rule(word)

    def upload_rule(self, word):
        return word[1:] + word[0] if word else word


class RotateWordRightRule(PasswordRule):
    def __init__(self, weight=1):
        super().__init__(weight)

    def execute(self, word):
        self.counter += 1
        return self.upload_rule(word)

    def upload_rule(self, word):
        return word[-1] + word[:-1] if word else word


class InsertCharacterAtRandomPositionRule(PasswordRule):
    def __init__(self, weight=1):
        super().__init__(weight)

    def execute(self, word):
        self.counter += 1
        return self.upload_rule(word)

    def upload_rule(self, word):
        random_index = random.randint(0, len(word))
        random_char = self.random_character()
        return word[:random_index] + random_char + word[random_index:]

    @staticmethod
    def random_character():
        return random.choice(string.ascii_letters)


class DeleteCharacterAtRandomPositionRule(PasswordRule):
    def __init__(self, weight=1):
        super().__init__(weight)

    def execute(self, word):
        self.counter += 1
        return self.upload_rule(word)

    def upload_rule(self, word):
        random_index = random.randint(0, len(word) - 1)
        return word[:random_index] + word[random_index + 1:]


class AddSpecialCharacterAtRandomPositionRule(PasswordRule):
    def __init__(self, weight=1):
        super().__init__(weight)
        self.special_char = random.choice(SPECIAL_CHARACTERS)

    def execute(self, word):
        self.counter += 1
        return self.upload_rule(word)

    def upload_rule(self, word):
        random_index = random.randint(0, len(word))
        return word[:random_index] + self.special_char + word[random_index:]
