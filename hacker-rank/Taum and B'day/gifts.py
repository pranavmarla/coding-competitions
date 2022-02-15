#! /usr/bin/env python

from sys import exit

# Constraints:
# 1 <= num_testcases <= 10
# 0 <= cost_black, cost_white, cost_convert, num_black, num_white <= 10^9

# NOTE:
#   Up to sys.maxint (9223372036854775807 = 2^63 - 1 --> 64-bit signed integer), the type of the value remains 'int' -- if we increase past that, there is still no integer overflow issue, but the type is silently promoted to 'long'. Thus, the only real hard limit is the size of the machine's RAM.
#   In Python 3, 'int' is essentially the same as Python 2's 'long' (i.e. 'long' was essentially renamed to 'int'), so sys.maxint was removed in Python 3.

DEBUG = False

num_testcases = int(raw_input().strip())

if DEBUG:
    print 'num_testcases: {}'.format(num_testcases)
    print '\n'

for n in range(num_testcases):
    
    if DEBUG:
        print 'Testcase #{}:'.format(n + 1)

    num_black, num_white = raw_input().strip().split()
    num_black = int(num_black)
    num_white = int(num_white)

    cost_black, cost_white, cost_convert = raw_input().strip().split()
    cost_black = int(cost_black)
    cost_white = int(cost_white)
    cost_convert = int(cost_convert)

    # Ignoring conversion, cost is calculated as: 
    #   (num_black * cost_black) + (num_white * cost_white)
    
    # If, instead, we are buying all black gifts and converting num_white of them to white gifts, then cost is:
    #   (num_black * cost_black) + (num_white * (cost_black + cost_convert))
    
    # If, instead, we are buying all white gifts and converting num_black of them to black gifts, then cost is:
    #   (num_black * (cost_white + cost_convert)) + (num_white * cost_white)
    
    
    # Cheaper to buy all black and convert num_white of them to white -- note that the below equation means that it will never be cheaper to convert some from black to white and also directly buy some white.
    if (cost_black + cost_convert) < cost_white:
        print (num_black * cost_black) + (num_white * (cost_black + cost_convert))
    
    # Cheaper to buy all white and convert num_black of them to black -- note that the below equation means that it will never be cheaper to convert some from white to black and also directly buy some black.
    elif (cost_white + cost_convert) < cost_black:
        print (num_black * (cost_white + cost_convert)) + (num_white * cost_white)
    
    # Cheaper to ignore conversion
    else:
        print (num_black * cost_black) + (num_white * cost_white)
    
exit()
