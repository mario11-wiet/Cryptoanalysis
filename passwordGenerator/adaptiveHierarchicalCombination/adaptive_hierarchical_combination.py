import random

from passwordGenerator.rule.rule import PasswordRules


class AdaptiveHierarchicalCombination:
    def __init__(self):
        self.password_rules = PasswordRules()
        self.history = []

    def generate_password(self, length, complexity_threshold=8):
        password = ''
        for _ in range(length):
            chosen_rule = self.choose_rule(complexity_threshold)
            password += chosen_rule(password)
        return password

    def choose_rule(self, complexity_threshold):
        if len(self.history) == 0 or len(self.history[-1]) < complexity_threshold:
            return self.password_rules.rule_add_suffix
        else:
            filtered_rules = self.filter_rules_based_on_history()
            return random.choice(filtered_rules)

    def filter_rules_based_on_history(self):
        filtered_rules = [rule for rule in self.password_rules.rules if rule not in [PasswordRules.rule_remove_letter]]
        return filtered_rules

    def update_history(self, password):
        self.history.append(password)
