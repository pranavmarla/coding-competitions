#! /usr/bin/env python

from sys import exit

DEBUG = False

num_testcases = int(raw_input().strip())

if DEBUG:
    print 'num_testcases: {}'.format(num_testcases)
    print '\n'

for n in range(num_testcases):
    
    if DEBUG:
        print 'Testcase #{}:'.format(n + 1)

    num = int(raw_input().strip())
    
    counter = 0
    
    # Cannot directly iterate over digits in integer, so convert it to a string and iterate over the corresponding characters.
    num_str = str(num)
    
    for digit_str in num_str:
        
        digit = int(digit_str)
        
        # NOTE: The digit might be 0 and dividing or 'modulo-ing' by 0 will cause an error.
        
        if (digit != 0) and ((num % digit) == 0):
            counter += 1
            
    print counter
    
exit()