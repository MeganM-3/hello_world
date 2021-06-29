def intro():
    print('Requirement 1:\nThis is Program 9 - Megan Weir')
    print('\n\nRequirement 2:\nThis program keeps track of Pokemon'
          ' characters, saves the data to a file, and displays the data from the file.\n\n')


# Pokemon class definition
class Pokemon:
    # __init__ called AUTOMATICALLY when an object is created
    def __init__(self, name, ability):
        # Assign argument 'name' to instance variable 'self.__name'
        self.__name = name
        # Assign argument 'ability' to instance variable 'self.__ability'
        self.__ability = ability

    # Get INSTANCE VARIABLE self.__name
    def get_name(self):
        return self.__name

    # Get INSTANCE variable self.__ability
    def get_ability(self):
        return self.__ability


def display_data(file_name):
    print('\nProduce output')
    pokemon_number = 1
    for line in file_name:
        file_name.read
        print('\nName of Pokemon #{}: {}'.format(pokemon_number, file_name(line)))
        print('\nAbility of Pokemon #{}: {}'.format(pokemon_number, file_name(line)))
        pokemon_number += 1


# main() function
def main():
    file_name = "my_pokemon.txt"
    intro()
    save_data(file_name)
    display_data(file_name)
    print('\n###############  In main ()  ###############')
    print("\nRequirement 3\n--calling 'save_data()' function--")
    print("\nRequirement 4\n--calling 'display_data()' function--")
    feedback()


# add_pokemon() function
def save_data(file_name):
    print("\nIn add_pokemon()")
    file_data = open(file_name, "w+")
    # Create new list to hold pokemon characters
    pokemon_list = []
    # Counter used in loop
    pokemon_number = 1
    more_pokemon = input("\nDo you have a pokemon to enter? (y/n): ").lower()
    while more_pokemon == 'y':
        # Get the name of the pokemon from user
        pokemon_name = input('\nEnter name for Pokemon #{}: '.format(pokemon_number))
        # Get the ability of the pokemon from user
        pokemon_ability = input('\nEnter ability for Pokemon #{}: '.format(pokemon_number))
        # Create a new pokemon object with pokemon_name and pokemon_ability
        new_pokemon = Pokemon(pokemon_name, pokemon_ability)
        # Add new_pokemon to list
        pokemon_list.append(new_pokemon)
        file_data.write('pokemon_list')
        # Increment counter
        pokemon_number += 1
        more_pokemon = input("\nAnother pokemon to enter? (y/n): ").lower()

    return pokemon_list


def feedback():
    print('\nRequirement 5\n XXXXXXX.')


# Determine if program is run as the main or a module
if __name__ == '__main__':
    # This program is being run as the main program
    main()

else:
    pass
    # Do nothing. This module has been imported by another
    # module that wants to make use of the functions,
    # classes, and/or other items it has defined.
