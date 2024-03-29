import math
import random

from Algorithm.passwordGenerator.constants import min_rule, max_rule
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
            nodes_at_level.extend(find_nodes_at_level(child, target_level, current_level + 1))

    return nodes_at_level

class PasswordGenerator:
    def __init__(self, base_password: str, num_levels: int,size_of_level:int = 10, percentage_of_candidates: float = 0.7):
        self.base_password = base_password
        self.tree = None
        self.num_levels = num_levels
        self.current_level = 0
        self.size_of_level = size_of_level
        self.percentage_of_candidates = percentage_of_candidates
        self.password_rules = PasswordRules()

    def execute_algorithm(self):
        self.initialize()

        for step in range(num_levels):
            self.one_step(step)
            self.current_level += 1

        # Krok 8: Wybór kandydatów na hasło
        return self.password_candidate_selection()

    def initialize(self):
        self.tree = TreeNode(self.base_password)


    def one_step(self, step):

        candidates = self.check_candidate(step)

        self.check_rules(candidates)

        self.create_tree(candidates)

        # Krok 2: Dynamiczna modyfikacja hierarchiczna
        self.adaptive_hierarchical_adjustment()

        # Krok 3: Równoległa transformacja
        self.parallel_transformation()

        # Krok 4: Selektywne stosowanie
        self.selective_application()

        # Krok 5: Iteracyjne wzmacnianie
        self.iterative_reinforcement()

        # Krok 6: Generowanie złożonych reguł
        self.composite_rule_generation()

        # Krok 7: Rozszerzenie drzewa
        self.tree_expansion()

    def check_candidate(self, step):
        all_candidates = find_nodes_at_level(self.tree,step)
        number_of_candidate = math.ceil(self.percentage_of_candidates * len(all_candidates))

        sorted_candidates = sorted(all_candidates, key=lambda node: node.strength_metric, reverse=True)
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
            num_rules = random.randint(min_rule, max_rule)
            selected_rules = random.sample(self.password_rules.rules, num_rules)

            new_child = TreeNode(self.tree.initial_word,self.tree,selected_rules)
            new_child.uplay_rules()
            self.tree.add_child(new_child)

    def create_nodes(self, candidates):

        for candidate in candidates:
            for _ in range(self.size_of_level):
                pass

        pass

    def create_node(self, candidate):
        pass

    def adaptive_hierarchical_adjustment(self):
        # Implementacja dynamicznej modyfikacji hierarchicznej
        pass

    def parallel_transformation(self):
        # Implementacja równoległej transformacji
        pass

    def selective_application(self):
        # Implementacja selektywnego stosowania
        pass

    def iterative_reinforcement(self):
        # Implementacja iteracyjnego wzmacniania
        pass

    def composite_rule_generation(self):
        # Implementacja generowania złożonych reguł
        pass

    def tree_expansion(self):
        # Implementacja rozszerzenia drzewa
        pass

    def password_candidate_selection(self):
        # Implementacja wyboru kandydatów na hasło
        pass

# Przykładowe użycie
base_password = "initial_password"
initial_tree = {}  # Tutaj możesz zainicjalizować początkową strukturę drzewa
num_levels = 3  # Liczba poziomów drzewa do rozwinięcia

password_generator = PasswordGenerator(base_password, initial_tree, num_levels)
generated_password = password_generator.execute_algorithm()
print("Generated password:", generated_password)