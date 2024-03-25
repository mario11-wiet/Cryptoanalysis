import random

from passwordGenerator.rule.rule import PasswordRules


class ParallelCombination:
    def __init__(self):
        self.password_rules = PasswordRules()

    def generate_password(self, length, num_rules_to_apply=3):
        password = ''
        for _ in range(length):
            chosen_rules = random.sample(self.password_rules.rules, num_rules_to_apply)
            transformed_characters = [rule(password) for rule in chosen_rules]
            password += ''.join(transformed_characters)
            self.update_rules_weight(chosen_rules)
        return password

    def update_rules_weight(self, chosen_rules):
        for rule in chosen_rules:
            rule.weight += 1

        total_weight = sum(rule.weight for rule in self.password_rules.rules)
        for rule in self.password_rules.rules:
            rule.weight /= total_weight