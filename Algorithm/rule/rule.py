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
            AddSuffixRule(),
            AddNumberRule(),
            ReplaceLetterRule(),
            RemoveLetterRule(),
            ReverseLettersRule(),
            UppercaseLettersRule(),
            LowercaseLettersRule(),
            RemoveDigitsRule(),
            ReplaceSpacesRule()
        ]

    def sort_rules(self):
        sorted_rules = sorted(self.rules, key=lambda rule: rule.weight / rule.counter)
        return sorted_rules

class PasswordRule:
    def __init__(self, weight=1):
        self.weight = weight
        self.counter = 0
        self.is_repeatedly = True
        self.rules = {}

    def add_rule(self, rule):
        if rule not in self.rules:
            self.rules[rule] = 1
        else:
            self.rules[rule] += 1

    def most_common_rules(self, number):
        sorted_rules = sorted(self.rules.items(), key=lambda x: x[1], reverse=True)
        best_rules = sorted_rules[:number]
        return best_rules


    def execute(self, word):
        self.counter += 1
        return word


class AddUppercaseRule(PasswordRule):
    def __init__(self, weight=1):
        super().__init__(weight)
        self.is_repeatedly = False

    def execute(self, word):
        self.counter += 1
        return word.capitalize()


class AddSuffixRule(PasswordRule):
    def __init__(self, suffix='a', weight=1):
        super().__init__(weight)
        self.suffix = suffix

    def execute(self, word):
        self.counter += 1
        return word + self.suffix


class AddNumberRule(PasswordRule):
    def __init__(self, number=1, weight=1):
        super().__init__(weight)
        self.number = number

    def execute(self, word):
        self.counter += 1
        return word + str(self.number)


class ReplaceLetterRule(PasswordRule):
    def __init__(self, old_letter='q', new_letter='a', weight=1):
        super().__init__(weight)
        self.old_letter = old_letter
        self.new_letter = new_letter

    def execute(self, word):
        self.counter += 1
        return word.replace(self.old_letter, self.new_letter)


class RemoveLetterRule(PasswordRule):
    def __init__(self, letter='a', weight=1):
        super().__init__(weight)
        self.letter = letter

    def execute(self, word):
        self.counter += 1
        return word.replace(self.letter, '')


class ReverseLettersRule(PasswordRule):
    def __init__(self, weight=1):
        super().__init__(weight)
        self.is_repeatedly = False
    def execute(self, word):
        self.counter += 1
        return word[::-1]


class UppercaseLettersRule(PasswordRule):
    def __init__(self, weight=1):
        super().__init__(weight)
        self.is_repeatedly = False
    def execute(self, word):
        self.counter += 1
        return word.upper()


class LowercaseLettersRule(PasswordRule):
    def __init__(self, weight=1):
        super().__init__(weight)
        self.is_repeatedly = False
    def execute(self, word):
        self.counter += 1
        return word.lower()


class RemoveDigitsRule(PasswordRule):
    def __init__(self, weight=1):
        super().__init__(weight)
        self.is_repeatedly = False
    def execute(self, word):
        self.counter += 1
        return ''.join(char for char in word if not char.isdigit())


class ReplaceSpacesRule(PasswordRule):
    def __init__(self, weight=1):
        super().__init__(weight)
        self.is_repeatedly = False

    def execute(self, word):
        self.counter += 1
        return word.replace(' ', '_')
