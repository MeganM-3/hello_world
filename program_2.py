print('\nRequirement 1\n')
print('\nThis is Program 2\n')
print('\nRequirement 2\n')
print('\nThis program calculates strawberry sales '
      'for the month.\n')
print('\nRequirement 3\n')     
more_sales_data = input('Do you have strawberry sales '
                        'data to enter? (y/n): ')
                        
total_sales_data = 0

print('\nRequirement 4\n')
while more_sales_data == "y":
    new_sales_data = int(input('\nEnter the quantity of '
                               'sales in pints: '))
    print('\nRequirement 5\n')
    total_sales_data += new_sales_data
    print('\nRequirement 6\n')
    more_sales_data = input('\nDo you have more strawberry '
                            'sales data to enter? (y/n): ')
                            
print('\nRequirement 7\n')
print('\nTotal strawberry sales in pints: {}'.format(total_sales_data))
