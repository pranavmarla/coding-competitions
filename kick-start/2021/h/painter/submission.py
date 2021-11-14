# Constants

COLOUR_COMPOSITION_DICT = {'U': set(), 'R': {'R'}, 'Y': {'Y'}, 'B': {'B'}, 'O': {'R', 'Y'}, 'P': {'R', 'B'}, 'G': {'Y', 'B'}, 'A': {'R', 'Y', 'B'}}


# Functions

def process_test_case(test_case_num, painting_length, desired_painting_str, colour_composition_dict=COLOUR_COMPOSITION_DICT):

    painting = []
    for colour in desired_painting_str:
        painting.append(colour_composition_dict[colour])

    # Eg.
    # painting_length = 5
    # desired_painting_str = 'ROAOR'
    # painting = [{'R'}, {'R', 'Y'}, {'R', 'Y', 'B'}, {'R', 'Y'}, {'R'}]

    num_strokes = 0
    for current_square_index, square_composition in enumerate(painting):
        for primary_colour in square_composition:
            # print(f'Colour: {primary_colour}')
            primary_colour_set = set(primary_colour)
            # Remove primary_colour from every square's set, starting from current square, until it hits one that it's not already present in
            for square_index in range(current_square_index, painting_length):
                if primary_colour in painting[square_index]:
                    # print(f'Removing {primary_colour_set} from {painting[square_index]}')
                    painting[square_index] = painting[square_index] - primary_colour_set
                else:
                    break
            num_strokes += 1

    print(f'Case #{test_case_num}: {num_strokes}')


# Execution

num_test_cases = int(input())

for test_case in range(1, num_test_cases+1):
    painting_length = int(input())
    desired_painting_str = input()
    process_test_case(test_case, painting_length, desired_painting_str)