class Recipe:
    def __init__(self, title: str, ingredients: list):
        self.title = title 
        self.ingredients = ingredients
    
    def add_ingridients(self, ingredient: Ingredient):
        for i in self.ingredients:
            if i == self.ingredient:
                i.quantity += ingredient.quantity
                return 
        self.ingredients.append(self.ingredient)

    @staticmethod
    def is_valid_ratio(ratio):
        if isinstance(ratio, bool):
            return False
        return isinstance(ratio, )
        