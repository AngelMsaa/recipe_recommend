# Script where you write the ingredients that you have and it will give you a recipe through an API.
import os
import inflect


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


class Pantry:

    def __init__(self):
        self.inflect = inflect.engine()
        self._ingredients = {}

    @property
    def ingredients(self):
        return self._ingredients

    def add_ingredient(self, quantity, ingredient):
        quantity = int(quantity)

        # If ingredient already exists in pantry
        if ingredient in self._ingredients:
            self._ingredients[ingredient] += quantity

            if self._ingredients[ingredient] == 1:
                ingredient = self.inflect.singular_noun(ingredient)
            else:
                ingredient = self.inflect.plural(ingredient)

            self._ingredients[ingredient] = self._ingredients.pop(ingredient)

        # If ingredient does not exist in pantry
        else:

            if quantity == 1:
                ingredient = self.inflect.singular_noun(ingredient)
            else:
                ingredient = self.inflect.plural(ingredient)

            self._ingredients[ingredient] = quantity

    def format_ingredients_for_print(self):
        return ", ".join(f"{value} {self.inflect.plural(key) if value > 1 else key}" for key, value in self._ingredients.items())


def main():

    pantry = Pantry()

    while True:
        try:
            cls()
            if len(pantry.ingredients) > 0:

                print(f"Your pantry: {pantry.format_ingredients_for_print()}\n")
            added_item = input(f"Enter the ingredients you have, separated by commas. If you have many, add a number in front (e.g., '2 Carrots'). Press Ctrl + D when done.\n>>> ")

            quantity, ingredient

            pantry.add_ingredient(quantity, ingredient)

        except EOFError:
            break


if __name__ == "__main__":
    main()
