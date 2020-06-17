import json
import urllib.request

class ApiManager:
    """relation with the Api."""

    def __init__(self):
        "class initialization"
        self.list_product = []

    def load_json(self, category):
        """ Method for loading the json """
        url = "https://fr.openfoodfacts.org/category/"+ category + ".json"
        response = urllib.request.urlopen(url)
        data = json.loads(response.read())

        return data

    def get_data(self, category, id_category):
        """ Method for taking the data we need from json """
        data = self.load_json(category)

        for dictionary in data["products"]:
            product = dictionary.get("product_name_fr","")
            stores = dictionary.get("stores", "")
            description = dictionary.get("ingredients_text_fr", "")
            score = dictionary.get("nutrition_grades", "")
            brand = dictionary.get("brands", "")
            link = dictionary.get("url", "")

            tuple_product = (id_category, product, description, score, stores, brand, link)
            self.list_product.append(tuple_product)

        return self.list_product
