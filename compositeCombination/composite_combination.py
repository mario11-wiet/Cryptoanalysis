import random

from rule.rule import PasswordRules


class CompositeCombination:
    def __init__(self, complexity_threshold=8):
        self.password_rules = PasswordRules()
        self.complexity_threshold = complexity_threshold

    def generate_password(self, length):
        password = ''
        for _ in range(length):
            composed_rule = self.compose_rule()
            password = composed_rule(password)
        return password

    def compose_rule(self):
        eligible_rules = self.get_eligible_rules()
        selected_rules = self.select_rules(eligible_rules)
        return self.combine_rules(selected_rules)

    def get_eligible_rules(self):
        return [rule for rule in self.password_rules.rules if self.is_rule_eligible(rule)]

    def is_rule_eligible(self, rule):
        return len(rule.__name__) <= self.complexity_threshold

    def select_rules(self, eligible_rules):
        return random.sample(eligible_rules, k=random.randint(1, len(eligible_rules)))

    def combine_rules(self, selected_rules):
        def composed_rule(password):
            transformed_password = password
            for rule in selected_rules:
                transformed_password = rule.transformation_function(transformed_password)
            return transformed_password
        return composed_rule