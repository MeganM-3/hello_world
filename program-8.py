# intro() to call requirements 1 and 2
def intro():
    print('Requirement 1:\nThis is Program 8 - Megan Weir')
    print('\n\nRequirement 2:\nThis program keeps track of Pokemon characters\n\n')


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
        print('\nRequirement 3\n')
        return self.__name

    # Get INSTANCE variable self.__ability
    def get_ability(self):
        print('\nRequirement 3\n')
        return self.__ability


# main() function
def main():
    intro()
    print('\n###############  In main ()  ###############')
    pokemon_list = add_pokemon()
    display_pokemon(pokemon_list)
    feedback()


# add_pokemon() function
def add_pokemon():
    print("\nIn add_pokemon()")
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
        # Increment counter
        pokemon_number += 1
        more_pokemon = input("\nAnother pokemon to enter? (y/n) ").lower()

    return pokemon_list


def display_pokemon(pokemon_list):
    print('\nRequirement 4\n')
    print('\nRequirement 5\nProduce output')
    # initiate counter variable
    pokemon_number = 1
    # output user entered data
    for pokemon in pokemon_list:
        print('\nName of Pokemon #{}: {}'.format(pokemon_number, pokemon.get_name()))
        print('\nAbility of Pokemon #{}: {}'.format(pokemon_number, pokemon.get_ability()))
        pokemon_number += 1


# provide student feedback
def feedback():
    print('\nRequirement 6\nThis assignment was fairly easy but understanding how the class and '
          'class methods span across the rest of the module and into main() was weird. With all '
          'the layering involved, I think I was over-complicating the display_pokemon function.')


# Determine if program is run as the main or a module
if __name__ == '__main__':
    # This program is being run as the main program
    main()

else:
    pass
    # Do nothing. This module has been imported by another
    # module that wants to make use of the functions,
    # classes, and/or other items it has defined.
