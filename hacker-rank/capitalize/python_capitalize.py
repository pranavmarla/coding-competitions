# NOTE: The simplest option of just printing raw_input().title() does not work in cases when the word starts with a number -- eg. '3g' should remain '3g', but title() will change it to '3G'.

DEBUG = False
SINGLE_SPACE = ' '

lower_str = raw_input().strip()

# NOTE: Need to preserve the original spaces between words (eg. 'Hello   wor ld') -- thus, use split(' ') instead of just split()
# Eg. 3 spaces in between words 'Hello' and 'wor', 1 space between 'wor' and 'ld' -- after using split(' '), this is the resulting list: ['Hello', '', '', 'wor', 'ld']
lower_str_list = lower_str.split(SINGLE_SPACE)

#final_sentence = None

if DEBUG:
    print 'list of words in str: {}'.format(lower_str_list)
    print '\n'
    
for i, word in enumerate(lower_str_list):

    if DEBUG:
        print 'Initially, word: |{}|'.format(word)
    
    # For simplicity, do NOT try and print out the words here directly -- will be easier to deal with multiple spaces between words afterwards, when printing the whole sentence together in one operation.
    
    lower_str_list[i] = word.capitalize()
    
    # Alternative method:
    
    # Ensure word is not an empty string before attempting to access its characters
    #if word:
        # Capitalize first char of each word -- if it is already capitalized or is a number, this will not affect it. 
        #lower_str_list[i] = ''.join([word[0].upper(), word[1:]])
        
        # Note that this below code does not seem to be necessary:
        # Also ensure that the other characters are lowercase, even if they were initially capitalized!
        # lower_str_list[i] = ''.join([word[0].upper(), word[1:].lower()])
        
        
    if DEBUG:
        print 'Now, word: |{}|'.format(lower_str_list[i])
        print '\n'
    
if DEBUG:
    print 'Final list of words: {}\n\n'.format(lower_str_list)
    #print 'Initially, final_sentence: |{}|'.format(final_sentence)
    print '\n'
    
print SINGLE_SPACE.join(lower_str_list)
    
# Alternative method:
    
# Built up the sentence, preserving any multiple spaces between the original words
#for word in lower_str_list:
    
    # In beginning, set final_sentence equal to the first word (guaranteed to be a valid word since, if there was any preceding spaces in the original sentence, we would have removed it using strip())
    #if final_sentence is None:
        # final_sentence = word
        
        # if DEBUG:
            # print 'final_sentence: |{}|\n'.format(final_sentence)
        
        # continue
    
    # Even if word is an empty string, treat it as a valid word and delimit it with a space -- note that this only works if we keep the word as an empty string, rather than replacing it with a space.
    # final_sentence = SINGLE_SPACE.join([final_sentence, word])
 
    # Alternative method:
    
    # Word is an empty string, implying that there is an additional space here -- do NOT treat this additional space as a valid word and try to delimit it with another space, since that will introduce too many spaces.
    #if not word:
    #    final_sentence = ''.join([final_sentence, SINGLE_SPACE])
        
    # Word is a valid word -- delimit it with a space
    #else:
    #    final_sentence = SINGLE_SPACE.join([final_sentence, word])
        
    # if DEBUG:
        # print 'final_sentence: |{}|\n'.format(final_sentence)
    
# if DEBUG:
    # print 'FINALLY:\n\n'
    
# Built up capitalized sentence, while preserving any multiple spaces present in original sentence -- print it.
# print final_sentence