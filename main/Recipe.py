from Ingredient import Ingredient
class Recipe:
    def __init__(self, title: str, ingredients: list):
        self.title = title 
        self.ingredients = ingredients
    
    def add_ingridients(self, ingredient: Ingredient):
        for i in self.ingredients:  
            if i == ingredient:
                i.quantity += ingredient.quantity
                return 
        self.ingredients.append(ingredient)

    @staticmethod
    def is_valid_ratio(ratio):
        if isinstance(ratio, bool):
            return False
        return isinstance(ratio, (int, float)) and ratio > 0
    
    def scale(self, ratio: float):
        new_ingr = [Ingredient(i.name, i.quantity * ratio, i.unit) for i in self.ingredients]
        return Recipe(self.title, new_ingr)
    
    def __len__(self):
        return len(self.ingredients)
    
    def __str__(self):
        l = [f"Рецепт: {self.title}"]
        for i in self.ingredients:
            l.append(f" - {i}")
        return "\n".join(l)
    