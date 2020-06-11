import mysql.connector

class DatabaseManager:
    """docstring forDatabaseManager."""

    def __init__(self):
        self.mydb = False
        self.mycursor = False
        self.connect_database()

    def connect_database(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="food_substitue_bdd"
        )

        self.mycursor = self.mydb.cursor()

    def get_products(self, column, place_table, result_table):

        request_sql = "SELECT " + column +" FROM products WHERE "+ place_table +" = '" + result_table + "'"
        self.mycursor.execute(request_sql)
        myresult = self.mycursor.fetchall()
        return myresult

    def put_products(self, list_product):
        request_sql = "INSERT IGNORE INTO products (category, product_name, ingredients_text, nutrition_grade, stores, brands, link) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        self.mycursor.executemany(request_sql, list_product)
        self.mydb.commit()

    def get_better_products(self, category):
        request_sql = "SELECT id, nutrition_grade, product_name, link, ingredients_text, stores FROM products WHERE category = '"+category+"' ORDER BY nutrition_grade LIMIT 0,3"
        self.mycursor.execute(request_sql)
        list_result = self.mycursor.fetchall()
        return list_result

    def record_user(self, list_user):
        request_sql = "INSERT IGNORE INTO user_record (name, product_id) VALUES (%s , %s)"
        self.mycursor.executemany(request_sql, list_user)
        self.mydb.commit()
