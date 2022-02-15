#! /usr/bin/env python

from sys import exit

DEBUG = False

# Maximise the value of the palindrome (final_str_list)
def maximise_palindrome(final_str_list, indices_changed, change_left, num_digits_even, made_changes = True):
    
    if DEBUG:
        print 'final_str_list: {}, indices_changed = {}, change_left = {}'.format(final_str_list, indices_changed, change_left)
        print '\n\n'
    
    for i, c in enumerate(final_str_list):
    
        undid_change = False
    
        if DEBUG:
            print 'index: {}, digit: {}, change_left: {}'.format(i, c, change_left)
    
        # If we made a change here, undo/recover it
        if made_changes and (i in indices_changed):
                
            change_left += 1
            undid_change = True
            
            if DEBUG:
                print 'Recovered a change -- change_left: {}'.format(change_left)

        # If num_digits is even, every digit in the first half of final_str_list has a corresponding digit in the 2nd half and we will always be changing 2 digits (1 in first half and corresponding digit in 2nd half). Thus, change_left has to be at least 2.
        # If num_digits is odd, then the last digit in first half (i.e. the middle digit) of final_str_list does NOT have a corresponding digit in the 2nd half and, in this one case, we will only be changing 1 digit (the middle digit). Thus, change_left can be only 1 in this one case.
        
        # Either num_digits is even, or it is odd but we are not at middle digit -- since every digit in the first half of final_str_list has a corresponding digit in the 2nd half, need change_left to be at least 2.
        if (change_left >= 2) and not ((not num_digits_even) and (i == middle_index)):

            if DEBUG:
                print 'We have sufficient change -- change_left: {}'.format(change_left)
                
            # Assuming the digit wasn't already 9, change it to 9
            if c != '9':
                
                final_str_list[i] = '9'
                
                # Essentially changing 2 digits (1 in first half and corresponding digit in 2nd half)
                change_left -= 2
                
                if DEBUG:
                    print 'Changed 2 digits to 9, change_left is now: {}'.format(change_left)
            
            # This digit is 9 (implying other, corresponding digit is 9 as well since it can't be larger than this) -- cannot further maximise this pair of digits.
            else:
            
                # If we undid this change, redo it.
                if undid_change:
                    change_left -= 1
                    undid_change = False
                    
                    if DEBUG:
                        print 'Since this pair of digits is already 9 and canot be maximised further, undoing this change doesn\'t help -- redo that change.\nchange_left is now: {}'.format(change_left)

        # num_digits is odd and we are at the middle digit -- change_left can be 1.
        elif ((not num_digits_even) and (i == middle_index) and (change_left >= 1)):
            
            if DEBUG:
                print 'We have sufficient change -- change_left: {}'.format(change_left)
            
            # Assuming the digit wasn't already 9, change it to 9
            if c != '9':
                
                final_str_list[i] = '9'
            
                # Changing only this 1 digit (the middle digit)
                if i == middle_index:
                    change_left -= 1
                    
                if DEBUG:
                    print 'Changed the 1 middle digit to 9, change_left is now: {}'.format(change_left)
                    
        else:
        
            if DEBUG:
                print 'Insufficient change'
        
            # If it was possible to undo/recover a change, we have already done so. Since, even after recovering a change, it is not sufficient, we need to revert/return/redo the change.
            if undid_change:
            
                change_left -= 1
                undid_change = False
                
                if DEBUG:
                    print 'Since undoing a change wasn\'t enough to help, we re-did that change -- change_left is now: {}'.format(change_left)
        
            # NOTE: Do NOT always immediately leave when the change is insufficient (< 2)! Keep iterating if num_digits is odd since we will eventually get to the middle digit which only requires 1 change.
            if num_digits_even:
                break
        
        if DEBUG:
            print '\n\n'
            
    if DEBUG:
        print '\n\n'

num_digits, change_left = raw_input().strip().split()
num_digits, change_left = [int(num_digits),int(change_left)]
num_str = raw_input().strip()
rev_num_str = num_str[::-1]
final_str_list = []

# Base Case: When num_str is just one digit (eg. 5) -- if change_left is at least 1, simply replace the digit with 9 to produce the maximum possible 1-digit palindrome.
if (num_digits == 1) and (change_left >= 1):
    print '9'
    exit()

# Stores the indices of digits in num_str -- this means that we have changed either the digit at this index (in first half of num_str), or the corresponding digit in the second half of num_str.
indices_changed = []

# Stores whether the number of digits in num_str is even or odd (if num_digits is even, num_digits_even is True)
num_digits_even = False

# NOTE: If num_str is already a palindrome, does NOT mean that we can immediately leave, since we might still be able to make it a LARGER palindrome (by making <= change_left changes).

# Middle index of num_str
middle_index = num_digits / 2

if (num_digits % 2) == 0:
    num_digits_even = True
    middle_index -= 1
    
if DEBUG:
    print 'number: {}'.format(num_str)
    print 'reverse: {}'.format(rev_num_str)
    print 'Does number have an even no. of digits? --> {}'.format(num_digits_even)
    print 'middle_index: {}'.format(middle_index)
    print 'final_str_list: {}'.format(final_str_list)
    print 'change_left: {}'.format(change_left)
    print '\n\n'
    
# Format: (index, ('first digit', 'last digit'))
for (i, (c1,c2)) in enumerate(zip(num_str, rev_num_str)):

    if DEBUG:
        print 'index: {}'.format(i)
        print 'first half digit: {}'.format(c1)
        print 'last half digit: {}'.format(c2)
    
    # Stop after reading 1st half of original string and 2nd half of reversed string
    if i > middle_index:
    
        if DEBUG:
            print 'Finished processing first half of num_str -- stop iterating'
            print '\n\n'
        
        break
        
    # Compare corresponding digits from num_str and rev_num_str
    
    # If digits are equal, append the digit from num_str to final_str_list -- no changes made
    if c1 == c2:
        final_str_list.append(c1)
        
        if DEBUG:
            print 'Digits equal, append the digit from num_str to final_str_list'
            print 'final_str_list: {}'.format(final_str_list)
            print 'change_left: {}'.format(change_left)
            print '\n\n'
    
    # If digits are not equal, and if we can still afford to make a change, append the larger of c1 and c2 to final_str_list -- essentially, we changed / will change (when the 2nd half of final_str_list is built up) the smaller digit (c2 or c1)
    else:
    
        if DEBUG:
            print 'Digits NOT equal'
            print 'Initially, change_left: {}'.format(change_left)
    
        # Check if we can afford to make a change
        if change_left > 0:
            change_left -= 1
        
            # Keep track of the first_half index involved in this change
            indices_changed.append(i)
        
            if DEBUG:
                print 'Now, change_left: {}'.format(change_left)
            
            if c1 > c2:
                larger = c1
                
            else:
                larger = c2
            
            final_str_list.append(larger)
            
            if DEBUG:
                print 'Append the larger digit to final_str_list'
                print 'final_str_list: {}'.format(final_str_list)
                print '\n\n'
            
        # Can no longer afford to make changes -- no point iterating through num_str any more
        else:
        
            if DEBUG:
                print 'Run out of change_left -- stop iterating through num_str'
                print '\n\n'
        
            break
            
# Successfully converted num_str to a palindrome or could not afford to make any more changes

# Successfully converted num_str to a palindrome (final_str_list)
if i > middle_index:

    if DEBUG:
        print 'Successfully converted num_str to a palindrome (final_str_list)'
        print '\n\n'

    # If we can afford to make more changes, try to maximise the value of this palindrome.
    if change_left > 0:
    
        if DEBUG:
            print 'Since we can afford more changes, maximise the palindrome'
        
        # To maximise the palindrome, we will need to change 2 digits (a digit in the first half of final_str_list and its corresponding digit in the second half) at a time to 9. The only exception is if num_str has an odd number of digits and we are changing the middle digit (i.e. the digit which does not have a corresponding digit).
        # Note that we can gain an extra change by essentially undoing one of the previous changes we made.
        
        # We made no changes whatsoever (num_str was already a palindrome)
        if not indices_changed:
                    
            if DEBUG:
                print 'We\'ve made no changes so far'
                print '\n\n'
                    
            # Maximise the value of the palindrome (final_str_list)
            maximise_palindrome(final_str_list, indices_changed, change_left, num_digits_even, False)
            
             
        # We've made at least 1 change to num_str
        else:

            if DEBUG:
                print 'We\'ve already made at least 1 change so far'
                print '\n\n'        
            
            # Maximise the value of the palindrome (final_str_list)
            maximise_palindrome(final_str_list, indices_changed, change_left, num_digits_even)
            
    # Only the first half of the palindrome (that we want to build up) has been built (and saved as final_str_list) -- finish building the palindrome by appending the reverse of the first half to final_str_list.

    # If num_str has an even number of digits, the first half of the palindrome is just the entire final_str_list built up so far.
    if num_digits_even:
        first_half = final_str_list

    # If num_str has an odd number of digits, the first half of the palindrome is everything in final_str_list except for the last digit.
    else:
        first_half = final_str_list[:-1]
    
    # Create the second half by reversing the first half
    second_half = first_half[::-1]

    if DEBUG:
        print 'Initially, final_str_list: {}'.format(final_str_list)
        print 'first_half of final_str_list: {}'.format(first_half)
        print 'second_half of final_str_list: {}'.format(second_half)
    
    # Finish building final_str_list by appending second_half to final_str_list (NOT to first_half, since that might exclude the middle digit!)
    final_str_list.extend(second_half)
    
    if DEBUG:
        print 'Finally, final_str_list: {}'.format(final_str_list)
        print '\n\n'
    
# Could not afford to make any more changes -- might not have been able to successfully convert num_str to a palindrome
else:
    
    if DEBUG:
        print 'Could not afford to make any more changes'
        print '\n\n'
    
    # final_str_list only consists of part of num_str (always starting from the beginning of num_str -- i.e. always has first few digits of num_str, where 'few' varies based on how many digits of num_str we processed before change_left became 0)
    
    if DEBUG:
        print 'Initially, final_str_list: {}'.format(final_str_list)
        print 'Remainder of num_str that we\'re going to add to final_str_list: {}'.format(num_str[len(final_str_list) : ])
    
    # Complete final_str_list by appending the remainder of num_str
    final_str_list.extend(list(num_str[len(final_str_list) : ]))
    
    if DEBUG:
        print 'Finally, final_str_list: {}'.format(final_str_list)
    
    # Check if we managed to convert enough of num_str before running out of change_left -- i.e. check if final_str_list is now a palindrome.
    # If final_str_list is not a palindrome, not possible to convert num_str to a palindrome given the input value of change_left -- print -1 and exit.
    if final_str_list != final_str_list[::-1]:
    
        if DEBUG:
            print 'final_str_list is NOT a palindrome -- print -1 and leave!'
            print '\n\n'
        
        print '-1'
        
        # NOTE: exit(1) makes HackerRank think the testcase has failed somehow!
        exit()

# Successfully converted num_str to a palindrome (final_str_list) -- convert it to a string and print it.
print ''.join(final_str_list)
exit()