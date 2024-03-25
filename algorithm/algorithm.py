import random
import string
from typing import List

class PasswordGenerator:
    def __init__(self, base_password: str) -> None:
        self.base_password: str = base_password
        self.tree_structure: dict = {}
        self.generated_passwords: List[str] = []

    def adaptive_hierarchical_adjustment(self) -> None:
        rules_frequency: dict = {}
        for password in self.generated_passwords:
            for rule in password:
                rules_frequency[rule] = rules_frequency.get(rule, 0) + 1


    def parallel_transformation(self) -> None:
        for password in self.generated_passwords:
            transformed_password: str = password
            rules_to_apply: List[str] = ['uppercase', 'reverse']
            for rule in rules_to_apply:
                transformed_password = self._apply_rule(rule, transformed_password)
            self.generated_passwords.append(transformed_password)

    def selective_application(self) -> None:
        for password in self.generated_passwords:
            if len(password) > 10:
                password = self._apply_rule('special_characters', password)
        pass

    def iterative_reinforcement(self) -> None:
        for password in self.generated_passwords:
            for _ in range(2):
                password = self._apply_rule('reverse', password)
        pass

    def composite_rule_generation(self,password) -> None:
        composite_rules: List[str] = ['uppercase_digits', 'lowercase_special_characters']
        for rule in composite_rules:
            if 'uppercase_digits' in rule:
                password = self._apply_rule('uppercase', password)
                password = self._apply_rule('digits', password)
            elif 'lowercase_special_characters' in rule:
                password = self._apply_rule('lowercase', password)
                password = self._apply_rule('special_characters', password)
        pass

    def tree_expansion(self) -> None:
        expanded_tree = self.tree_structure.copy()
        expanded_tree['additional_rule'] = 'digits'
        self.tree_structure = expanded_tree

    def password_candidate_selection(self) -> str:
        return random.choice(self.generated_passwords)

    def generate_password(self) -> str:
        self.adaptive_hierarchical_adjustment()
        self.parallel_transformation()
        self.selective_application()
        self.iterative_reinforcement()
        self.composite_rule_generation()
        self.tree_expansion()
        return self.password_candidate_selection()

    def _apply_rule(self, rule: str, password: str) -> str:
        if rule == 'uppercase':
            return password.upper()
        elif rule == 'lowercase':
            return password.lower()
        elif rule == 'digits':
            return password + random.choice(string.digits)
        elif rule == 'special_characters':
            return password + random.choice(string.punctuation)
        elif rule == 'reverse':
            return password[::-1]
        else:
            return password

    def _apply_rules(self, rules: List[str], password: str) -> str:
        for rule in rules:
            password = self._apply_rule(rule, password)
        return password

    def _generate_rules(self) -> List[str]:
        rules: List[str] = ['uppercase', 'lowercase', 'digits', 'special_characters', 'reverse']
        return rules

    def _generate_passwords(self, rules: List[str]) -> None:
        for _ in range(10):
            new_password: str = self._apply_rules(rules, self.base_password)
            self.generated_passwords.append(new_password)

base_password: str = "myBasePassword123"
generator: PasswordGenerator = PasswordGenerator(base_password)
generator._generate_passwords(generator._generate_rules())
generated_password: str = generator.generate_password()
print("Generated Password:", generated_password)
