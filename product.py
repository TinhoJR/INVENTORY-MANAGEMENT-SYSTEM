import json,os
import datetime

PRODUCT_FILE = "C:/Users/ELITEBOOK 840 G5/Desktop/CODING/BACKEND/PERSONAL-TESTS/PROJECTS/INVENTORY-SYSTEM/DATA/products_file.json"

class Product:
    def __init__(self,name,price,qty,product_id):
        self.name = name
        self.price = price
        self.qty = qty
        self.product_id = product_id

    def add_product(self):
        creation_date = datetime.datetime.now().isoformat()
        "CHECK IF FILE EXISTS AND LOAD IT UP IF NOT,CREATE A NEW DICTIONARY"
        if os.path.exists(PRODUCT_FILE):
            with open(PRODUCT_FILE) as product:
                product_data = json.load(product)
        else:
            product_data = {}
        # CHECK IF PRODUCT EXIST,INCREASE QTY IF THE PRODUCT(NAME) EXISTS
        for product_id, product_info in product_data.items():
            if self.name.lower() == product_info["name"].lower():
                product_info["qty"] += self.qty
                print("PRODUCTS ALREADY EXISTS INCREASING QTY")
                break
        else:
            # SAVE NEW PRODUCT TO FILE,PRODUCT_ID AS KEY,WITH ALL NEEDED INFO AS VALUE
            product_data[self.product_id] = {
                "name"     : self.name,
                "price"    : self.price,
                "qty"      : self.qty,
                "added on" : creation_date
            }
            print("PRODUCT SUCCESSFULLY ADDED")

        with open(PRODUCT_FILE,"w") as product:
            json.dump(product_data,product,indent=4)  

    @classmethod
    def display_product(cls):
        "CHECK IF FILE EXISTS AND LOAD IT UP"
        if os.path.exists(PRODUCT_FILE):
            with open(PRODUCT_FILE) as product:
                product_data = json.load(product)
        else:
            print("NO AVAILABLE PRODUCT")

        # LOOP THROUGH THE LOADED FILE AND DISPLAY ALL PRODUCT IN A NEAT FORMAT
        print("\nID       | Name         | Price    | Qty   | Added On")
        for product_id, product_info in product_data.items():
            print("\n{:<8} | {:<12} | {:<8} | {:<5} | {:<20}".format(
            product_id,
            product_info["name"],
            product_info["price"],
            product_info["qty"],
            product_info["added on"]
            ))

    @classmethod
    def make_sale(cls,transaction_instance,user_logged_in):
        "LOAD ALL PRODUCT FROM FILE AND CHECK IF THE FILE EXISTS"
        if os.path.exists(PRODUCT_FILE):
            with open(PRODUCT_FILE) as product_file:
                product_data = json.load(product_file)
        else:
            print("NO AVAILABLE PRODUCT")
            return
        # DISPLAY ALL AVAILABLE PRODUCTS AND ASK USER CHOOSE PRODUCT TO BUY/SELL
        cls.display_product()
        user_product_name = input("ENTER PRODUCT NAME YOU WANT TO BUY/SELL: ")
        product_found = False
        creation_date = datetime.datetime.now().isoformat()
        # LOOP THROUGH THE PRODUCT, CHECK IF THE PRODUCT EXISTS IN FILE
        for product_id, product_info in product_data.items():
            if user_product_name.lower() == product_info["name"].lower():
                product_found = True

                # ASK FOR QTY IN A LOOP UNTIL ITS VALID
                while True:
                    try:
                        user_product_qty = int(input("ENTER QUANTITY: "))
                    except ValueError:
                        print("INVALID QTY ENTERED")
                        continue
                    # CHECK IF REQUESTED QTY CORRESPONDS WITH AVALAIBLE PRODUCT QTY
                    if user_product_qty > product_info["qty"]:
                        print("NO ENOUGH STOCK") 

                    else:
                        break # VALID QTY ENTERED        
                # CALCULATE TOTAL PRICE OF QTY, CALL NEEDED METHODS AND PRINT SUCCESSFUL SALE
                total_price = user_product_qty * product_info["price"]
                cls.update_quantity(product_id,user_product_qty)
                sale_data = {
                    "product_id" : product_id,
                    "product_name" : product_info["name"],
                    "quantity_sold" : user_product_qty,
                    "total_price"  : total_price,
                    "sold_by_name" :  user_logged_in.username, # TO RECORD WHO MADE THE SALE
                    "sold_by_id" : user_logged_in.user_id,
                    "date"   : creation_date
                }
                # HANDING OFF SALES RECORD WITH NEEDED IN TO TRANSACTION CLASS FOR RECORDING
                transaction_instance.record_sale(sale_data)

                print("SALE SUCCESSFUL")
                return

        if not product_found:
            print("NO PRODUCT MATCHES RETRY!")

    @classmethod
    def update_quantity(cls,product_id,user_product_qty):
        with open(PRODUCT_FILE) as product_file:
            product_data = json.load(product_file)

        # REDUCE PRODUCT QTY BY USER REQUESTED QTY AND SAVE BACK TO FILE
        product_data[product_id]["qty"] -= user_product_qty

        # ALERT WHEN PRODUCT QTY IS LESS OR EQUAL TO 5
        if product_data[product_id]["qty"]  <= 5:
            print("LOW PRODUCT STUCK")

        with open(PRODUCT_FILE, "w") as product_file:
            json.dump(product_data,product_file,indent=4)

            
                
