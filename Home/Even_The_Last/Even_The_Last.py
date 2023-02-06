def checkio(array: list[int]) -> int:
    parzyste= 0
    if len(array) == 0:
        return 0 
    
    ostatni_element= array[-1]
    for i, x in enumerate(array):
        if i % 2 == 0:
          parzyste += x
       
    return parzyste * ostatni_element
    
   

print("Example:")
print(checkio([0, 1, 2, 3, 4, 5]))

assert checkio([0, 1, 2, 3, 4, 5]) == 30
assert checkio([1, 3, 5]) == 30
assert checkio([6]) == 36
assert checkio([]) == 0

print("The mission is done! Click 'Check Solution' to earn rewards!")

