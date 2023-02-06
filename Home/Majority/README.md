We have a list of booleans. Let's check if the majority of elements are True.

example

Some cases worth mentioning: 1) an empty list should return False; 2) if True-s and False-s have an equal amount, function should return False.

Input: A list of booleans.

Output: A Boolean.

Examples:

assert is_majority([True, True, False, True, False]) == True
assert is_majority([True, True, False]) == True
assert is_majority([True, True, False, False]) == False
assert is_majority([True, True, False, False, False]) == False
