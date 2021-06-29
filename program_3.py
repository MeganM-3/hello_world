print('\nRequirement 1\n')
print('This is Program 3\n')

print('\nRequirement 2\n')
print('This program records votes for best players in the world.\n')

print('\nRequirement 3\n')
soc_player1 = input('Enter name of a soccer player: ')
soc_player2 = input('Enter name of a soccer player: ')
soc_player3 = input('Enter name of a soccer player: ')

print('\n\nRequirement 4\n')
svote_1 = int(input('Total number of votes for {}: '.format(soc_player1)))
svote_2 = int(input('Total number of votes for {}: '.format(soc_player2)))
svote_3 = int(input('Total number of votes for {}: '.format(soc_player3)))

print('\n\nRequirement 5\n')
if svote_1 > svote_2 and svote_1 > svote_3:
    print('\nRequirement 6')
    print('\n{} is the winner with {} votes!\n'.format(soc_player1, svote_1))
if svote_2 > svote_1 and svote_2 > svote_3:
    print('\nRequirement 6')
    print('\n{} is the winner with {} votes!\n'.format(soc_player2, svote_2))
if svote_3 > svote_1 and svote_3 > svote_2:
    print('\nRequirement 6')
    print('\n{} is the winner with {} votes!\n'.format(soc_player3, svote_3))
else:
    print('\nRequirement 6\nNo Winner.')

print('\nRequirement 7\n')
bas_player1 = input('Enter name of a basketball player: ')
bas_player2 = input('Enter name of a basketball player: ')
bas_player3 = input('Enter name of a basketball player: ')

print('\n\nRequirement 8\n')
bvote_1 = int(input('Total number of votes for {}: '.format(bas_player1)))
bvote_2 = int(input('Total number of votes for {}: '.format(bas_player2)))
bvote_3 = int(input('Total number of votes for {}: '.format(bas_player3)))

print('\n\nRequirement 9\n')
if bvote_1 > bvote_2 and bvote_1 > bvote_3:
    print('\nRequirement 10')
    print('\n{} is the winner with {} votes!\n'.format(bas_player1, bvote_1))
if bvote_2 > bvote_1 and bvote_2 > bvote_3:
    print('\nRequirement 10')
    print('\n{} is the winner with {} votes!\n'.format(bas_player2, bvote_2))
if bvote_3 > bvote_1 and bvote_3 > bvote_2:
    print('\nRequirement 10')
    print('\n{} is the winner with {} votes!\n'.format(bas_player3, bvote_3))
else:
    print('\nRequirement 10\n No Winner.')
print('\nRequirement 11\n')
print('I enjoyed program 3 which allowed me to incorporate the course content I have learned so far.')
