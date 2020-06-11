import mysql.connector

class DatabaseManager:
    """docstring forDatabaseManager."""

    def __init__(self):

        self.mydb = False
        self.mycursor = False

    def connect_database(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="food_substitue_bdd"
        )

        self.mycursor = self.mydb.cursor()

    def get_products(self, column, place_table, result_table):
        self.connect_database()
        request_sql = "SELECT " + column +" FROM products WHERE "+ place_table +" = " + result_table
        self.mycursor.execute(request_sql)

        myresult = self.mycursor.fetchall()
        return myresult

    def put_products(self, list_product):
        self.connect_database()
        request_sql = "INSERT IGNORE INTO products (category, product_name, ingredients_text, nutrition_grade, stores, brands, link) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        self.mycursor.executemany(request_sql, list_product)
        self.mydb.commit()
