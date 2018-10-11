from functools import reduce
from operator import mul as multiply
from collections import Counter


# Part I
# Write the following functions
#
# difference
# this function takes in two parameters and returns the difference between the two
# difference(2,2) # 0
# difference(0,2) # -2


def difference(a, b):
    return a - b

# product
# this function takes in two parameters and returns the product of the two
# product(2,2) # 4
# product(0,2) # 0


def product(a, b):
    return a * b

# print_day
# this function takes in one parameter (a number from 1-7) and returns the day
#  of the week (1 is Sunday, 2 is Monday, 3 is Tuesday etc.). If the number is
#  less than 1 or greater than 7, the function should return None
# print_day(4) # "Wednesday"
# print_day(41) # None


def print_day(day=0):
    days = {k: v for k, v in zip(
        range(1, 8), "Sunday Monday Tuesday Wednesday Thursday Friday Saturday".split())}
    return days.get(day)


# last_element
# this function takes in one parameter (a list) and returns the last
# value in the list. It should return None if the list is empty.
# last_element([1,2,3,4]) # 4
# last_element([]) # None

def last_element(lst=[]):
    return lst[-1] if lst else None

# number_compare
# this function takes in two parameters (both numbers). If the first is greater
# than the second, this function returns "First is greater." If the second
# number is greater than the first, the function returns "Second is greater."
# Otherwise the function returns "Numbers are equal."
# number_compare(1,1) # "Numbers are equal"
# number_compare(1,2) # "Second is greater"
# number_compare(2,1) # "First is greater"


def number_compare(a, b):
    if a > b:
        return "First is greater"
    elif a < b:
        return "Second is greater"
    else:
        return "Numbers are equal"


# single_letter_count
# this function takes in two parameters (two strings). The first parameter
# should be a word and the second should be a letter. The function returns
# the number of times that letter appears in the word. The function should
# be case insensitive (does not matter if the input is lowercase or uppercase).
# If the letter is not found in the word, the function should return 0.
# single_letter_count('amazing','A') # 2

def single_letter_count(word, letter):
    return word.lower().count(letter.lower())


# multiple_letter_count
# this function takes in one parameter (a string) and returns a dictionary
# with the keys being the letters and the values being the count of the letter.
# multiple_letter_count("hello") # {h:1, e: 1, l: 2, o:1}
# multiple_letter_count("person") # {p:1, e: 1, r: 1, s:1, o:1, n:1}

def multiple_letter_count(string):
    return {i: string.count(i) for i in string}


# list_manipulation
# this function should take in three parameters (a list, command, location and value).
# If the command is "remove" and the location is "end", the function should remove the
#  last value in the list and return the value removed
# If the command is "remove" and the location is "beginning", the function should remove
#  the first value in the list and return the value removed
# If the command is "add" and the location is "beginning", the function should add the
#  value (fourth parameter) to the beginning of the list and return the list
# If the command is "add" and the location is "end", the function should add the value
#  (fourth parameter) to the end of the list and return the list
# list_manipulation([1,2,3], "remove", "end") # 3
# list_manipulation([1,2,3], "remove", "beginning") # 1
# list_manipulation([1,2,3], "add", "beginning", 20) # [20,1,2,3]
# list_manipulation([1,2,3], "add", "end", 30) # [1,2,3,30]

def list_manipulation(lst, command, location, value=''):
    if command == "remove" and location == "end":
        return lst.pop()
    if command == "remove" and location == "beginning":
        return lst.pop(0)
    if command == "add" and location == "beginning":
        if value:
            lst.insert(1, value)
        return lst
    if command == "add" and location == "end":
        if value:
            lst.append(value)
        return lst


# is_palindrome
# A Palindrome is a word, phrase, number, or other sequence of characters
# which reads the same backward or forward. This function should take in
# one parameter and returns True or False depending on whether it is a
# palindrome. As a bonus, allow your function to ignore whitespace and
# capitalization so that is_palindrome('a man a plan a canal Panama')
# returns True.
# is_palindrome('testing') # False
# is_palindrome('tacocat') # True
# is_palindrome('hannah') # True
# is_palindrome('robert') # False

def is_palindrome(str):
    new_str = [i for i in str.lower() if not i.isspace()]
    return new_str == new_str[::-1]


# frequency
# This function accepts a list and a search_term (this will always be
# a primitive value) and returns the number of times the search_term
# appears in the list.
#
# frequency([1,2,3,4,4,4], 4) # 3
# frequency([True, False, True, True], False) # 1

def frequency(lst, target):
    return lst.count(target)

# flip_case
# This function accepts a string and a letter and reverses the case of
# all occurances of the letter in the string.
#
# flip_case("Hardy har har", "h") # "hardy Har Har"


def flip_case(str, letter):
    return ''.join(map(lambda i: i.swapcase() if i.lower() == letter.lower() else i, str))


# multiply_even_numbers
# This function accepts a list of numbers and returns the product of
# all even numbers in the list.
#
# multiply_even_numbers([2,3,4,5,6]) # 48

def multiply_even_numbers(lst):
    return reduce(multiply, filter(lambda i: i % 2 == 0, lst))

# mode
# This function accepts a list of numbers and returns the most frequent
# number in the list of numbers. You can assume that the mode will be unique.
#
# mode([2,4,1,2,3,3,4,4,5,4,4,6,4,6,7,4]) # 4


def mode(lst):
    return Counter(lst).most_common(1).pop()[0]


# capitalize
# This function accepts a string and returns the same string with the first
# letter capitalized.
#
# capitalize("tim") # "Tim"
# capitalize("matt") # "Matt"

def capitalize(string):
    return string.capitalize()

# compact
# This function accepts a list and returns a list of values that are truthy values.
#
# compact([0,1,2,"",[], False, {}, None, "All done"]) # [1,2, "All done"]


def compact(lst):
    return [item for item in lst if item]

# partition
# This function accepts a list and a callback function (which you can assume returns
#  True or False). The function should iterate over each element in the list and
# invoke the callback function at each iteration. If the result of the callback
# function is True, the element should go into one list if it's False, the element
# should go into another list. When it's finished, partition should return both
# lists inside of one larger list.
#
# def is_even(num):
#    return num % 2 == 0
#
# partition([1,2,3,4], is_even) # [[2,4],[1,3]]


def partition(lst, func):
    true_list, false_list = [], []
    for item in lst:
        if func(item):
            true_list.append(item)
        else:
            false_list.append(item)
    return [true_list, false_list]

# intersection
# This function should accept a two dimensional list and return a list with the
# values that are the same in each list.
#
# intersection([1,2,3], [2,3,4]) # [2,3]


def intersection(lst):
    first_set, second_set = map(set, lst)
    return list(first_set.intersection(second_set))

# once
# This function accepts a function and returns a new function that can only be
# invoked once. If the function is invoked more than once, it should return None.
# Hint you will need to define a new function inside of your once function and
# return that function. You can add properties to your inner function to see if
# it has run already.
#
# def add(a,b):
#    return a + b
#
#one_addition = once(add)
#
# one_addition(2,2) # 4
# one_addition(2,2) # undefined
# one_addition(12,200) # undefined


def once(func):

    def wrapped_func(*args):
        if wrapped_func.has_been_called:
            return
        wrapped_func.has_been_called = True
        return func(*args)

    wrapped_func.has_been_called = False
    return wrapped_func


# Super bonus
# Research what decorators are and refactor your once code to use a decorator so that you can run
#
# @run_once
# def add(a,b):
#    return a + b
#
# add(2,2) # 4
# add(2,20) # None
# add(12,20) # None

def run_once(func):

    def wrapped_func(*args):
        if wrapped_func.has_been_called:
            return
        wrapped_func.has_been_called = True
        return func(*args)

    wrapped_func.has_been_called = False
    return wrapped_func
