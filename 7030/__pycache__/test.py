"""
CSSE1001 Assignment 1
Semester 1, 2023
"""

# Fill these in with your details
__author__ = "Yifan Zhang"
__email__ = "yifan.zhang19@uq.net.au"
__date__ = "03/03/2023"

from constants import *


# Write your functions here
def num_hours() -> float:
    hours = "119.7 hours"
    return hours


def get_recipe_name(recipe: tuple[str, str]) -> str:
    """Returns the name of the recipe."""
    print(recipe[0])
    return recipe[0]



def main():
    """ Write your docstring """
    # cook book
    recipe_collection = [
        CHOCOLATE_PEANUT_BUTTER_SHAKE,
        BROWNIE,
        SEITAN,
        CINNAMON_ROLLS,
        PEANUT_BUTTER,
        MUNG_BEAN_OMELETTE
    ]
    # Write the rest of your code here
    flag = True
    while flag:
        selection = input("Please enter a command: ")
        if selection == "H" or selection == "h":
            print(HELP_TEXT)
        elif selection == "Q" or selection == "q":
            flag = False
        elif selection == "add CHOCOLATE_PEANUT_BUTTER_SHAKE":
            pass
        elif selection == "add BROWNIE":
            pass
        elif selection == "add SEITAN":
            pass
        elif selection == "add CINNAMON_ROLLS":
            pass
        elif selection == "add PEANUT_BUTTER":
            pass
        elif selection == "add MUNG_BEAN_OMELETTE":
            pass
        elif selection == "rm CHOCOLATE_PEANUT_BUTTER_SHAKE":
            pass
        elif selection == "rm BROWNIE":
            pass
        elif selection == "rm SEITAN":
            pass
        elif selection == "rm CINNAMON_ROLLS":
            pass
        elif selection == "rm PEANUT_BUTTER":
            pass
        elif selection == "rm MUNG_BEAN_OMELETTE":
            pass
        elif selection == "G" or selection == "g":
            pass
        elif selection == "ls":
            pass
        elif selection == "ls -a":
            for name in recipe_collection:
                get_recipe_name(name)
        elif selection == "ls -s":
            pass
        elif selection == "mkrec":
            pass
        else:
            print("enter is wrong")


if __name__ == "__main__":
    main()
