from myapp.models.database_manager import DatabaseManager
from myapp.models.api_manager import ApiManager


class Application:
    """ Object that will manage the classes of models and views """
    def __init__(self):
        """class initialization"""
        self.DatabaseManager = DatabaseManager()
        self.ApiManager = ApiManager()
        self.list_categories = ["pizzas", "spread", "snacks", "cheeses", "desserts"]
        self.id_user = -1

    def main(self):
        """ application main class """
        var = True

        while var:
            Connect_enter = int(input("1. Souhaitez-vous vous inscrire ? , 2. Souhaitez-vous vous connecter ? "))
            if Connect_enter in [1,2]:
                var = self.registration(Connect_enter)
                var = self.log(Connect_enter)
            else:
                print("veuillez entrer le bon nombre")
                var = True

        if not var:
            var = True

            while var:
                User_enter_1 = int(input("1. Quel aliment souhaitez-vous remplacer ?, 2. Mes aliments substitués >> "))
                if User_enter_1 in [1,2]:
                    var = self.display_category(User_enter_1)
                    var = self.manage_products_user(User_enter_1)
                else:
                    print("Veuillez entrer le bon nombre")
                    var = True

            if not var:

                User_enter_2 = int(input("Sélectionnez votre catégorie >> "))
                category = self.manage_second_entry(User_enter_2)

                User_enter_3 = int(input("Sélectionnez votre produit >> "))
                self.manage_third_entry(User_enter_3, category)

    def insert_products(self):
        """ Method for inserting products into the database. """
        list_categories = self.list_categories
        for category in list_categories:
            list_product = self.ApiManager.get_data(category)
            self.DatabaseManager.put_products(list_product)

    def display_category(self, user_enter):
        """ Method for displaying categories """
        if user_enter == 1:
            list_categories = self.list_categories
            for nbs,category in enumerate(list_categories):
                print(str(nbs) + " : " + category)
        return False


    def manage_products_user(self, user_enter):
        """ Method for displaying registered products """
        var_bool_products_user = False
        if user_enter == 2:
            list_id_products_record = self.DatabaseManager.get_id_products_record(self.id_user)
            if list_id_products_record == []:
                print("vous n'avez rien enregistré")
                var_bool_products_user = True
            else:
                for tuple_id_product_record in list_id_products_record:
                    (id_product_record,) = tuple_id_product_record
                    id_product_record = str(id_product_record)
                    [(name, stores, link)] = self.DatabaseManager.get_products_record(id_product_record)
                    print("--------------------Vos éléments enregistrés ------------------------")
                    print(name + " - " + stores + " - " + link + "\n")
                    var_bool_products_user = True
        return var_bool_products_user




    def manage_second_entry(self, user_enter):
        """ Method for displaying the products of the chosen category """
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
        """ Method for displaying and saving the best products """
        if user_enter > 0:
            list_substitute = self.DatabaseManager.get_better_products(category)
            for numbs, substitute in enumerate(list_substitute):
                (id, nutrient_grade, name, link, description, stores) = substitute
                print("--------------------------------------------------SUBSTITUTE-----------------------------------------------------\n")
                print(name + " , " + description + " , " + stores + " , " + link + "\n")
                record_user_enter = str(input("Tapez sur enter pour voir un autre produit "+ str(numbs) + "/2 OU seléctionnez s si vous souhaitez enregistrer le produit >> \n"))
                self.record_user_product(record_user_enter, id)

    def record_user_product(self, record_user_enter, id):
        """ Method for registering users' products """
        if record_user_enter == "s":
            list_product_user = (self.id_user, id)
            self.DatabaseManager.record_user(list_product_user)

    def registration(self, user_enter):
        """ Method for registering a user """
        bool_regi = False
        if user_enter == 1:
            pseudo = str(input("Votre pseudo >> "))
            password = str(input("Votre mot de passe >> "))
            mail = str(input("Votre email >> "))
            tuple_infos = (pseudo, password, mail)
            self.DatabaseManager.register_user(tuple_infos)
            bool_regi = False
        return bool_regi


    def log(self, user_enter):
        """ Method for logging in a user """
        var_bool = True
        if user_enter == 2:
            pseudo = str(input("Votre pseudo >> "))
            password = str(input("Votre mot de passe >> "))
            (var_bool_connect ,id) = self.DatabaseManager.connect_user(pseudo, password)
            self.id_user = str(id)


            if var_bool_connect == True:
                var_bool = False
            else:
                var_bool = True
        return var_bool
