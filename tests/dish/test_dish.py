from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction
import pytest


# Req 2
def test_dish():
    food = Dish("hamburguer", 15.0)
    assert food.name == "hamburguer"
    food2 = Dish("pizza", 27.0)
    assert food2.name != food.name
    assert food2 != food
    food3 = Dish("hamburguer", 15.0)
    assert food3.name == food.name
    assert food3 == food
    assert hash(food) == hash(food3)
    assert hash(food) != hash(food2)
    food_rpr = "Dish('hamburguer', R$15.00)"
    assert repr(food) == food_rpr
    assert repr(food2) != food_rpr
    item1 = Ingredient("bacon")
    food.add_ingredient_dependency(item1, 2)
    assert food.recipe.get(item1) == 2
    assert food.recipe.get(item1) != 3
    assert food.get_ingredients() == {item1}
    needed_restrictions = {Restriction.ANIMAL_DERIVED, Restriction.ANIMAL_MEAT}
    assert food.get_restrictions() == needed_restrictions

    with pytest.raises(TypeError):
        Dish("pizza", "27.0")

    with pytest.raises(ValueError):
        Dish("pizza", -27.0)
