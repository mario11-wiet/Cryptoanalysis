import math
import random

from Algorithm.passwordGenerator.constants import MAX_RULE, MIN_RULE
from Algorithm.passwordGenerator.tree_node import TreeNode
from Algorithm.rule.rule import PasswordRules

def find_nodes_at_level(root, target_level, current_level=0):
    """
        Recursive function to find nodes at a specified level in a tree.

        :param root: The starting node (root) of the tree.
        :param target_level: The level at which we are searching for nodes.
        :param current_level: The current level in the tree (defaults to 0).
        :return: A list of nodes at the specified level.
    """
    nodes_at_level = []

    if current_level == target_level:
        nodes_at_level.append(root)
    elif current_level < target_level:
        for child in root.children:
            if not child.processed:
                nodes_at_level.extend(find_nodes_at_level(child, target_level, current_level + 1))

    return nodes_at_level

class PasswordGenerator:
    def __init__(self, base_password: str = "mariusz", num_levels: int = 3,size_of_level:int = 12, percentage_of_candidates: float = 0.5):
        self.base_password = base_password
        self.tree = None
        self.num_levels = num_levels
        self.current_level = 0
        self.size_of_level = size_of_level
        self.percentage_of_candidates = percentage_of_candidates
        self.password_rules = PasswordRules()

#ptopa
    def execute_algorithm(self):
        self.initialize()

        for step in range(self.num_levels):
            print(step)
            self.one_step(step)
            self.current_level += 1

        all_candidates = find_nodes_at_level(self.tree, self.current_level)
        return self.password_candidate_selection(all_candidates)

    def initialize(self):
        self.tree = TreeNode(self.base_password)


    def one_step(self, step):

        candidates = self.check_candidate(step)

        self.check_rules(candidates)

        self.create_tree(candidates)

        self.clean()

    def clean(self):
        for rule in self.password_rules.rules:
            rule.weight = 0
            rule.counter = 0
            rule.rules = {}


    def check_candidate(self, step):
        all_candidates = find_nodes_at_level(self.tree,step)
        number_of_candidate = math.ceil(self.percentage_of_candidates * len(all_candidates))

        sorted_candidates = sorted(all_candidates, key=lambda node: node.strength_metric* node.difference_metric, reverse=True)
        selected_candidates = sorted_candidates[:number_of_candidate]

        [candidate.mark_as_processed() for candidate in sorted_candidates if candidate not in selected_candidates]

        return selected_candidates

    def check_rules(self, candidates):
        for candidate in candidates:
            for rule in candidate.used_rules:
                rule.weight += 1
                for other_rule in candidate.used_rules:
                    if rule != other_rule:
                        rule.add_rule(other_rule)


    def create_tree(self, candidates):
        if self.current_level == 0:
            self.create_first_nodes()
        else:
            self.create_nodes(candidates)

    def create_first_nodes(self):
        for _ in range(self.size_of_level):
            selected_rules = self.selected_rules()
            self.create_children(self.tree.initial_word,self.tree, selected_rules)

    def create_nodes(self, candidates):
        for candidate in candidates:
            random_number = random.randint(1, math.ceil(self.size_of_level/2))
            number = self.size_of_level-random_number
            created_rules = self.create_best_rules(number)
            for node in range(number):
                self.create_children(self.tree.initial_word, candidate, created_rules[node])
            for _ in range(random_number):
                selected_rules = self.selected_rules()
                self.create_children(self.tree.initial_word,candidate,selected_rules)

    def create_children(self, initial_word, parent, selected_rules):
        new_child = TreeNode(initial_word, parent, selected_rules)
        new_child.upload_rules()
        parent.add_child(new_child)

    def selected_rules(self):
        num_rules = random.randint(MIN_RULE, MAX_RULE)
        selected_rules = []
        repeated_rules_count = 0

        while len(selected_rules) < num_rules:
            rule = random.choice(self.password_rules.rules)
            if rule in selected_rules and not rule.is_repeatedly:
                continue
            else:
                selected_rules.append(rule)
                if not rule.is_repeatedly:
                    repeated_rules_count += 1

        return selected_rules

    def create_best_rules(self, number):
        created_rules = []
        sorted_rules = self.password_rules.sort_rules()
        for sorted_rule in sorted_rules:
            num_rules = random.randint(MIN_RULE, MAX_RULE)
            if num_rules == 1:
                created_rules.append([sorted_rule])
            else:
                rules = [sorted_rule] + sorted_rule.most_common_rules(num_rules - 1)
                created_rules.append(rules)
            if len(created_rules) > number:
                break
        return created_rules

    @staticmethod
    def password_candidate_selection(candidates):
        password_candidate = []
        candidates.sort(key=lambda x: x.difference_metric*x.strength_metric,reverse=True)
        for candidate in candidates:
            password_candidate.append(candidate.current_word) #, candidate.difference_metric, candidate.strength_metric, candidate.used_rules_from_node

        print(f"{len(candidates)}, {len(password_candidate)}")
        return password_candidate

