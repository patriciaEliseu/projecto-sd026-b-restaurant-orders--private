from src.models.ingredient import Ingredient  # noqa: F401, E261, E501
from src.models.ingredient import Restriction


# Req 1
def test_ingredient():
    ingredient = Ingredient('farinha de trigo')
    assert ingredient.name == 'farinha de trigo'
    assert ingredient.restrictions == {Restriction.GLUTEN}

    ingredient = Ingredient('unknown_ingredient')
    assert ingredient.name == 'unknown_ingredient'
    assert ingredient.restrictions == set()

    ingredient = Ingredient('farinha de trigo')
    assert repr(ingredient) == 'Ingredient("farinha de trigo")'

    ingredient1 = Ingredient('farinha de trigo')
    ingredient2 = Ingredient('farinha de trigo')

    ingredient1 = Ingredient('farinha de trigo')
    ingredient2 = Ingredient('ovo')
    assert not ingredient1 == ingredient2

    ingredient1 = Ingredient('farinha de trigo')
    ingredient2 = Ingredient('farinha de trigo')
    assert hash(ingredient1) == hash(ingredient2)

    ingredient1 = Ingredient('farinha de trigo')
    ingredient2 = Ingredient('ovo')
    assert hash(ingredient1) != hash(ingredient2)
