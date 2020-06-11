from myapp.models.database_manager import DatabaseManager
from myapp.models.api_manager import ApiManager


class Application:
    """ Object that will manage the classes of models and views """
    def __init__(self):
        self.DatabaseManager = DatabaseManager()
        self.ApiManager = ApiManager()
        self.list_categories = ["pizzas", "spread", "snacks", "cheeses", "desserts"]

    def display_start_menu(self):
        list_categories = self.list_categories
        for i in list_categories:
            list_product = self.ApiManager.get_data(i)
            self.DatabaseManager.put_products(list_product)


        var_bool = True
        while var_bool:
            User_enter_1 = int(input("1. Quel aliment souhaitez-vous remplacer ?, 2. Mes aliments substitués"))
            if User_enter_1 == 1:
                self.DatabaseManager.get_products("product_name", "category", "pizzas")
