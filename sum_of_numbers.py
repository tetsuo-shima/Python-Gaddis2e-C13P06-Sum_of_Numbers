__author__ = 'dwight'

# Design a function that accepts an integer argument and returns the sum of all the integers from 1 up to the number
# passed as an argument. For example, if 50 is passed as an argument, the function will return the sum of
# 1, 2, 3, 4, . . . 50. Use recursion to calculate the sum.

import random


def main():
    value = random.randint(1, 10)
    print('Random value:', value)
    print('Sum of Integers from 1 to ' + str(value) + ':', sum_of_positive_integers(value))


def sum_of_positive_integers(num_value):
    if num_value == 1:
        return 1
    else:
        return num_value + sum_of_positive_integers(num_value - 1)


main()