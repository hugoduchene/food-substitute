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
            User_enter_1 = int(input("1. Quel aliment souhaitez-vous remplacer ?, 2. Mes aliments substitués > "))
            if User_enter_1 == 1:
                for nbs,cat in enumerate(self.list_categories):
                    print(str(nbs) + " :"+ cat)

                User_enter_2 = int(input("Choisissez votre catégorie de produits > "))

                for nbs,cat in enumerate(self.list_categories):
                    if User_enter_2 == nbs:
                        list_food = self.DatabaseManager.get_products("product_name", "category", cat)
                        for nubs,food in enumerate(list_food):
                            (nutrient,) = food
                            print(str(nubs)+ "." + nutrient)
                            category = cat

                User_enter_3 = int(input("Choisissez Votre aliment > "))

                list_better_products = self.DatabaseManager.get_better_products(category)
                for numbs, better_products in enumerate(list_better_products):
                    (id, nutrient_grade, name, link, description, stores) = better_products
                    print("-----------------------------Substitute-------------------------------------\n")

                    print(str(numbs)+ " :" + name + " , " + description + " , " + stores + " , " + link + "\n")
                    User_enter_3 = input("Appuyez sur une touche pour voir un autre résultat " + str(numbs) + "/2 OU appuyez sur 's' pour enregistrer le résultat")

                    if User_enter_3 == "s":
                        name_user = str(input("Dit moi ton nom : "))
                        id = str(id)
                        list_user = [(name_user, id)]
                        self.DatabaseManager.record_user(list_user)
                        var_bool = False


    """def get_products_category(self):
        for nbs,cat in enumerate(self.list_categories):
            print(str(nbs) + " :"+ cat)

    def choose_category(self, User_enter_2):
        for nbs,cat in enumerate(self.list_categories):
            if User_enter_2 == nbs:
                list_food = self.DatabaseManager.get_products("product_name", "category", cat)
                for nubs,food in enumerate(list_food):
                    (nutrient,) = food
                    print(str(nubs)+ "." + nutrient)
                    category = cat

        return category

    def display_better_products(self, category):
        list_better_products = self.DatabaseManager.get_better_products(category)
        for numbs, better_products in enumerate(list_better_products):
            (id, nutrient_grade, name, link, description, stores) = better_products
            print("-----------------------------Substitute-------------------------------------\n")

            print(str(numbs)+ " :" + name + " , " + description + " , " + stores + " , " + link + "\n")
        return numbs

    def option_record_user(self, User_enter_3, id):
        if User_enter_3 == "s":
            name_user = str(input("Dit moi ton nom : "))
            list_user = [(name_user, id)]
            self.DatabaseManager.record_user(list_user)
            var_bool = False

            return var_bool"""
