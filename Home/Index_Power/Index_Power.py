def index_power(array: list, n: int) -> int:
    dlugosc= len(array)
    if dlugosc > n:
      potega= array[n]**n
      return potega
    else:
      return -1


print("Example:")
print(index_power([1, 2, 3], 2))

assert index_power([1, 2, 3, 4], 2) == 9
assert index_power([1, 3, 10, 100], 3) == 1000000
assert index_power([0, 1], 0) == 1
assert index_power([1, 2], 3) == -1

print("The mission is done! Click 'Check Solution' to earn rewards!")

