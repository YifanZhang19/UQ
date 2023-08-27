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
    """Record the spend time

    :return:
        The time for assignment
    """
    hours = 119.7
    return hours


def get_recipe_name(recipe: tuple[str, str]) -> str:
    """Gets the recipe name.

    Args:
      recipe: A tuple with recipe name and ingredients.

    Returns:
      The name of the recipe.
    """

    return recipe[0]


def parse_ingredient(raw_ingredient_detail: str) -> tuple[float, str, str]:
    """Gets the ingredient details.

    Args:
      raw_ingredient_detail: A string with ingredients.

    Returns:
      The ingredient breakdown from the details amount, measure, and ingredient.
    """
    # split the raw ingredient to three parts
    reverse_str = raw_ingredient_detail.split(' ')
    ingredient_name = ' '.join(reverse_str[2:])
    parse = tuple((float(reverse_str[0]), reverse_str[1], ingredient_name))
    return parse


def create_recipe() -> tuple[str, str]:
    """Creates a recipe.

    Returns:
      The recipe in tuple[str, str] format after a series of prompting.
    """

    ingredient_list = []
    recipe_name = input("Please enter the recipe name: ").lower()
    flag = True
    while flag:  # an infinite loop to get ingredients
        ingredient = input("Please enter an ingredient: ")
        if ingredient != "":
            ingredient_list.append(ingredient)
        else:
            flag = False
    new_recipe = tuple((recipe_name, ','.join(ingredient_list)))
    return new_recipe


def recipe_ingredients(recipe: tuple[str, str]) -> \
        tuple[tuple[float, str, str]]:
    """This transforms a given recipe from the string form into the tuples form.

    Args:
      recipe: A tuple with recipe name and ingredients.

    Returns:
      The ingredients of a recipe amount, measure, and ingredient.
    """

    ingredients = recipe[-1]
    each_ingredient = ingredients.split(",")
    times = 0
    content_list = []
    # the loop time in how many ingredients in recipe
    while times < len(each_ingredient):
        operation = each_ingredient[times]  # get each ingredient
        reverse_string = operation.split(' ')
        ingredient_name = ' '.join(reverse_string[2:])
        each_content = tuple((float(reverse_string[0]),
                                str(reverse_string[1]), ingredient_name))
        times += 1
        content_list.append(each_content)
    all_content = tuple(content_list)
    return all_content


def add_recipe(new_recipe: tuple[str, str],
               recipes: list[tuple[str, str]]) -> None:
    """Add a given recipe, new_recipe, into the list of recipes.

    Args:
      new_recipe: a tuple with recipe name and ingredient
      recipes: a list with one or more tuple recipe

    Returns:
      None
    """

    recipes.append(new_recipe)


def find_recipe(recipe_name: str, recipes: list[tuple[str, str]]) \
        -> tuple[str, str] | None:
    """This function should attempt to find the recipe by the given recipe name
        within the list of recipes.

    Args:
      recipe_name: a string for recipe name
      recipes: a list with one or more tuple recipe

    Returns:
      A recipe or None.
    """

    for recipe in recipes:
        if recipe[0] == recipe_name:  # check the recipe name in recipes
            return recipe
    return None


def remove_recipe(name: str, recipes: list[tuple[str, str]]) -> None:
    """Remove a recipe from the list of recipes given the name of a recipe.

    Args:
      name: a string for recipe name
      recipes: a list with one or more tuple recipe

    Returns:
      None.
    """
    # if the recipe in recipes, remove it.
    for recipe in recipes:
        if recipe[0] == name:
            recipes.remove(recipe)
            return


def get_ingredient_amount(ingredient: str, recipe: tuple[str, str]) \
        -> tuple[float, str] | None:
    """Get the ingredient amount and measure.

    Args:
      ingredient: a string for ingredient name
      recipe: a tuple with recipe name and ingredient

    Returns:
      The amount and measure of a certain ingredient as a tuple[float, str]
    """

    ingredients = recipe[1].split(",")  # get ingredient detail
    # find need information and format it.
    for i in ingredients:
        if ingredient in i:
            contents = i.split(" ")
            amount_measure = tuple((float(contents[0]), contents[1]))
            return amount_measure
    return None


def add_to_shopping_list(ingredient_details: tuple[float, str, str],
                         shopping_list: list[tuple[float, str, str] | None]) \
        -> None:
    """Add an ingredient to the shopping list which could be empty or could
        contain tuples of ingredient details.

    Args:
      ingredient_details: a tuple with ingredient detail
      shopping_list: a list with ingredient detail in a tuple 

    Returns:
      None
    """

    ingredient_name = ingredient_details[-1]
    flag = False
    # check the ingredient in or not in shopping list
    for i in shopping_list:
        if ingredient_name in i:
            position = shopping_list.index(i)
            flag = True
            break
    # if in shopping list run the add amount else append to shopping list
    if flag:
        amount = shopping_list[position][0] + ingredient_details[0]
        shopping = list(shopping_list[position])
        shopping[0] = amount
        shopping_content = tuple(shopping)
        shopping_list[position] = shopping_content
    else:
        shopping_list.append(ingredient_details)


def remove_from_shopping_list(ingredient_name: str, amount: float,
                              shopping_list: list) -> None:
    """Remove a certain amount of an ingredient, with the given ingredient_name,
        from the shopping_list.

    Args:
      ingredient_name: a string with ingredient name
      amount: the ingredient amount
      shopping_list: a list with ingredient detail

    Returns:
      None
    """
    # find each ingredient position
    for i in shopping_list:
        if ingredient_name in i:
            position = shopping_list.index(i)
            cur_amount = shopping_list[position][0] - amount
            if cur_amount <= 0:  # if the amount less 0, delete this ingredient
                del shopping_list[position]
            else:
                shopping = list(shopping_list[position])
                shopping[0] = cur_amount  # replace amount
                shopping_content = tuple(shopping)
                shopping_list[position] = shopping_content


def generate_shopping_list(recipes: list[tuple[str, str]]) \
        -> list[tuple[float, str, str]]:
    """Create a shopping list by recipes.

    Args:
      recipes: a list with ingredients

    Returns:
      Return a list of ingredients,(amount, measure, ingredient name).
    """

    content_name = []
    shopping_list = []
    for i in recipes:
        for j in i[1:]:
            each_content = j.split(',')
            # get ingredient details
            for m in each_content:
                contents = m.split(' ')
                amount = float(contents[0])
                measure = contents[1]
                name = ' '.join(contents[2:])
                # check if ingredient in shopping list add the amount
                # else add ingredient to shopping list
                if name in content_name:
                    shopping_list[content_name.index(name)][0] = \
                        shopping_list[content_name.index(name)][0] + amount
                else:
                    content_name.append(name)
                    shopping_list.append([amount, measure, name])
    #  switch each ingredient to tuple
    for i in range(len(shopping_list)):
        shopping_list[i] = tuple(shopping_list[i])
    return shopping_list


def display_ingredients(shopping_list: list[tuple[float, str, str]]) -> None:
    """Print the given shopping list in alpha order.

    Args:
      shopping_list: a list of ingredients,(amount, measure, ingredient name)

    Returns:
      None
    """
    # sort the list by ingredient name in alpha order
    shopping_list.sort(key=lambda x: x[2])
    amount = []
    # get maximum length for amount
    for i in shopping_list:
        amount_str = len(str(i[0]))
        amount.append(amount_str)
    if len(amount) != 0:
        max_amount = max(amount)
    measure = []
    # get maximum length for measure
    for i in shopping_list:
        measure_str = len(i[1])
        measure.append(measure_str)
    if len(measure) != 0:
        max_measure = max(measure)
    name = []
    # get maximum length for name
    for i in shopping_list:
        name_str = len(i[2])
        name.append(name_str)
    if len(name) != 0:
        max_name = max(name)
    display_ingredient = ''
    new_list = []
    # switch to list
    for j in shopping_list:
        new_list.append(list(j))
    # for use center function, change measure length to even
    for i in new_list:
        if len(i[1]) % 2 != 0:
            i[1] = " " + i[1]
    # format the shopping list
    for i in new_list:
        ingredients = '| ' + str(i[0]).rjust(max_amount, ' ') + ' | ' \
                      + i[1].center(max_measure, ' ') + '  | ' \
                      + i[2].ljust(max_name, ' ') + '  |\n'
        display_ingredient += ingredients
    print(display_ingredient, end='')


def sanitise_command(command: str) -> str:
    """Make the command in a format.

    Args:
      command: a string for command

    Returns:
      Return a standardised command to all lower-case and no leading or
      trailing white spaces removing
        any numbers from the string.
    """

    command = ''.join([i for i in command if not i.isdigit()])
    # filter all digit one, to get all alpha
    command = command.lower().strip()
    # remove space in the head and rear, make all characters lower
    return command


def main():
    """ This function to control logical of all functions above.
    """
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
    collection = []
    shop_list = []
    while flag:
        command = input("Please enter a command: ")
        if command == "H" or command == "h":
            print(HELP_TEXT)
        elif command == "Q" or command == "q":
            flag = False
        elif command == "mkrec":
            new_recipe = create_recipe()
            recipe_collection.append(new_recipe)
        elif (command.split(' '))[0] == 'add':
            add_command = sanitise_command(command)
            find_name = ' '.join((add_command.split(' '))[1:])
            recipe = find_recipe(find_name, recipe_collection)
            if recipe is not None:
                add_recipe(recipe, collection)
            else:
                print("\nRecipe does not exist in the cook book. ")
                print("Use the mkrec command to create a new recipe.\n")
        elif ' '.join(command.split(' ')[0:2]) == 'rm -i':
            amount = float((command.split(' '))[-1])
            name = ' '.join((command.split(' '))[2:-1])
            remove_from_shopping_list(name, amount, shop_list)
        elif (command.split(' '))[0] == 'rm':
            rm_command = sanitise_command(command)
            remove_name = ' '.join((rm_command.split(' '))[1:])
            remove_recipe(remove_name, shop_list)
        elif command == "G" or command == "g":
            shop_list = generate_shopping_list(collection)
            display_ingredients(shop_list)
        elif command == "ls":
            if len(collection) == 0:
                print("No recipe in meal plan yet.")
            else:
                print(collection)
        elif command == "ls -a":
            for i in recipe_collection:
                print(get_recipe_name(i))
        elif command == "ls -s":
            display_ingredients(shop_list)
        else:
            print("enter is wrong")


if __name__ == "__main__":
    main()

