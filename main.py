LONG_WORD = 10
DELTA_BUDGET = 0.2


def rule_add_uppercase(word):
    return word.capitalize()


def rule_add_suffix(word, suffix='a'):
    return word + suffix


def rule_add_number(word, number=1):
    return word + str(number)


def rule_replace_letter(word, old_letter='q', new_letter='a'):
    return word.replace(old_letter, new_letter)


def rule_remove_letter(word, letter='a'):
    return word.replace(letter, '')


def rule_reverse_letters(word):
    return word[::-1]


def rule_uppercase_letters(word):
    return word.upper()


def rule_lowercase_letters(word):
    return word.lower()


def rule_remove_digits(word):
    return ''.join(char for char in word if not char.isdigit())


def rule_replace_spaces(word):
    return word.replace(' ', '_')


def analyze_word(word):
    length = len(word)
    has_special_chars = any(not char.isalnum() for char in word)
    has_digits = any(char.isdigit() for char in word)
    has_lowercase = any(char.islower() for char in word)
    has_uppercase = any(char.isupper() for char in word)
    starts_with_uppercase = word[0].isupper() if length > 0 else False
    is_palindrome = word.lower() == word.lower()[::-1]
    vowels = [char for char in word.lower() if char in 'aeiou']

    result = {
        'length': length,
        'has_special_chars': has_special_chars,
        'has_digits': has_digits,
        'has_lowercase': has_lowercase,
        'has_uppercase': has_uppercase,
        'starts_with_uppercase': starts_with_uppercase,
        'is_palindrome': is_palindrome,
        'vowels': vowels
    }

    return result


def evaluate_rule(analyze, rule):
    score = 0

    if rule == "rule_add_uppercase":
        if not analyze['starts_with_uppercase']:
            score += 1
        if not analyze['has_uppercase']:
            score += 1
        if analyze['length'] >= LONG_WORD:
            score += 1
        if analyze['has_digits']:
            score += 1
        if analyze['has_special_chars']:
            score += 1

    if rule == "rule_add_number":
        if analyze['has_digits']:
            score -= 1
        else:
            score += 1
        if analyze['length'] < LONG_WORD:
            score += 1
        if analyze['has_special_chars']:
            score += 1
        if analyze['has_lowercase'] and analyze['has_uppercase']:
            score += 1

    if rule == "rule_add_suffix":
        if analyze['length'] < LONG_WORD:
            score += 1
        if analyze['length'] >= LONG_WORD:
            score -= 1
        if analyze['has_lowercase'] and analyze['has_uppercase']:
            score += 1
        if analyze['is_palindrome']:
            score -= 1
        if analyze['starts_with_uppercase']:
            score += 1

    if rule == "rule_replace_letter":
        if analyze['has_lowercase'] and analyze['has_uppercase']:
            score += 1
        if analyze['has_digits']:
            score += 1
        if analyze['has_special_chars']:
            score += 1
        if analyze['has_digits'] and analyze['has_special_chars']:
            score += 1
        if analyze['has_digits'] and analyze['has_lowercase'] and analyze['has_uppercase']:
            score -= 1

    if rule == "rule_remove_letter":
        if analyze['length'] >= LONG_WORD:
            score += 1
        if analyze['has_lowercase'] and analyze['has_uppercase']:
            score += 1
        if analyze['has_digits']:
            score += 1
        if analyze['has_special_chars']:
            score += 1
        if analyze['length'] >= LONG_WORD and analyze['has_digits']:
            score += 1
        if analyze['length'] >= LONG_WORD and analyze['has_digits'] and analyze['has_special_chars']:
            score -= 1

    if rule == "rule_reverse_letters":
        if analyze['is_palindrome']:
            score += 1
        if analyze['has_lowercase'] and analyze['has_uppercase']:
            score += 1
        if analyze['length'] >= LONG_WORD and analyze['has_digits']:
            score += 1
        if analyze['has_special_chars']:
            score += 1
        if analyze['length'] >= LONG_WORD and analyze['is_palindrome']:
            score += 1
        if analyze['length'] >= LONG_WORD and analyze['is_palindrome'] and analyze['has_special_chars']:
            score -= 1

    if rule == "rule_uppercase_letters":
        if analyze['has_lowercase']:
            score += 1
        if analyze['has_digits']:
            score += 1
        if analyze['has_special_chars']:
            score += 1
        if analyze['has_digits'] and analyze['has_special_chars']:
            score += 1
        if analyze['length'] >= LONG_WORD and analyze['has_digits'] and analyze['has_special_chars']:
            score += 1
        if analyze['length'] >= LONG_WORD and analyze['has_digits'] and analyze['has_special_chars'] and analyze['has_lowercase']:
            score -= 1

    if rule == "rule_lowercase_letters":
        if analyze['has_uppercase']:
            score += 1
        if analyze['has_digits']:
            score += 1
        if analyze['has_special_chars']:
            score += 1
        if analyze['has_digits'] and analyze['has_special_chars']:
            score += 1
        if analyze['length'] >= LONG_WORD and analyze['has_digits'] and analyze['has_special_chars']:
            score += 1
        if analyze['length'] >= LONG_WORD and analyze['has_digits'] and analyze['has_special_chars'] and analyze['has_uppercase']:
            score -= 1

    if rule == "rule_remove_digits":
        if analyze['length'] >= LONG_WORD:
            score += 1
        if analyze['has_lowercase'] and analyze['has_uppercase']:
            score += 1
        if analyze['has_special_chars']:
            score += 1
        if analyze['has_lowercase'] and analyze['has_uppercase'] and analyze['has_special_chars']:
            score += 1
        if analyze['length'] >= LONG_WORD and analyze['has_lowercase'] and analyze['has_uppercase'] and analyze['has_special_chars']:
            score -= 1
        if analyze['length'] >= LONG_WORD and analyze['has_lowercase'] and analyze['has_uppercase'] and analyze['has_special_chars'] and analyze['has_digits']:
            score -= 1

    if rule == "rule_replace_spaces":
        if analyze['length'] >= LONG_WORD:
            score += 1
        if analyze['has_lowercase'] and analyze['has_uppercase']:
            score += 1
        if analyze['has_digits']:
            score += 1
        if analyze['has_special_chars']:
            score += 1
        if analyze['length'] >= LONG_WORD and analyze['has_lowercase'] and analyze['has_uppercase']:
            score += 1
        if analyze['length'] >= LONG_WORD and analyze['has_lowercase'] and analyze['has_uppercase'] and analyze['has_digits']:
            score -= 1

    # score range -5,5

    # normalization
    return (score + 5) / (max(10, score + 5))


def calculate_compatibility(word, rules):
    word_analysis = analyze_word(word)
    compatibility = {}
    for rule in rules:
        rule_score = evaluate_rule(word_analysis, rule)
        compatibility.update({rule: rule_score})
    return compatibility


def update_budget(budget, rule_chosen, rules, value=0.2):
    for rule in rules:
        if rule != rule_chosen:
            budget[rule] = max(0.1, budget[rule] - (value / (len(rules) - 1)))
        else:
            budget[rule] = min(0.9, budget[rule] + value)

    return budget


def get_compatible_rules(budgets, word_compatibility):
    result = []
    for rule, compatibility in word_compatibility.items():
        if compatibility > 1 - budgets[rule]:
            result.append(rule)
    return result


def main_function():
    words = ["kamil"]
    rules = ["rule_add_uppercase", "rule_add_suffix", "rule_add_number"]
    passwords = ["kamil1", "Kamil", "kabel"]

    # initial compatibility
    compatibility = {}
    for word in words:
        compatibility[word] = calculate_compatibility(word, rules)

    # initial budget
    budgets = {}
    for rule in rules:
        budgets[rule] = 0.5

    # initial rule score
    rules_score = {}
    for rule in rules:
        rules_score[rule] = 0

    guessed_word = []

    for word in words:
        for rule in get_compatible_rules(budgets, compatibility[word]):
            guess = eval(rule)(word)
            print(guess)
            if guess in passwords and guess != word:
                print(guess, "guessed!")
                guessed_word.append(guess)
                # update stats
                rules_score[rule] += 1
                # add guess to the words
                words.append(guess)
                # update compatibility
                compatibility[guess] = calculate_compatibility(guess, rules)
                # increase budget for a rule, normalize all budgets, add to one budget, take from others
                # add inversely proportional value
                value = DELTA_BUDGET / rules_score[rule]
                budgets = update_budget(budgets, rule, rules, value)

    return guessed_word


# run
result = main_function()
print("Guessed: ", result)

# kamil -> [0.5, 0.5]

# kabel


#
# kamil

# kamil123, Kamil123!, kamil1

# Kompatyblinosc
# 10 rule -> kamil-> analizuje -> wyliczamy kompablitycznosc dla tego slowa dla zasad

# kamil -> kamil1, Kamil, kamil!, kami, kamik

# kamil1_> 5 kolejnych, Kamil -> 5 kolejnych, kamil! -> 5 kolejnych, kami -> 5 kolejnych, kamik -> 5 kolejnych

# kamil -> kamil123

# kamil -> kamil12345 -> zla droga

# kamil

# Kamil1!
# Kamil2
# 1Kamil1