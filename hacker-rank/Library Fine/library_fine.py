#! /usr/bin/env python

from sys import exit

DEBUG = False

actual_day, actual_month, actual_year = raw_input().strip().split()
actual_day = int(actual_day)
actual_month = int(actual_month)
actual_year = int(actual_year)

expected_day, expected_month, expected_year = raw_input().strip().split()
expected_day = int(expected_day)
expected_month = int(expected_month)
expected_year = int(expected_year)

fine = 0

# Book is returned after expected year
if actual_year > expected_year:
    fine = 10000
    
    if DEBUG:
        print 'Book is returned after expected year: fine = {}'.format(fine)
        print '\n'
    
# Book is returned after expected month, but IN (NOT 'before or in') expected year (eg. if you return it 2 years ahead of time, but the month is after the expected month, obviously you should not be fined!)
elif (actual_month > expected_month) and (actual_year == expected_year):
    fine = 500 * (actual_month - expected_month)
    
    if DEBUG:
        print 'Book is returned after expected month (but in year), # of late months = {}, fine = {}'.format((actual_month - expected_month), fine)
        print '\n'
    
# Book is returned after expected day, but IN expected month and year (eg. if 1 month early or 2 years early or both -- day is irrelevant, should not be fined!)
elif (actual_day > expected_day) and (actual_month == expected_month) and (actual_year == expected_year):
    fine = 15 * (actual_day - expected_day)
    
    if DEBUG:
        print 'Book is returned after expected day (but in month and year), # of late days = {}, fine = {}'.format((actual_day - expected_day), fine)
        print '\n'
    
# Print fine
print fine

exit()
