# Functions

def process_test_case(test_case_num, candy_bags, num_kids):

    total_num_candy = 0

    for num_candy_in_bag in candy_bags:
        total_num_candy += num_candy_in_bag

    # Divide total num candy by num kids: Quotient is the max that each kid gets, Remainder is what's left over
    leftover_candy = total_num_candy % num_kids
    print(f'Case #{test_case_num}: {leftover_candy}')


# Execution

num_test_cases = int(input())

for test_case_num in range(1, num_test_cases+1):
    _, num_kids = [int(int_str) for int_str in input().split()]
    candy_bags = [int(int_str) for int_str in input().split()]
    process_test_case(test_case_num, candy_bags, num_kids)