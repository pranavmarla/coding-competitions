# Constants



# Functions

def process_test_case(test_case_num, num_papers, num_citations_per_paper):

    print(f'Case #{test_case_num}:', end='')

    max_possible_h_index = num_papers
    # For simplicity, initialize entire list so that we can assume all the values already exist
    # Technically don't need elements 0 and 1, since min possible h-index is 1, but keeping them there to avoid complexity when indexing into the list
    # Note: Need an element in the list for max_possible_h_index itself, so adjust range endpoint accordingly
    possible_h_indexes = [0 for i in range(max_possible_h_index + 1)]
    # Technically, we are already told that every paper is cited at least once, but it makes our code simpler to start from 0
    current_h_index = 0
    next_possible_h_index = current_h_index + 1

    # For each paper's number of citations, store its contributions towards each of the remaining possible h-indexes -- i.e. all the possible h-indexes (starting from next_possible_h_index) that that paper's number of citations could potentially help us get to
    for num_citations in num_citations_per_paper:

        for i in range(next_possible_h_index, min(num_citations, max_possible_h_index) + 1):
            possible_h_indexes[i] += 1

        if possible_h_indexes[next_possible_h_index] == next_possible_h_index:
            current_h_index = next_possible_h_index
            next_possible_h_index += 1
        
        print(f' {current_h_index}', end='')

    # Add newline at the end of the test case
    print()

# Execution

num_test_cases = int(input())

for test_case_num in range(1, num_test_cases+1):
    num_papers = int(input())
    num_citations_per_paper = [int(int_str) for int_str in input().split()]
    process_test_case(test_case_num, num_papers, num_citations_per_paper)