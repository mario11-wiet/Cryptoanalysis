import random

from Algorithm.rule.rule import PasswordRules


class IterativeCombination:
    def __init__(self):
        self.password_rules = PasswordRules()

    def generate_password(self, length, num_iterations=3):
        password = ''
        for _ in range(length):
            for _ in range(num_iterations):
                chosen_rule = self.choose_rule()
                password = chosen_rule.transformation_function(password)
        return password

    def choose_rule(self):
        weighted_rules = self.weight_rules()
        rules, weights = zip(*weighted_rules.items())
        chosen_rule = random.choices(rules, weights=weights)[0]
        return chosen_rule

    def weight_rules(self):
        rule_weights = {rule: rule.weight for rule in self.password_rules.rules}
        return rule_weights
