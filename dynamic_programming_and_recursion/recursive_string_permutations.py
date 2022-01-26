def get_permutations(string):
    # Base case
    if len(string) <= 1:
        return set([string])

    all_chars_except_last = string[:-1]
    last_char = string[-1]

    # Recursive call: get all possible permutations for all chars except last
    permutations_of_all_chars_except_last = get_permutations(all_chars_except_last)

    # Put the last chat in all possible positions for each of the above permutations
    permutations = set()
    for permutations_of_all_chars_except_last in permutations_of_all_chars_except_last:
        for position in range(len(all_chars_except_last) + 1):
            permutation = (
                permutations_of_all_chars_except_last[:position] 
                + last_char 
                + permutations_of_all_chars_except_last[position:]
            )
            permutations.add(permutation)

    return permutations

string = 'cats'

print(get_permutations(string))