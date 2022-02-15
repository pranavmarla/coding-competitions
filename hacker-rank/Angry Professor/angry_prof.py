# Enter your code here. Read input from STDIN. Print output to STDOUT

failure_str = 'YES'
success_str = 'NO'

num_test_cases = int(raw_input())

for i in range(num_test_cases):
    
    #print '\n'
    
    # raw_input().split() returns a list of strings
    # Eg. ['4', '3'] --> 4 is total number of students, 3 is the minimum needed.
    min_students = int(raw_input().split()[-1])
    
    # List of strings
    arrival_times_str_list = raw_input().split()
    
    # Number of students who arrived at or before class started (arrival time <= 0)
    good_students = 0
    
    # Boolean keeping track of whether or not we fulfilled prof's condition
    professor_happy = False
    
    for arrival_time_str in arrival_times_str_list:
        
        arrival_time = int(arrival_time_str)
        
        #print 'arrival_str: {} arrival_num: {}'.format(arrival_time_str, arrival_time)
        
        if arrival_time <= 0:
            good_students += 1
            #print 'num_good: {:d}'.format(good_students)
            #print 'min_needed: {:d}'.format(min_students)
            
            # As soon as we hit the minimum number required, stop.
            if good_students == min_students:
                professor_happy = True
                #print 'SUCCESS!'
                print success_str
                
                # Can stop iterating through list of arrival times
                break
                
    # At this point, went through all students' arrival times.
    # If we have not reached the minimum, we failed.
    if not professor_happy:
        #print 'FAILURE'
        print failure_str