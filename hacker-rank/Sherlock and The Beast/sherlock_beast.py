#! /usr/bin/env python

from sys import exit

DEBUG = True

num_testcases = int(raw_input().strip())

if DEBUG:
    print 'num_testcases: {}\n'.format(num_testcases)

str_5 = '555'
len_5 = 3

str_3 = '33333'
len_3 = 5
    
for n in range(num_testcases):

    num_digits = int(raw_input().strip())
    
    if DEBUG:
        print 'Testcase #{}:'.format(n + 1)
        print 'num_digits: {}'.format(num_digits)
    
    final_num_str = ''
    
    # Create the number by packing as many str_5s as possible in the left, remainder with str_3s
    
    # Max number of str_5s we can pack into this number,starting from the left
    max_num_str_5s = num_digits / len_5
    
    # Final number of str_5s that we will pack into this number -- initialise to max possible
    num_str_5s = max_num_str_5s
    
    if DEBUG:
        print 'num_str_5s = max_num_str_5s = {}'.format(max_num_str_5s)
        print '\n'
    
    # Need to squeeze str_3s into this remainder
    remainder = num_digits % len_5
    
    if DEBUG:
        print 'Remainder, for str_3s: {}'.format(remainder)
        print '\n'
    
    # If cannot squeeze str_3s into this remainder, need to remove 1 str_5 at a time and use its space to squeeze in a str_3
    while ((remainder % len_3) != 0) and (num_str_5s > 0):
        
        if DEBUG:
            print 'Not enough space for str_3s'
            
        num_str_5s -= 1
        remainder += len_5
        
        if DEBUG:
            print 'Now, num_str_5s: {}'.format(num_str_5s)
            print 'Now, remainder: {}'.format(remainder)
            print '\n'
        
    # If desired number does not exist, print -1 and exit.
    if not (((num_str_5s > 0) and ((remainder % len_3) == 0)) or ((num_digits % len_3) == 0)):
        
        if DEBUG:
            print 'Desired no. does not exist!'
        
        print '-1'
        
        if DEBUG:
            print '\n#############\n\n'
        
    else:
    
        if DEBUG:
            print 'Building up desired no. with str_5s and str_3s'
            print 'num_str_5s: {}, num_str_3s: {}'.format(num_str_5s, remainder/len_3)
            print '\n'
    
        for _ in range(num_str_5s):
            final_num_str = ''.join([final_num_str, str_5])
            
        for _ in range(remainder / len_3):
            final_num_str = ''.join([final_num_str, str_3])
            
        print final_num_str
        
        if DEBUG:
            print '\n#############\n\n'
exit()
