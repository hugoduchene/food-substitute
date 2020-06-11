import json
import urllib.request

class ApiManager:
    """docstring fs ApiManager."""

    def __init__(self):
        self.list_product = []

    def load_json(self, category):
        url = "https://fr.openfoodfacts.org/category/"+ category + ".json"
        response = urllib.request.urlopen(url)
        data = json.loads(response.read())

        return data

    def get_data(self, category):
        data = self.load_json(category)

        for dictionary in data["products"]:
            product = dictionary.get("product_name_fr","")
            stores = dictionary.get("stores", "")
            description = dictionary.get("ingredients_text_fr", "")
            score = dictionary.get("nutrition_grades", "")
            brand = dictionary.get("brands", "")
            link = dictionary.get("url", "")

            tuple_product = (category, product, description, score, stores, brand, link)

            self.list_product.append(tuple_product)
        return self.list_product
