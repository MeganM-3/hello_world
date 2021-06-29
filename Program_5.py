print('Requirement 1\n')
# Program header
print('This is Program 5 - Megan Weir')


print('\n\nRequirement 2\n')
# Program purpose
print('This program records Austin Area Whole Foods product data.')


print('\n\nRequirement 3\n')
# Collect number of stores from user
num_stores = int(input('Enter the number of stores: '))

print('\n\nRequirement 4\n')
# Initiate store count
store = 1
# Iterate through number in range of number of stores and print numbers
for stores in range(num_stores):
    print('Store {}: '.format(store))
    # Collect store data from user
    store_name = input('Store name: ')
    store_phone = input('Store phone number: ')
    store_address = input('Store address: ')
    # Add one to variable value for each loop
    store += 1

    print('\n\nRequirement 5')
    # Create product lists
    veg_name_list = []
    veg_plu_list = []
    veg_order_quantity_list = []
    # Request product data
    print('\nEnter products... (-1) to end.')
    # Initiate product counter
    i = 1
    # Initiate while loop
    veg_name = input('\nVegetable name {}: '.format(i))
    while veg_name != "-1":
        veg_plu = input('Vegetable PLU {}: '.format(i))
        veg_quantity = input('Amount to Order {}: '.format(i))
        # Append input data to lists
        veg_name_list.append(veg_name)
        veg_plu_list.append(veg_plu)
        veg_order_quantity_list.append(veg_quantity)
        # Add one to variable to count products
        i += 1
        veg_name = input('\nVegetable name {}: '.format(i))

    print('\n\nRequirement 6\n')
    # Generate store output data
    print('{}'.format(store_name))
    print('{}'.format(store_phone))
    print('{}'.format(store_address))

    print('\n\nRequirement 7\n')
    # Initiate list index
    i = 0
    for i in range(len(veg_name_list)):
        print('Vegetable name {} - '.format(i), veg_name_list[i])

        print('Vegetable PLU {} - '.format(i), veg_plu_list[i])

        print('Amount to Order {} - '.format(i), veg_order_quantity_list[i])
        # Add one to variable to recall next item in lists
        i += 1
        print('\n')

# Student statement
print('\nRequirement 8:\n\nThis assignment was a lot harder for me when it '
      'came to recalling the values from the lists. Turned out after I '
      'went to tutoring that my only real mistake was that '
      'I appended the input to the lists after the final loop statement '
      'for veg_name rather than after asking for the final order amount.')
