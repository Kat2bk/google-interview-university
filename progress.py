# 10/26/21
# exponents with products X 
# exponent properties with parentheses X
# exponent properties with quotients X (subtract) (numerator/donominator)
# reviewing

# 10/27/21
# exponent properties test
# x^n * n^m = x(n + m) = x^nm
# x^n / x^m = = x(n-m)
# (x^n)m = x(n * m)
# (x * y)n = x^n * y^n
# (x/y)n = x^n / x^y
# Product of powers
# negative exponents
# intro to logarithms
# ---- notes
# logarithms are another way of thinking about exponents
# suppose someone asked us "2 raised to which power equals 16?" The answer would be 4
# this is expressed by logarithmic equation log^2(16) = 4 (log base two of sixteen = 4)
# 2 is the base 4 is the exponent
# difference being that exponential form isolates the power, logarithmic isolates the exponent
# logarithmic = log2(8) = 3 ... exponential = 2^3 = 8
# log3(81) ... 3^4 = 81

# definition of a logarithm
# log b (a) = c
# let's evaluate log4(64)
# https://www.khanacademy.org/math/algebra2/x2ec2f6f830c9fb89:logs/x2ec2f6f830c9fb89:log-intro/a/intro-to-logarithms
# special logarithms
# bases can have many different values,there are two bases that are used more often
# common logarithm
# this base is 10 (base 10 logarithm)
# when writing these we omit the base, it is understood to be 10
# log10(x) = log(x)

# natural logarithm
# this base is the number e ("base-e logarithm")
# e is a mathematical constant, it is an irrational number that is approx equal to 2.718
# instead of writing base as e, we indicate with lm
# log e(x) = ln(x)
# evaluating logarithms

# grokking algorithms
# Big O notation log always means log2
# to check a list of 8 elements in binary search
# log 8 == 3
# for 1,024 elements, log == 10
# binary search only works when your list is in sorted order
# you need to keep track of what part of the array you have to search through
# low = 0
# high = len(list) - 1
# each time you check the middle element
# mid = (low + high) / 2
# guess = list[mid]
# if the guess is too low, you update low
# if guess < item:
#   low = mid + 1
# if guess is too high you update high
# while low <= high:
# if guess > item:
#   high = mid - 1
# else:
#  low = mid + 1
# return None

# suppose you have a sorted list of 128 names, what's the max num of steps?
# log2(128) == 2^128 = 2^7 so 7 names will be selected
# suppose you doubled the size of the list. What's the max num of steps now?
# log2(256) == 2(x) = 256? == 2^8 power = 256

# Running Time
# most efficient algorithm whether by time or space
# binary search runs in logarithmic time or log time

# 10/28/21
# codesignal problems

# 10/29/21
# Arrays and Strings Runtime

# 10/30/21
# Array Manipulation video
# everytime you slice O(k) is the size of the slice. it makes a new array.
# O(n) is the size of the list
# be clear what n refers to
# insert is bad (a linked list would get you better time performance for inserts)
# the bigger the index the more items need to move around
# big O is concerned with the worse case
# x in s lookups in sets are better, yet a set only allows you to store unique values
# hash tables are built out of linked lists/arrays
# lru cache are made of hash tables/double linked lists to create larger data structures
# n2 can consume space quickly
# in-place uses the passed-in list to do work
# out-of-place uses intermediate/other lists to do work, or makes a new one
# def triple_values_in_list(a): out of place
# a = [1, 2, 3]
# b = triple_values_in_list(a)
# does not mutate original list
# out-of-place uses more space
# if a has 10 elements, b has 10 elements -- O(n)
#  ...with space complexity do we consider the input space or just the space used
# execute the function
# space complexity -- this includes the size of the input
# auxillary space complexity -- only includes the additional space needed, not the

# 10/31/2021
# in-place example
# def triple_values_in_list(a):
# for i, e in enumerate(a):
#   a[i] = e * 3
#  return a
# there's no in-place algorithms for strings or tuples
# in-place manipulates the same array, so all references to it are changed in the
# memory
# multiple variables can point to the same object
# in-place O(1) aux memory complexity over len(a)
# because you didn't make a new list, and no matter what you pass in it doesn't scale
# up with input size
# amount of space doesn't change
# O(n) for the loop time complexity over len(a)
# what is preferred for out-of-space?
# in-place saved us a bunch of memory, we did lose the original value of the array
# do you still need the original value? question this
# you can make a copy of the change by setting the variable to a list:
# b = triple_values_in_list(list(a))
# this is O(n) space complexity
# sorted() does out of place, returning a new copy of list
# a.sort() does in-place
# 2 dementional array: O(n^2)
# quicksort:
# what is partitioning?
# partitioning goes through the rest of the list and finds out which numbers are greater
# or less than a target number and sorts them to a left or right side

# 11/01/2021
# def partition(a):
#   left = []
#   right = []
#   // get pivot
#   pivot = a[0]
#   for i in range(1, len(a)):
#       if a[i] < pivot:
#           left.append(a[i])
#       else:
#           right.append(a[i])
#   return left, pivot, right
# partitoning a list, sorts the pivot
# if you wanted to sort the other numbers, you can partition the left part
# l, p, r = partition(to_be_paritioned)
# in recursion we are looking for a problem that is made up of identical sub-problems
# def quicksort(a):
#  if len(a) <= 1:
#       return a
# // partition a into 1, p, r
#   left, pivot, right = parition(a)
# sorted_list = quicksort(1eft) + [pivot] + quicksort(right)
# return sorted_list
# O(log n) time - splitting list in half
# this is returning a new list
# it is out of place... + operators return a new list
# there is an in place quicksort, it is possible
# any sort that involves a comparison sort such as < > 
# best case time complexity is O(n log n)

# 11/02/21
# Looking over mutable/immutable objects/strings/tuples/lists

# 11/06/2021
# binary quiz

# 11/07/2021
# Overhead, binary to deciaml

#11/08/2021 
# for loop challenge
# spaces vs tabs
# for item in list:
# for number in range(a, b):
# while loop
# challenges with robot
# finishing last challenge
# needed to add a final function to check if obstacle was to the right

# 11/09/20211
# Finished maze for robot
# However, need to come back to debug! **
# trying to finish hangman challenge
# discovered issue with index, index of both lists needed to be assigned

# 11/10/2021
# finishing problem
# realized there's a "not in" 
# stuck on accessing another list, looking into issue

# 11/11/2021
# imported modules
# from replit import clear
# clear()
# functions with input
# cipher
# positional arguements, keyword arguements

# 11/12/2021
# prime number function
# starting cipher

# 11/13/2021
# finished encrypt
# finished decode
# need to figure out spaces
# figured out alphabet ord() chr()

# 11/15/2021
# simplified issue

# 11/17/2021
# fiished cipher

# 11/18/2021
# dictionaries/lists challenges

# 11/19/2021
# finished auction challenge
# finished leap year challenge
# starting calculator challenge
# learned about docstrings

# 11/24/2021
# learning recursion

        
