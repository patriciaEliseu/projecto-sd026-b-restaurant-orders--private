import csv

from src.models.dish import Dish
from src.models.ingredient import Ingredient


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.source_path = source_path
        self.dishes = set()
        self.load_data()

    def load_data(self):
        dish_dict = {}
        with open(self.source_path, "r") as file:
            csv_reader = csv.reader(file)
            next(csv_reader)
            for row in csv_reader:
                dish_name = row[0]
                dish_price = float(row[1])
                ingredient_name = row[2]
                ingredient_quantity = int(row[3])

                ingredient = Ingredient(ingredient_name)

                if dish_name not in dish_dict:
                    dish = Dish(dish_name, dish_price)
                    dish_dict[dish_name] = dish
                else:
                    dish = dish_dict[dish_name]

                dish.add_ingredient_dependency(ingredient, ingredient_quantity)

            self.dishes = set(dish_dict.values())
