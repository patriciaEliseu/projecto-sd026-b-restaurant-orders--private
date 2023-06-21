from csv import DictReader
from typing import Dict

from src.models.dish import Recipe
from src.models.ingredient import Ingredient

BASE_INVENTORY = "data/inventory_base_data.csv"

Inventory = Dict[Ingredient, int]


def read_csv_inventory(inventory_file_path=BASE_INVENTORY) -> Inventory:
    inventory = dict()

    with open(inventory_file_path, encoding="utf-8") as file:
        for row in DictReader(file):
            ingredient = Ingredient(row["ingredient"])
            inventory[ingredient] = int(row["initial_amount"])

    return inventory


# Req 5
class InventoryMapping:
    def __init__(self, inventory_file_path=BASE_INVENTORY) -> None:
        self.inventory = read_csv_inventory(inventory_file_path)

    def _load_inventory(self, inventory_path: str) -> Dict[str, int]:
        inventory = {}
        with open(inventory_path, "r") as file:
            for line in file:
                ingredient, quantity = line.strip().split(",")
                inventory[ingredient] = int(quantity)
        return inventory

    # Req 5.1
    def check_recipe_availability(self, recipe: Recipe) -> bool:
        def check_recipe_availability(self, recipe: Dict[str, int]) -> bool:
            for ingredient, required_quantity in recipe.items():
                if (
                    ingredient not in self.inventory
                    or self.inventory[ingredient] < required_quantity
                ):
                    return False
            return True

    # Req 5.2
    def consume_recipe(self, recipe: Recipe) -> None:
        def consume_recipe(self, recipe: Dict[str, int]) -> None:
            if not self.check_recipe_availability(recipe):
                raise ValueError("Recipe is not available for consumption")

            for ingredient, required_quantity in recipe.items():
                self.inventory[ingredient] -= required_quantity
