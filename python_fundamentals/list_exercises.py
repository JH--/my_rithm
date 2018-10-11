# Write the following Python code to do the following (complete ALL of these
# using list comprehension).

# Given a list [1,2,3,4], print out all the values in the list.
print([i for i in [1, 2, 3, 4]])

# Given a list [1,2,3,4], print out all the values in the list multiplied by 20.
print([i*20 for i in [1, 2, 3, 4]])

# Given a list ["Elie", "Tim", "Matt"], return a new list with only the first
# letter (["E", "T", "M"]).
new_list = [name[0] for name in ["Elie", "Tim", "Matt"]]

# Given a list [1,2,3,4,5,6] return a new list of all the even values ([2,4,6]).
new_list = [i for i in range(1, 7) if i % 2 == 0]

# Given two lists [1,2,3,4] and [3,4,5,6], return a new list that is the
# intersection of the two ([3,4]).
new_list = [i for i in range(1, 5) if i in range(3, 7)]

# Given a list of words ["Elie", "Tim", "Matt"] return a new list with each word
# reversed and in lower case (['eile', 'mit', 'ttam']).
new_list = [name.lower()[::-1] for name in ["Elie", "Tim", "Matt"]]

# Given two strings "first" and "third", return a new string with all the letters
# present in both words (["i", "r", "t"]).
''.join([i for i in "first" if i in "third"])

# For all the numbers between 1 and 100, return a list with all the numbers that
# are divisible by 12 ([12, 24, 36, 48, 60, 72, 84, 96]).
print([i for i in range(1, 100) if i % 12 == 0])

# Given the string "amazing", return a list with all the vowels removed (['m', 'z', 'n', 'g']).
[i for i in "amazing" if i not in "aeiou"]

# Generate a list with the value [[0, 1, 2], [0, 1, 2], [0, 1, 2]].
new_list = [[0, 1, 2]]*3

# Generate a list with the value:
#
# [
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# ]
new_list = [list(range(10))] * 10
