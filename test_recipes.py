import pytest
from Ingredient import Ingredient

#Тесты для для класса Ingredient

class TestIngredient:
    def _test_ing(self):
        ing = Ingredient("Мука", 500, "г")
        assert ing.name == "Мука"
        assert ing.quantity == 500.0
        assert ing.unit == "г"

    def _test_str(self):
        ing = Ingredient("Мука", 500, "г")
        res = str(ing)
        assert res == "Мука: 500.0 г"
    
    def _test_eq(self):
        ing1 = Ingredient("Мука", 500, "г")
        ing2 = Ingredient("Мука", 500, "г")
        assert ing1 == ing2
    
    def _test_eq_diff_name(self):
        ing1 = Ingredient("Мука", 500, "г")
        ing2 = Ingredient("Яйцо", 500, "г")
        assert ing1 != ing2
    
    def _test_eq_diff_unit(self):
        ing1 = Ingredient("Мука", 500, "г")
        ing2 = Ingredient("Мука", 500, "кг")
        assert ing1 != ing2
    

