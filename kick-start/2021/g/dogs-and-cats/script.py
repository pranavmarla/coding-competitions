import sys

CAT = 'C'
DOG = 'D'
OUT_OF_CAT_FOOD = False

num_test_cases = int(input())

for i in range(1, num_test_cases+1):
    
    num_animals, num_dog_food, num_cat_food, num_cat_food_refills = [int(int_str) for int_str in input().split()]
    animals_str = input()
    
    #! TODO: Edge cases when inputs are 0

    for animal in animals_str:
        
        if not OUT_OF_CAT_FOOD:
            if animal == CAT:
                if num_cat_food > 0:
                    num_cat_food -= 1
                # Out of cat food -- cat cannot eat
                else:
                    OUT_OF_CAT_FOOD = True
            # Animal is dog
            else:
                if num_dog_food > 0:
                    num_dog_food -= 1
                    num_cat_food += num_cat_food_refills
                # Out of dog food -- dog cannot eat
                else:
                    print(f'Case #{i}: NO')
                    sys.exit()

        # Out of cat food -- need to see if there are any dogs remaining in line
        else:
            if animal == DOG:
                print(f'Case #{i}: NO')
                sys.exit()
        
    # Either we never ran out of food, or we ran out of cat food but there were no more dogs left in line (i.e. all dogs were still fed prior)
    print(f'Case #{i}: YES')