from password_strength import PasswordStats
import Levenshtein
import zxcvbn

from Algorithm.passwordGenerator.constants import MAX_LENGTH


class TreeNode:
    def __init__(self, initial_word,parent = None, rule = []):
        self.processed = False
        self.parent = parent
        self.children = []
        self.used_rules = rule
        self.used_rules_from_node = rule if not self.parent else self.parent.used_rules + rule
        self.current_word = initial_word if not parent else parent.current_word
        self.initial_word = initial_word
        self.strength_metric = 0
        self.difference_metric = 0
        self.level = 0 if not self.parent else self.parent.level + 1

    def upload_rules(self):
        for rule in self.used_rules:
            self.current_word = rule.execute(self.current_word)

        self.update_metrics()
        self.reject_passwords()


    def reject_passwords(self):
        if len(self.current_word) > MAX_LENGTH:
            self.mark_as_processed()
        if self.difference_metric == 0:
            self.mark_as_processed()

    def add_child(self, child):
        self.children.append(child)

    def remove_child(self, child):
        if child in self.children:
            self.children.remove(child)
            child.parent = None

    def calculate_strength_metric(self):
        strength = PasswordStats(self.current_word)
        zxcvbn_strength = zxcvbn.zxcvbn(self.current_word)['score'] / 4.0
        return (strength.strength() + zxcvbn_strength)/2

    def calculate_difference_metric(self):
        diff = Levenshtein.ratio(self.initial_word,self.current_word)
        return diff

    def update_metrics(self):
        self.strength_metric = self.calculate_strength_metric()
        self.difference_metric = self.calculate_difference_metric()

    def find_child(self, target_word):
        for child in self.children:
            if child.current_word == target_word:
                return child
        return None

    def mark_as_processed(self):
        self.processed = True

    def __repr__(self):
        return f"TreeNode: {self.current_word}, Strength: {self.strength_metric}, Difference: {self.difference_metric}"
