from myapp.models.database_manager import DatabaseManager
from myapp.models.api_manager import ApiManager


class Application:
    """ Object that will manage the classes of models and views """
    def __init__(self):
        self.DatabaseManager = DatabaseManager()
        self.ApiManager = ApiManager()
        self.list_categories = ["pizzas", "spread", "snacks", "cheeses", "desserts"]

    def main(self):
        User_enter_1 = int(input("1. Quel aliment souhaitez-vous remplacer ?, 2. Mes aliments substitués >> "))
        self.manage_first_entry(User_enter_1)

        User_enter_2 = int(input("Sélectionnez votre catégorie >> "))
        category = self.manage_second_entry(User_enter_2)

        User_enter_3 = int(input("Sélectionnez votre produit >> "))
        self.manage_third_entry(User_enter_3, category)

    def insert_products(self):
        list_categories = self.list_categories
        for category in list_categories:
            list_product = self.ApiManager.get_data(category)
            self.DatabaseManager.put_products(list_product)

    def manage_first_entry(self, user_enter):
        if user_enter == 1:
            list_categories = self.list_categories
            for nbs,category in enumerate(list_categories):
                print(str(nbs) + " : " + category)

    def manage_second_entry(self, user_enter):
        list_categories = self.list_categories
        for nbs,categories in enumerate(list_categories):
            if user_enter == nbs:
                list_tuple_products = self.DatabaseManager.get_products("product_name", "category", categories)
                for nubs,food in enumerate(list_tuple_products):
                    (nutrient,) = food
                    print(str(nubs) + " : " + nutrient)
                    category = categories
        return category

    def manage_third_entry(self, user_enter, category):
        if user_enter > 0:
            list_substitute = self.DatabaseManager.get_better_products(category)
            for numbs, substitute in enumerate(list_substitute):
                (id, nutrient_grade, name, link, description, stores) = substitute
                print("--------------------------------------------------SUBSTITUTE-----------------------------------------------------\n")
                print(name + " , " + description + " , " + stores + " , " + link + "\n")
                record_user = str(input("Tapez sur enter pour voir un autre produit "+ str(numbs) + "/2 OU seléctionnez s si vous souhaitez enregistrer le produit >> \n"))
                self.record_user_product(record_user, name, id)

    def record_user_product(self, record_user, name_product, id):
        if record_user == "s":
            user_name_enter = str(input("Saisis ton nom >> "))
            list_product_user = (name_product, id)
            self.DatabaseManager.record_user(list_product_user)

    def log_inscription(self, user_enter):
        if user_enter == 2:
            choose_enter = int(input("1. Souhaitez-vous vous inscrire ? , 2. Souhaitez-vous vous connecter ? "))
            if choose_enter == 1:
                #inscrire
            if choose_enter == 2:
                #connect
                #montre aliment 
