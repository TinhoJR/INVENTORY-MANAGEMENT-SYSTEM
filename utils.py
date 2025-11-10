
import json
import random

def generate_id(prefix,file):  
    with open(file) as product:
            data = json.load(product)        
    # GENERATE 4 UNIQUE ID FOR EACH PRODUCT AND CHECK FOR DUPLICATE
    while True:
        product_unique_id = f"{prefix}{random.randint(1000, 9999)}"

        if product_unique_id not in data.keys():
            return product_unique_id  