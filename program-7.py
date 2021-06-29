reps_dealers = {}
weeks = ('Week One', 'Week Two')
days = ('Thursday', 'Friday', 'Saturday')
cars_sold_thursday = []
cars_sold_friday = []
cars_sold_saturday = []
comp_list = []


# Outputs program header
def program_header():
    print('Requirement 1:')
    print('This is Program 7 - Megan Weir')


# Outputs program purpose
def program_purpose():
    print('\n\nRequirement 2\n')
    print('This program practices working with lists, strings, tuples, and dictionaries.')


# Creates tuples for weeks and days
def create_tuples():
    print('\n\nRequirement 3\n--Call tuples--')
    global weeks
    print(weeks)
    global days
    print(days)


# Creates loop to collect sales rep data
def sales_persons():
    print('\n\nRequirement 4:\n')
    global reps_dealers
    # Collect sales reps' names and dealership with while loop
    sales_reps = input('Enter first and last name of sales reps ... Enter "end" to end: ')
    while sales_reps != "end":
        dealer = input('{}\'s dealership: '.format(sales_reps))
        print('\nRequirement 5:\n--dictionary entry--')
        # record input data into dictionary
        reps_dealers[sales_reps] = dealer

        sales_reps = input('Enter first and last name of sales reps ... Enter "end" to end: ')


def nested_loop_cars_sold_intro():
    # Creating nested loop
    print('Requirement 6:\n\t--Initiating Nested Loop--\n')


def nested_loop_cars_sold():
    print('Requirement 7:')
    global reps_dealers
    global weeks
    global cars_sold_thursday
    global cars_sold_friday
    global cars_sold_saturday
    global days
    for key in reps_dealers.keys():
        # Outer loop using weeks tuple

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


def compliments_loop():
    print('\n\nRequirement 9:\nCustomer Compliments:')
    global comp_list
    # Initiate counter for compliments
    c = 1
    # 'while loop' for 20 total compliments
    while c <= 20:
        compliments = input('\n\t{}: '.format(c))
        # Update compliment count variable
        c += 1
        # Append compliments to list
        comp_list.append(compliments)


def print_compliments():
    print('\nRequirement 10:')
    global reps_dealers
    global comp_list
    for key in reps_dealers.keys():
        print('\n\tCompliments for {}:'.format(key))
        c = 1
        for compliments in comp_list:
            if key in compliments:
                print('\n\t\t{}: {}'.format(c, compliments))
                c += 1

        print('\n\tTotal number of compliments: {}'.format(c - 1))


def final_output():
    print('\nRequirement 11:\nReport of Sales:')
    global reps_dealers
    global weeks
    global days
    global cars_sold_thursday
    global cars_sold_friday
    global cars_sold_saturday
    global comp_list
    # 'for' outer loop of sales reps
    i = 0
    for key, value in reps_dealers.items():
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
        c = 1
        for compliments in comp_list:
            if key in compliments:
                c += 1
        print('\n\tNumber of Compliments: {}'.format(c - 1))


def feedback():
    print('\n\n Requirement 12:\n\tThis program\'s concepts were easier to understand.')


def main():
    program_header()
    program_purpose()
    create_tuples()
    sales_persons()
    nested_loop_cars_sold_intro()
    nested_loop_cars_sold()
    compliments_loop()
    print_compliments()
    final_output()
    feedback()


# Determine if program is run as the main or a module
if __name__ == '__main__':
    # This program is being run as the main program
    main()

else:
    pass
