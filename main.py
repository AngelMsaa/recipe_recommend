# Script where you write the ingredients that you have and it will give you a recipe through an API.
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

class Pantry:

    def __init__(self):
        self._ingredients = {}

    @property
    def ingredients(self):
        return self._ingredients

    @ingredients.setter
    def ingredients(self):
        ...

    def add_ingredient(self, quantity, ingredient):
        if ingredient in self._ingredients:
            self._ingredients[ingredient] += quantity
        else:
            self._ingredients[ingredient] = quantity

    def format_ingredients_for_print(self):
        return ", ".join(f"{value} {key}" for key, value in self._ingredients.items())

def main():

    pantry = Pantry()

    while True:
        try:
            cls()
            if len(pantry.ingredients) > 0:

                print(f"Your pantry: {pantry.format_ingredients_for_print()}\n")
            quantity, ingredient = input(f"Enter the ingredients you have, separated by commas. If you have many, add a number in front (e.g., '2 Carrots'). Press Ctrl + D when done.\n>>> ").split(" ")

            pantry.add_ingredient(quantity, ingredient)

        except EOFError:
            break

    pantry_dict = {}
    for item in pantry:
        quantity, ingredient = item.split(",")
        quantity = int(quantity)
        if ingredient in pantry_dict:
            pantry_dict[ingredient] += quantity
        else:
            pantry_dict[ingredient] = quantity


    print(pantry_dict)

if __name__ == "__main__":
    main()