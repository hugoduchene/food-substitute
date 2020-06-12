import mysql.connector

class DatabaseManager:
    """relation with Database."""

    def __init__(self):
        self.mydb = False
        self.mycursor = False
        self.connect_database()

    def connect_database(self):
        """ Method for connecting to a database """
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="food_substitue_bdd"
        )

        self.mycursor = self.mydb.cursor()

    def get_products(self, column, place_table, result_table):
        """ Method of taking products according to their parameter """

        request_sql = "SELECT " + column +" FROM products WHERE "+ place_table +" = '" + result_table + "'"
        self.mycursor.execute(request_sql)
        myresult = self.mycursor.fetchall()
        return myresult

    def get_id_products_record(self, id_user):
        """ Method for taking the id of registered products """
        request_sql = "SELECT id_product FROM product_id WHERE id_user = "+ id_user
        self.mycursor.execute(request_sql)
        myresult = self.mycursor.fetchall()
        return myresult

    def get_products_record(self, id_product):
        """ Method for taking registered products """
        request_sql = "SELECT product_name, stores, link FROM products WHERE id = "+ id_product
        self.mycursor.execute(request_sql)
        myresult = self.mycursor.fetchall()
        return myresult

    def put_products(self, list_product):
        """ Method for inserting products  """
        request_sql = "INSERT IGNORE INTO products (category, product_name, ingredients_text, nutrition_grade, stores, brands, link) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        self.mycursor.executemany(request_sql, list_product)
        self.mydb.commit()

    def get_better_products(self, category):
        """ Method for taking the best products  """
        request_sql = "SELECT id, nutrition_grade, product_name, link, ingredients_text, stores FROM products WHERE category = '"+category+"' ORDER BY nutrition_grade LIMIT 0,3"
        self.mycursor.execute(request_sql)
        list_result = self.mycursor.fetchall()
        return list_result

    def record_user(self, list_user):
        """ Method for inserting user records """
        request_sql = "INSERT INTO product_id (id_user, id_product) VALUES (%s , %s)"
        self.mycursor.execute(request_sql, list_user)
        self.mydb.commit()

    def register_user(self, list_infos):
        """ Method for inserting users upon registration """
        request_sql = "INSERT INTO user (pseudo, password, mail) VALUES (%s, %s, %s)"
        self.mycursor.execute(request_sql, list_infos)
        self.mydb.commit

    def connect_user(self, pseudo, password):
        """ Method for registering users """
        id = -1
        var = False
        request_sql = "SELECT id, pseudo, password FROM user WHERE password = '"+password+"' AND pseudo = '"+pseudo+"'"
        self.mycursor.execute(request_sql)
        tuple_connect = self.mycursor.fetchall()
        id = tuple_connect[0][0]

        if tuple_connect == [(id, pseudo, password)]:
            var = True
        elif tuple_connect == []:
            var = False

        return (var, id)
