import random

from rule.rule import PasswordRules


class SelectiveCombination:
    def __init__(self):
        self.password_rules = PasswordRules()

    def generate_password(self, length, complexity_threshold=8):
        password = ''
        for _ in range(length):
            chosen_rule = self.choose_rule(complexity_threshold, password)
            password += chosen_rule(password)
        return password

    def choose_rule(self, complexity_threshold, password):
        eligible_rules = self.get_eligible_rules(complexity_threshold, password)
        selected_rule = self.select_rule(eligible_rules)
        return selected_rule

    def get_eligible_rules(self, complexity_threshold, password):
        eligible_rules = []
        for rule in self.password_rules.rules:
            if self.is_rule_eligible(rule, complexity_threshold, password):
                eligible_rules.append(rule)
        return eligible_rules

    def is_rule_eligible(self, rule, complexity_threshold, password):
        return len(rule.__name__) <= complexity_threshold

    def select_rule(self, eligible_rules):
        if eligible_rules:
            return random.choice(eligible_rules)
        else:
            return self.password_rules.rule_lowercase_letters
