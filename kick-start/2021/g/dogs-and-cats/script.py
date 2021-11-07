# Constants

CAT = 'C'
DOG = 'D'


# Functions

def process_test_case(test_case_num, num_dog_food, num_cat_food, num_cat_food_refills, animals_str, cat=CAT, dog=DOG):

    out_of_dog_food_at_beginning = False
    out_of_cat_food_and_need_to_feed_cat = False

    if num_dog_food == 0:
        out_of_dog_food_at_beginning = True

    for animal in animals_str:
        
        # Feeding has stopped: Fail if there are any dogs remaining in line
        if out_of_dog_food_at_beginning or out_of_cat_food_and_need_to_feed_cat:
            if animal == dog:
                print(f'Case #{test_case_num}: NO')
                return

        else:
            if animal == cat:
                if num_cat_food > 0:
                    num_cat_food -= 1
                # Cat needs to be fed, but we're out of cat food: Don't know if it's a fail at this point
                else:
                    out_of_cat_food_and_need_to_feed_cat = True
            # Animal is dog
            else:
                if num_dog_food > 0:
                    num_dog_food -= 1
                    num_cat_food += num_cat_food_refills
                # Dog needs to be fed, but we're out of dog food: Fail
                else:
                    print(f'Case #{test_case_num}: NO')
                    return
    
    # Either we never ran out of food, or we ran out of cat food but there were no more dogs left in line (i.e. all dogs had been fed prior)
    print(f'Case #{test_case_num}: YES')


# Execution

num_test_cases = int(input())

for test_case in range(1, num_test_cases+1):
    _, num_dog_food, num_cat_food, num_cat_food_refills = [int(int_str) for int_str in input().split()]
    animals_str = input()
    process_test_case(test_case, num_dog_food, num_cat_food, num_cat_food_refills, animals_str)