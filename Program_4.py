# Program-4.pyo

# Program title
print('\nRequirement 1')
print('This is Program 4 - Megan Weir')

# Program header
print('\nRequirement 2')
print('This program provides airline seat assignments.')


print('\n\nRequirement 3')

# Obtain passenger first and last name
first_name = input('\nFirst name: ')
last_name = input('Last name: ')

# Obtain priority status
priority_status = input('\nPlease input priority status (Platinum, Gold, or Newbie): ')

# Obtain seat preference
seat_pref = input('Please input your seat preference (First Class, Business, or Coach): ')

# Obtain ticket budget
ticket_budget = input('Please input your ticket budget (Colossal, Big Bucks, or Peanuts): ')


print('\n\nRequirement 4')
# 'if elif statements'
# Determine output message based on priority status and ticket budget
if priority_status == 'Platinum' and ticket_budget == 'Colossal':
    print('\n{} {}, you qualify for First Class and they are exceptional seats!'.format(first_name, last_name))
elif priority_status == 'Platinum' and ticket_budget == 'Big Bucks':
    print('\n{} {}, you have Business and they are ok seats. We suggest you '
          'spend more money to get better seats.'.format(first_name, last_name))
elif priority_status == 'Platinum' and ticket_budget == 'Peanuts':
    print('\nReally? {} {}, you are in Coach and will be sorry.'.format(first_name, last_name))
elif priority_status == 'Gold' and ticket_budget == 'Colossal':
    print('\n{} {}, you qualify for First Class. Did you get a promotion?'.format(first_name, last_name))
elif priority_status == 'Gold' and ticket_budget == 'Big Bucks':
    print('\n{} {}, you have Business, as usual. You know we do '
          'recommend First Class.'.format(first_name, last_name))
elif priority_status == 'Gold' and ticket_budget == 'Peanuts':
    print("\n{} {}, really? You can do better don't you think?".format(first_name, last_name))
elif priority_status == 'Newbie' and ticket_budget == 'Colossal':
    print("\n{} {}, we are running your credit card again to ensure "
          "there are no mistakes. Looks like you may get First Class. "
          "Please behave.".format(first_name, last_name))
elif priority_status == 'Newbie' and ticket_budget == 'Big Bucks':
    print("\nHmmm... Our fashion consultant will ensure you are professionally "
          "dressed. If so, it is Business for you, {} {}.".format(first_name, last_name))
elif priority_status == 'Newbie' and ticket_budget == 'Peanuts':
    print("\n{} {}, we apologize in advance for the crying baby next to you. Please limit "
          "peanut request to one 1 oz. bag.".format(first_name, last_name))

print('\n\nRequirement 5')

# Obtain survey scores
print('\nHope you enjoyed your flight! Please complete the following '
      'survey questions with a score of 1 - 5 (1 = dissatisfied; 5 = outstanding):\n')
flight_score = int(input('Did you have a good flight? '))
food_score = int(input('Was the food fantastic? '))
movie_score = int(input('How was the movie selection? '))

# calculate total survey score
total_score = flight_score + food_score + movie_score

print('\n\nRequirement 6\n')

# 'Nested if else elif statements'
# Determine if customer satisfaction is below expectations and generate output message
if priority_status == 'Platinum' and total_score < 12 or flight_score < 4 or food_score < 4 or movie_score < 4:
    print('Your total survey score of {} was lower than we would like. Please give us another '
          'opportunity soon.'.format(total_score))
elif priority_status == 'Gold' and total_score < 11 or flight_score < 3 or food_score < 3 or movie_score < 3:
    print('Your total survey score of {} was lower than we would like. The next time you fly you '
          'receive a complementary soft drink.'.format(total_score))
elif priority_status == 'Newbie' and total_score < 10 or flight_score < 2 or food_score < 2 or movie_score < 2:
    print('Your total survey score of {} was lower than we would like. You will have more fun next time.')

# Student feedback
print('\n\nRequirement 7')
print('\nThis was definitely more complex than program 3.')
