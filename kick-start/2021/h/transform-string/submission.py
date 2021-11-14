# Constants

LETTERS_TO_POSITION_DICT = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10, 'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 'p':16, 'q':17, 'r':18, 's':19, 't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26}
TOTAL_NUM_LETTERS = 26

# Functions

def find_shortest_distance_between_letters(letter1, letter2, letters_to_position_dict=LETTERS_TO_POSITION_DICT, max_distance=TOTAL_NUM_LETTERS):
    letter1_position = letters_to_position_dict[letter1]
    letter2_position = letters_to_position_dict[letter2]
    distance1 = abs(letter2_position - letter1_position)
    distance2 = max_distance - distance1
    return min(distance1, distance2)


def process_test_case(test_case_num, padlock_str, fav_str):

    total_operations = 0

    for letter1 in padlock_str:
        
        min_operations = None

        for letter2 in fav_str:
            num_operations = find_shortest_distance_between_letters(letter1, letter2)
            if (min_operations is None) or (num_operations < min_operations):
                min_operations = num_operations
        
        total_operations += min_operations

    print(f'Case #{test_case_num}: {total_operations}')


# Execution

num_test_cases = int(input())

for test_case in range(1, num_test_cases+1):
    padlock_str = input()
    fav_str = input()
    process_test_case(test_case, padlock_str, fav_str)