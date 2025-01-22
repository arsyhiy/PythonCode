import heapq

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3, nums)) # Выведет [42, 37, 23]
print(heapq.nsmallest(3, nums)) # выведет [-4, 1, 2]



