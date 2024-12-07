from part_one import CompositeRule, PrecedenceRule
from common import load_rules_and_updates


def main():
    rules, updates = load_rules_and_updates()
    composite_rule = CompositeRule()
    for pre, post in rules:
        composite_rule.add_rule(PrecedenceRule(pre, post))

    middles = 0
    for update in updates:
        if composite_rule.is_satisfied_by(update):
            middles += update[len(update) // 2]

    print(middles)


main()