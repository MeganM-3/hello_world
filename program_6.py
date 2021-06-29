print('Requirement 1:')
# Program Header
print('\tThis is Program 6 - Megan Weir')

print('\n\nRequirement 2:')
# Program purpose
print('\tThis program practices working with lists, '
      'strings, tuples, and dictionaries.')

print('\n\nRequirement 3:')
# Create two tuples
weeks = 'Week One', 'Week Two'
days = 'Thursday', 'Friday', 'Saturday'
print('\t--weeks and days tuples created--')

print('\n\nRequirement 4:')
# Create dictionary
Reps_dealers = {}

# Collect sales reps' names and dealership with while loop
sales_reps = input('\n\tEnter first and last name of '
                   'sales reps ... Enter "end" to end: ')
while sales_reps != "end":
    dealer = input('\t\t{}\'s dealership: '.format(sales_reps))
    print('\nRequirement 5:\n--dictionary entry--')
    # record input data into dictionary
    Reps_dealers[sales_reps] = dealer

    sales_reps = input('\tEnter first and last name of '
                       'sales reps ... Enter "end" to end: ')
# Creating nested loop
print('Requirement 6:\n\t--Initiating Nested Loop--\n')
# creating nested loop
print('Requirement 7:')
# Outer loop using weeks tuple
cars_sold_thursday = []
cars_sold_friday = []
cars_sold_saturday = []
for key in Reps_dealers.keys():
    for week in weeks:
        print('\n\n\tEntering cars for {}'.format(week))
        print('\n\nRequirement 8:')
        # Create lists for cars sold per day
        # Request user data entry for cars sold per day per week using days tuple
        # Initiate counter
        cars_sold_thursday.append(int(input('\n\t\t{} cars '
                                            'sold by {}: '.format(days[0], key))))
        cars_sold_friday.append(int(input('\n\t\t{} cars sold '
                                          'by {}: '.format(days[1], key))))
        cars_sold_saturday.append(int(input('\n\t\t{} cars sold '
                                            'by {}: '.format(days[2], key))))

print('\n\nRequirement 9:\nCustomer Compliments:')
# Initiate counter for compliments
c = 1
# create compliments list
comp_list = []
# 'while loop' to loop for 20 total compliments
while c <= 20:
    compliments = input('\n\t{}: '.format(c))
    # Update compliment count variable
    c += 1
    # Append compliments to list
    comp_list.append(compliments)

print('\nRequirement 10:')
for key in Reps_dealers:
    print('\n\tCompliments for {}:'.format(key))
    c = 1
    for compliments in comp_list:
        if key in compliments:
            print('\n\t\t', c, compliments)
            c += 1
    
    print('\n\tTotal number of compliments: {}'.format(c - 1))

print('\nRequirement 11:\nReport of Sales:')
# 'for' outer loop of sales reps
i = 0
for key, value in Reps_dealers.items():
    print('\n\t', key, 'of', value)
    print('\n\tCars Sold')
    total_cars = 0
    for week in weeks:
        print('\n\t', week)
        print('\n\t\t{}: {}'.format(days[0], cars_sold_thursday[i]))
        total_cars += cars_sold_thursday[i]
        print('\n\t\t{}: {}'.format(days[1], cars_sold_friday[i]))
        total_cars += cars_sold_friday[i]
        print('\n\t\t{}: {}'.format(days[2], cars_sold_saturday[i]))
        total_cars += cars_sold_saturday[i]
        i += 1

    print('\n\tTotal Cars Sold: {}'.format(total_cars))
    print('\n\tAverage Cars Sold: ', (total_cars/6))
    print('\n\tNumber of Compliments: {}'.format(comp_list.count(key)))

print('\n\n Requirement 12:\n\tThis assignment was much more difficult for me than the others but it '
      'helped me learn what operations worked with each (tuples, lists, and dictionaries). It was '
      'confusing to have them all merged into one program and remembering what was what.')
