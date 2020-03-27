import time

from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# original runtime: O(n^2) (technically O(n*m))
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# FIRST PASS SOLUTION
# t = BinarySearchTree(names_1[0])
# for name in names_1:
#     t.insert(name)
# # insertion of n elements is O(nlogn)

# for name in names_2:
#     if t.contains(name):
#         duplicates.append(name)
# assuming names_1 isn't in a hostile order, searching is O(logn) (so technically theta)

# runtime improvement on my computer: 9.1 seconds to 0.20 seconds

# STRETCH FROM README: only storing the names in lists
# Sort the first list and do binary search of it?

# sort_names = sorted(names_1)

# def find_name(name, floor, ceil):
#     mid = (ceil + floor) // 2
#     if sort_names[mid] == name:
#         return True
#     if mid == floor:
#         return False
#     elif name < sort_names[mid]:
#         return find_name(name, floor, mid)
#     else:
#         return find_name(name, mid, ceil)

# for name in names_2:
#     if find_name(name, 0, len(sort_names)):
#         duplicates.append(name)

# runtime on my computer: 0.08 seconds
# since the sorted list is effectively a balanced binary search tree,
# lookup time is definitely O(logn)
# timsort (Python's built-in SA) is O(nlogn)

# the solution more in line with the spirit of the problem would probably
# involve building the names_1 list from the file in a sorted way
# or a manually implemented in-place SA

# STRETCH 2.0: MINIMIZE RUNTIME WITHOUT IMPORTS
# try converting list to dict for constant lookup time?

di = {name: None for name in names_1}

for name in names_2:
    if name in di:
        duplicates.append(name)

# runtime: 0.009 seconds
# O(n) solution!! (technically O(n+m))

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
