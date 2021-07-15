"""
your task is to build out the v1 of this application. It must support adding
just the name of a dish, deleting a dish, and viewing all dish names we've
added
"""
import sys
from Dish import Dish
from DishHandler import DishHandler


def ask_for_int(question: str) -> int:
    val = input(question)
    try:
        return int(val)
    except TypeError:
        print('Please enter a valid integer value\n')
        return ask_for_int(question)


def main():
    '''
    We'll be handling the input here
    '''
    dish_mngr = DishHandler()

    running = True
    while(running):
        command = ask_for_int(
            "\nEnter an integer to indicate a command: \n"
            + "[1] Show all recipes\n"
            + "[2] Add recipe\n"
            + "[3] Delete recipe\n"
            + "[4] Exit\n"
        )

        if command == 1:
            dish_mngr.viewDishes()

        elif command == 2:
            recipe = input("Enter the recipe name: ")
            dish_mngr.addDish(recipe)
            print(f"{recipe} has been added.")

        elif command == 3:
            deleted_recipe = input("What recipe would you like to delete?: ")
            dish_mngr.deleteDish(deleted_recipe)
            print(f"{deleted_recipe} has been successfully deleted.")

        elif command == 4:
            print("Exiting program...\n")
            running = False

        else:
            print("Invalid command: {0}. Please try again.\n".format(command))


if __name__ == "__main__":
    main()
