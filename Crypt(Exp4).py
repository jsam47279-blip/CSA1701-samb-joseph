from itertools import permutations

def solve_cryptarithmetic(words, result_word):
    letters = set("".join(words) + result_word)

    if len(letters) > 10:
        return None

    letters = list(letters)
    leading = {w[0] for w in words + [result_word]}

    for perm in permutations(range(10), len(letters)):
        mapping = dict(zip(letters, perm))

        if any(mapping[l] == 0 for l in leading):
            continue

        def to_num(word):
            return int("".join(str(mapping[c]) for c in word))

        if sum(to_num(w) for w in words) == to_num(result_word):
            return mapping

    return None

words = ["SEND", "MORE"]
result_word = "MONEY"

mapping = solve_cryptarithmetic(words, result_word)

if mapping:
    print(mapping)
else:
    print("No solution found.")
