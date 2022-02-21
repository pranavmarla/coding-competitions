# Constants
VOWELS = ['a', 'e', 'i', 'o', 'u']

# Functions

def process_test_case(test_case_num, kingdom_name, vowels=VOWELS):

    last_letter = kingdom_name[-1]
    # To handle the case where, for example, the kingdom name consists of two words and the second word consists of just the starting capital letter -- i.e. the case where the last letter of the kingdom name is a capital letter!
    # Eg. New Y
    last_letter = last_letter.lower()

    if last_letter in vowels:
        ruler = 'Alice'
    elif last_letter == 'y':
        ruler = 'nobody'
    else:
        ruler = 'Bob'

    print(f'Case #{test_case_num}: {kingdom_name} is ruled by {ruler}.')


# Execution

num_test_cases = int(input())

for test_case_num in range(1, num_test_cases+1):
    kingdom_name = input()
    process_test_case(test_case_num, kingdom_name)