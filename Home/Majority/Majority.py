def is_majority(items: list[bool]) -> bool:
  count= (items.count(True))
  count2= (items.count(False))
  if count > count2:
      return True
  else:
      return False
    


print("Example:")
print(is_majority([True, True, False, True, False]))

assert is_majority([True, True, False, True, False]) == True
assert is_majority([True, True, False]) == True
assert is_majority([True, True, False, False]) == False
assert is_majority([True, True, False, False, False]) == False
assert is_majority([False]) == False
assert is_majority([True]) == True
assert is_majority([]) == False

print("The mission is done! Click 'Check Solution' to earn rewards!")

