num_test_cases = int(input())

for i in range(1, num_test_cases+1):
    num_animals, num_dog_food, num_cat_food, num_cat_food_refills = [int(int_str) for int_str in input().split()]
    print(f'num_animals: {num_animals}')
    print(f'num_dog_food: {num_dog_food}')
    print(f'num_cat_food: {num_cat_food}')
    print(f'num_cat_food_refills: {num_cat_food_refills}')
    animals_str = input()
    print(f'animals_str: {animals_str}\n')