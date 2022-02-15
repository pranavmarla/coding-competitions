from string import ascii_lowercase as letters
# ascii_lowercase, i.e. letters, is the following string: 'abcdefghijklmnopqrstuvwxyz'

DEBUG = False

def build_line(i, char_list, line_length):
    
    # Eg. If i = 2 and size = 5 ...
    
    if DEBUG:
        print 'i: {}'.format(i)
    
    # ... reduced_list = [e, d]
    reduced_list = char_list[ : i]
    
    if DEBUG:
        print 'reduced_list: {}'.format(reduced_list)
    
    # ... reversed_reduced_list = [d, e]
    reversed_reduced_list = reduced_list[: : -1]
    
    if DEBUG:
        print 'reversed_reduced_list: {}'.format(reversed_reduced_list)
    
    # ... reduced_list = [e, d, c]
    reduced_list.append(char_list[i])
    
    if DEBUG:
        print 'reduced_list: {}'.format(reduced_list)
    
    # ... reduced_list = [e, d, c, d, e]
    reduced_list.extend(reversed_reduced_list)
    
    if DEBUG:
        print 'reduced_list: {}'.format(reduced_list)
    
    # ... curr_baseline = 'e-d-c-d-e'
    curr_baseline = DASH.join(reduced_list)
    
    if DEBUG:
        print 'curr_baseline: {}'.format(curr_baseline)
    
    # Eg. If line_length = 17, then we are saying:   print '{:-^17}'.format(curr_baseline) 
    # which means that the resulting string has to be padded on the left and right with the character '-' such that the string curr_baseline is in the middle and the total length of the final string is 17.
    # This is the final string that is printed:   ----e-d-c-d-e----
    print '{:{}^{}}'.format(curr_baseline, DASH, line_length)
    
    if DEBUG:
        print '\n\n'.format(i)
    
DASH = '-'

size = int(raw_input())

# Formula for length of each line (including dashes) is: (2*x) - 1, where x = (2*(size-1)) + 1
x = (2 * (size - 1)) + 1
line_length = (2 * x) - 1

char_list = []

# Eg. If size = 5, values of letter_index are: 4, 3, 2, 1, 0
for letter_index in range(size - 1, -1, -1):    
        char_list.append(letters[letter_index])
        
# Eg. If size = 5, char_list is now [e, d, c, b, a]. Note that len(char_list) = size.

# Eg. If size = 5, values of i: 0, 1, 2, 3, 4
for i in range(size):
    build_line(i, char_list, line_length)
    
# Eg. If size = 5, values of i: 3, 2, 1, 0
for i in range(size - 2, -1, -1):
    build_line(i, char_list, line_length)