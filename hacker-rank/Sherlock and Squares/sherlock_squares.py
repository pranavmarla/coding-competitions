#! /usr/bin/env python

from math import ceil, floor, sqrt

DEBUG = False

num_testcases = int(raw_input().strip())

if DEBUG:
    print 'num_testcases: {}\n'.format(num_testcases)
    
for n in range(num_testcases):
    
    if DEBUG:
        print 'Testcase #{}:'.format(n + 1)
    
    num1, num2 = raw_input().split()
    num1 = int(num1)
    num2 = int(num2)
    
    # Counting no. of squares between num1 and num2 is same as counting no. of integers between ceil(sqrt(num1)) and floor(sqrt(num2)) [ceil and floor are chosen to keep the squares as integers within the range from num1 to num2]
    # All these math functions return floats -- for simplicity (to avoid any floating-point errors), convert them to integers.
    print int(floor(sqrt(num2))) - int(ceil(sqrt(num1))) + 1
    
exit()
