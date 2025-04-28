t1 = ((1, 2), (3, 4), (5, 6)) 
swapped_tuples = tuple((b, a) for a, b in t1)
print("Swapped tuple of tuples:", swapped_tuples)
