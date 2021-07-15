from Dish import Dish


class DishHandler(Dish):
    def __init__(self) -> None:
        self.dict = {}

    def addDish(self, name):
        if name in self.dict:
            print("Dish already exists!")
            return

        self.dict[name.lower()] = Dish(name) # All dish names will be lowercased

    def viewDishes(self):
        print('*' * 30) 
        print("Here are all of your dishes: ")
        print('*' * 30)

        if not self.dict:
            print("oh wait... there are no dishes")
        for i in self.dict:
            print(i)

    def deleteDish(self, name):
        if name not in self.dict:
            print('This dish does not exist!')
            return

        del self.dict[name]
