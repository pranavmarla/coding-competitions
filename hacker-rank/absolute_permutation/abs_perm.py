#! /usr/bin/env python

from sys import exit

DEBUG = False
INFINITY = float('inf')

# Constraints:
# 1 <= num_testcases <= 10
# 1 <= num_limit <= 10^5
# 0 <= desired_abs_diff <= num_limit

num_testcases = int(raw_input().strip())

if DEBUG:
    print 'num_testcases: {}\n'.format(num_testcases)

for n in range(num_testcases):
    
    absolute_permutation_exists = True
    
    if DEBUG:
        print 'Testcase #{}:'.format(n + 1)
    
    num_limit, desired_abs_diff = raw_input().strip().split()
    num_limit = int(num_limit)
    desired_abs_diff = int(desired_abs_diff)
    
    if DEBUG:
        print 'num_limit: {}'.format(num_limit)
        print 'desired_abs_diff: {}'.format(desired_abs_diff)
        print '\n\n'
    
    # This list of numbers will store the correct absolute permutation
    correct_perm = num_limit * [None]
    
    # Base case: If desired_abs_diff = 0, the smallest absolute permutation is just the numbers 1 to num_limit.
    if desired_abs_diff == 0:
        
        for i in range(1, num_limit + 1):
            print i,
        
        print
        
        if DEBUG:
            print '\n'
        
        # Skip everything below and proceed to next testcase
        continue
        
    # For each digit from 1 to num_limit, solve the equation "abs(digit_position - digit) = desired_abs_diff" to get 2 values of digit_position. Since we want the smallest correct permutation, need to ensure that smaller digits are put in the smaller (leftmost) position.
    # Note that the position is 1-based.
    # Note that if position < 1 or position >num_limit, then it is invalid.
    for digit in range(1, num_limit + 1):
        
        # digit_position - digit = desired_abs_diff --> digit_position = digit + desired_abs_diff
        digit_position_1 = digit + desired_abs_diff
        
        if (digit_position_1 < 1) or (digit_position_1 > num_limit):
            digit_position_1 = INFINITY
        
        # digit - digit_position = desired_abs_diff --> digit_position = digit - desired_abs_diff
        digit_position_2 = digit - desired_abs_diff
        
        if (digit_position_2 < 1) or (digit_position_2 > num_limit):
            digit_position_2 = INFINITY
        
        if DEBUG:
            print 'digit: {}'.format(digit)
            print 'digit_position_1: {}'.format(digit_position_1)
            print 'digit_position_2: {}'.format(digit_position_2)
            print '\n'
        
        # If both positions are invalid, then no absolute permutation exists!
        if (digit_position_1 == INFINITY) and (digit_position_2 == INFINITY):
            
            absolute_permutation_exists = False
                
            if DEBUG:
                print 'No absolute permutation exists!!'
        
            print '-1'
        
            if DEBUG:
                print '\n\n'
            
            break
        
        # Note that this is a 1-based position!
        final_digit_position = min(digit_position_1, digit_position_2)
        
        if DEBUG:
            print 'final_digit_position: {}'.format(final_digit_position)
            print 'Initially, correct_perm[final_digit_position - 1]: {}'.format(correct_perm[final_digit_position - 1])
        
        # If the element at this position in correct_perm has not already been overwritten, overwrite it.
        if correct_perm[final_digit_position - 1] is None:
            correct_perm[final_digit_position - 1] = digit
            
            if DEBUG:
                print 'Now, correct_perm[final_digit_position - 1]: {}'.format(correct_perm[final_digit_position - 1])
                print '\n\n'
            
        # If we have already occupied this position in correct_perm, then use the other position (assuming it is valid and has not already been overwritten).
        else:
            final_digit_position = max(digit_position_1, digit_position_2)
            
            if DEBUG:
                print 'Already occupied!'
                print 'final_digit_position is now: {}'.format(final_digit_position)
            
            if (final_digit_position != INFINITY) and (correct_perm[final_digit_position - 1] is None):
                
                if DEBUG:
                    print 'Initially, correct_perm[final_digit_position - 1]: {}'.format(correct_perm[final_digit_position - 1])
                
                correct_perm[final_digit_position - 1] = digit
                
                if DEBUG:
                    print 'Now, correct_perm[final_digit_position - 1]: {}'.format(correct_perm[final_digit_position - 1])
                    print '\n\n'
                
                
            # This digit cannot be placed in either of the 2 positions -- thus, no absolute permutation exists -- print -1.
            else:
                
                absolute_permutation_exists = False
                
                if DEBUG:
                    print 'No absolute permutation exists!!'
            
                print '-1'
            
                if DEBUG:
                    print '\n\n'
                
                break
            
    # Have finished building the correct permutation
    if absolute_permutation_exists:

        for digit in correct_perm:
            print digit,
        
        print
        
        if DEBUG:
            print '\n\n'
            
exit()
