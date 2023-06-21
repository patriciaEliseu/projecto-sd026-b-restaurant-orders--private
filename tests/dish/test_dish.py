from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction
import pytest


# Req 2
def test_dish():
    dish = Dish('pasta', 10.0)
    assert dish.name == 'pasta'
    assert dish.price == 10.0
    assert dish.recipe == {}

    with pytest.raises(TypeError):
        Dish('pasta', '10.0')

    with pytest.raises(ValueError):
        Dish('pasta', 0)

    dish1 = Dish('pasta', 10.0)
    dish2 = Dish('pasta', 10.0)
    assert dish1 == dish2

    assert dish != 1

    dish1 = Dish('pasta', 10.0)
    dish2 = Dish('pizza', 15.0)
    assert dish1 != dish2

    dish1 = Dish('pasta', 10.0)
    dish2 = Dish('pasta', 10.0)
    assert hash(dish1) == hash(dish2)

    dish1 = Dish('pasta', 10.0)
    dish2 = Dish('pizza', 15.0)
    assert hash(dish1) != hash(dish2)

    farinha = Ingredient('farinha')
    bacon = Ingredient('bacon')

    dish.add_ingredient_dependency(farinha, 2)
    dish.add_ingredient_dependency(bacon, 3)

    assert dish.recipe.get(farinha) == 2
    assert dish.recipe.get(bacon) == 3
    assert dish.get_ingredients() == {farinha, bacon}

    assert dish.get_restrictions() == farinha.restrictions.union(bacon.restrictions)

    with pytest.raises(TypeError):
        dish.get_ingredients('InvalidArgument')

        with pytest.raises(TypeError):
            dish.get_restrictions('InvalidArgument')

        dish_repr = f"Dish('{dish.name}', R${dish.price:.2f})"
        assert dish_repr == repr(dish)
