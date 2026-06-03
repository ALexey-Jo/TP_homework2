class DietaryRecipe:
    def __init__(self, title, diet_type, ingredients = None):
        self.title = title 
        self.diet_type = diet_type
        if ingredients is None:
            ingredients = []
        super().__init__(title, ingredients)

    def scale(self, ratio: float):
        sc_recipe = super().scale(ratio)
        new_recipe = DietaryRecipe(sc_recipe.title, self.diet_type, sc_recipe.ingredients)
        return new_recipe
    
    def __str__(self):
        res_pr = f"[{self.diet_type}] {self.title}"
        for i in self.ingredients:
            res_pr += "\n - " + str(i)
        return res_pr
    
