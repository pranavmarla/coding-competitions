# Note: This naive algorithm only passes test set 1

# Constants
STR_TRANSFORM_DICT = {'01': '2', '12': '3', '23': '4', '34': '5',  '45': '6', '56': '7', '67': '8', '78': '9', '89': '0', '90': '1'}


# Functions

def process_test_case(test_case_num, old_str, str_transform_dict=STR_TRANSFORM_DICT):

    while True:
        current_str = old_str

        # NOTE: As of Python 3.7, dicts preserve insertion order!
        for original_substr, new_substr in str_transform_dict.items():
            if original_substr in current_str:
                current_str = current_str.replace(original_substr, new_substr)

        # All transformations had no effect
        if current_str == old_str:
            break
        else:
            old_str = current_str

    print(f'Case #{test_case_num}: {current_str}')


# Execution

num_test_cases = int(input())

for test_case in range(1, num_test_cases+1):
    _ = input()
    input_str = input()
    process_test_case(test_case, input_str)