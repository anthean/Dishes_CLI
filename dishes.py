import sys

class Dish:
    def __init__(self, name) -> None:
        self.name = name

        #self.ingredients = ingredients
        
        
class DishHandler(Dish):
    def __init__(self) -> None:
        self.dict = {} 
        
    def addDish(self, name):
        if name in self.dict:
            print("Dish already exists!")

        dish = Dish(name)
        self.dict[name]

    
    def viewDishes(self):
        print('*'*20)
        print("Here are all of your dishes: ")
        print('*'*20)

        for i in self.dict:
            print(i)
    


update

def ask_for_int(question: str) -> int:
    val = input(question)
    try:
        return int(val)
    except:
        print('Please enter a valid integer value\n')
        return ask_for_int(question)
    

def main():
    '''
    We'll be handling the input here
    '''
    dish = Dish()

    running = True
    while(running):
        command = ask_for_int("\nEnter an integer to indicate a command: \n[1] Show all recipes\n[2] Add recipe\n[3] Delete recipe\n[4] Exit\n")

        if command == 1:
            pass

        elif command == 2:
            recipe = input("Enter the recipe name: ")
            dish.addDish(recipe)
            print("{0} has been added.".format(recipe))

        elif command == 3:
            deletedRecipe = input("What recipe would you like to delete?: ")
            print("{0} has been successfully deleted.".format(deletedRecipe))

        elif command == 4:
            print("Exiting program...")
            running = False

        else:
            print("Invalid command: {0}. Please try again.\n".format(command))


# Boilerplate code that proects users from accidentally invoking the script unintentionally
if __name__ == "__main__":
    main()