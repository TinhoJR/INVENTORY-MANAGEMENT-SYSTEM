import json,os
from utils import generate_id


SALES_FILE = "C:/Users/ELITEBOOK 840 G5/Desktop/CODING/BACKEND/PERSONAL-TESTS/PROJECTS/INVENTORY-SYSTEM/DATA/sales_file.json"

class Transaction:
    def __init__(self,file_path):
        self.file_path = file_path


    def record_sale(self,sale_data):
        "CHECK IF FILE EXISTS AND LOAD IT UP IF NOT,CREATE A NEW DICTIONARY"
        if os.path.exists(SALES_FILE):
            with open(SALES_FILE) as sales_file:
                transaction_data = json.load(sales_file)
        else:
            transaction_data = {}

        # GENERATE UNIQUE ID FOR TRANSACTION, USE TRANSACTION ID AS KEY AND SALE DATA AS VALE AND SAVE TO FIES
        transaction_id = generate_id("T",SALES_FILE) 
        transaction_data[transaction_id] = sale_data

        with open(SALES_FILE,"w") as sales_file:
            json.dump(transaction_data,sales_file,indent=4) 

        return transaction_id # RETURN TRANSACTION ID FOR FUTURE USE
    

    def print_receipt(self,user_logged_in):
        # LOAD USER INTO FILE,CREATE VARIABLES FOR TRACKING 
        with open(SALES_FILE) as sales_file:
            transaction = json.load(sales_file)
        total_amount = 0
        total_items = 0
        id_found = False  # SET TO FALSE UPATE IF ID MATCHES  
        print("""SALES RECEIPT""")
        """LOOP THROUGH TRANSACTION FILE, CHECK IF REGISTERED ID MATCHES USER LOGGED IN ID,IF IT MACTHES PRINT DETAILED RECEIPT -- 
           WITH USER DETAILS """
    
        for transaction_id,transaction_info in transaction.items():
            if transaction_info["sold_by_id"] == user_logged_in.user_id:
                id_found = True
                print("""
                TRANSACTION ID : {}
                DATE : {}
                SOLD BY : {} (ID: {})

                --------------------------------------------------

                PRODUCT NAME  | QTY   | TOTAL
                
                {:<13} | {:<5} | {:<5} 
                    
                """.format(
                    transaction_id,
                    transaction_info["date"],
                    transaction_info["sold_by_name"],
                    transaction_info["sold_by_id"],
                    transaction_info["product_name"],
                    transaction_info["quantity_sold"],
                    transaction_info["total_price"]
                ))
                # UPDATE TOTAL AMOUNT AND ITEMS
                total_amount += transaction_info["total_price"]
                total_items += transaction_info["quantity_sold"]

        if id_found:
            print("""
            TOTAL AMOUNT : {}
            TOTAL ITEM   : {}""".format(total_amount,total_items)) 

        else:
            print("NO SALES FOUNDS") 

    def transaction_summary(self):
        "LOAD SALES FILE INTO MEMORY"
        with open(SALES_FILE) as sales_file:
            transaction = json.load(sales_file)

        total_revenue = 0
        total_items = 0
        num_transaction = 0
        print("GENERATING SUMMARY...")
        # LOOP THROUGH SALES FILE,ADD UP ALL TOTAL ABOUT, ADD UP ALL TOTAL QTY SOLD,INCREMENT NUMBER OF TRANSACTION
        for transaction_id, transaction_info in transaction.items():
            total_revenue += transaction_info["total_price"]
            total_items += transaction_info["quantity_sold"]
            num_transaction += 1

        # DISPLAY SUMMARY 
        print("""
        TOTAL TRANSACTIONS : {}
        TOTAL ITEMS SOLD   : {}
        TOTAL REVENUE      : {}""".format(num_transaction,total_items,total_revenue))    



