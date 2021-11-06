# Constants

CAT = 'C'
DOG = 'D'


# Functions

def process_test_case(test_case_num, num_dog_food, num_cat_food, num_cat_food_refills, animals_str, cat=CAT, dog=DOG):

    out_of_food = False

    # Edge cases
    if (num_cat_food == 0) or (num_dog_food == 0):
        out_of_food = True
    
    for animal in animals_str:
            
        if not out_of_food:
            if animal == cat:
                if num_cat_food > 0:
                    num_cat_food -= 1
                # Cat needs to be fed, but we're out of cat food: Not necessarily a fail
                else:
                    out_of_food = True
            # Animal is dog
            else:
                if num_dog_food > 0:
                    num_dog_food -= 1
                    num_cat_food += num_cat_food_refills
                # Dog needs to be fed, but we're out of dog food: Automatic fail
                else:
                    print(f'Case #{test_case_num}: NO')
                    return

        # Out of food: Automatic fail if there are any dogs remaining in line
        else:
            if animal == dog:
                print(f'Case #{test_case_num}: NO')
                return
        
    # Either we never ran out of food, or we ran out of cat food but there were no more dogs left in line (i.e. all dogs were still fed prior)
    print(f'Case #{test_case_num}: YES')


def main():

    num_test_cases = int(input())

    for test_case in range(1, num_test_cases+1):
        _, num_dog_food, num_cat_food, num_cat_food_refills = [int(int_str) for int_str in input().split()]
        animals_str = input()
        process_test_case(test_case, num_dog_food, num_cat_food, num_cat_food_refills, animals_str)


# Execution
main()