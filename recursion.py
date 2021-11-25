# it goes from bigger inputs to smaller 
# a base condition is needed to stop recursion

# Why recursion?
# helps break down big problems into smaller one
# depending on the situation, iteration can be faster
# you use recursion when you can divide the problem into similar problems
# how do we know if it is similar? ::

# design an algorithm to compute nth...
# write code to list the n
# implement a method to compute all
# recursion is used a lot in data structures like trees and graphs
# how recursion works:

# def recursionMethod(parameters):
    # if exit from condition satified:
    # return some value
    # else:
        # recursionMethod(modified parameters)

def recursiveMethod(n):
    if n < 1:
        print("n is less than 1")
    else:
        recursiveMethod(n-1)
        print(n)

print(recursiveMethod(5))