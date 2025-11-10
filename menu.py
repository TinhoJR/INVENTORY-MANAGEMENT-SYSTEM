from user import User,USER_DATA_FILE
from product import Product,PRODUCT_FILE
from transaction import Transaction,SALES_FILE
from utils import generate_id

class Menu:

    def run(self):
        "INITIATE TRANSACTION CLASS"
        transaction_instance = Transaction(SALES_FILE)
        while True:
            # VALIDATE USER ENTRY
            try:
               user_choice = int(input("""\nWELCOME TO CHETA"S INVENTORY SYSTEM

                CHOOSE OPTION TO PERFORM TASK
                OPTION 1: CREATE ACCOUNT
                OPTION 2: LOGIN
                
                    ENTER OPTION: """))
               
            except ValueError:
               print("INVALID ENTRY RETRY!")
               continue   
            
            # ASK FOR INFO FOR USER CLASS AND CLASS CREATE ACCOUNT METHOD
            if user_choice == 1:
               username = input("ENTER USER NAME: ")
               password = input("ENTER PASSWORD: ")
               role = input("CHOOSE ROLE 'admin' or 'guest': ").lower()
               # VALIDATE ROLE ENTRY,GENERATE UNIQUE ID FOR USER
               while role not in ["admin", "guest"]:
                   print("INVALID ROLE CHOOSE 'admin' or 'guest'")
                   role = input("CHOOSE ROLE 'admin' or 'guest': ").lower()
               user_id = generate_id("U",USER_DATA_FILE)
               user = User(username,password,role,user_id)
               user.create_account()

            elif user_choice == 2:
               # CALL LOGIN CLASSMETHOD, HOLD THE USER LOGGED IN
               user_logged_in = User.login()
               print("\nHELLO {}".format(user_logged_in.username.upper()))
               # CHECK USER ROLE FOR UNIQUE VIEWS AND PERFORMANCE,CALL METHOD BASED ON USER ROLE
               if user_logged_in.role == "admin":
                   self.admin_menu(transaction_instance,user_logged_in)
               elif user_logged_in.role == "guest":
                   self.guest_menu(transaction_instance,user_logged_in)

            else:
                print("INVALID ENTRY")

    def guest_menu(self,transaction_inst,user_logged_in):
        while True:
            # DISPLAY GUEST OPTION AND VALIDATE GUEST ENTRY,CALL RESPECTIVE NETHOD BASED ON USER ENTRY
            try:
                guest_option = int(input("""\nWELCOME GUEST
                ENTER OPTION TO PERFORM TASKS
                OPTION 1: DISPLAY PRODUCTS
                OPTION 2: MAKE SALE
                OPTION 3: VIEW ALL RECEIPTS
                OPTION 4: CHANGE PASSWORD
                OPTION 5: LOGOUT
                                    
                    CHOOSE OPTION:  """))
            except:
                print("INVALID ENTRY RETRY!")
                continue

            if guest_option == 1:
                Product.display_product() 

            elif guest_option == 2:
                Product.make_sale(transaction_inst,user_logged_in)

            elif guest_option == 3:
                transaction_inst.print_receipt(user_logged_in)

            elif guest_option == 4:
                user_logged_in.change_password()

            elif guest_option == 5:
                print("LOGGED OUT..") 
                break                        

    def admin_menu(self,transaction_inst,user_logged_in):
        while True:
            # DISPLAY ADMIN OPTION AND VALIDATE ADMIN ENTRY,CALL RESPECTIVE NETHOD BASED ON USER ENTRY
            try:  
                admin_option = int(input("""\nWELCOME ADMIN
                ENTER OPTION TO PERFORM TASKS
                OPTION 1: ADD PRODUCT
                OPTION 2: DISPLAY PRODUCTS
                OPTION 3: MAKE SALE
                OPTION 4: TRANSACTION SUMMARY
                OPTION 5: CHANGE PASSWORD
                OPTION 6: LOGOUT
                                    
                    CHOOSE OPTION:  """))
            except:
                print("INVALID ENTRY RETRY!")
                continue
            if admin_option == 1:
                # ASK FOR PRODUCT DETAIL,VALIDATE ENTRY,CALL NEEDED METHOD
                product_name = input("ENTER PRODUCT NAME: ")
                product_id = generate_id("P",PRODUCT_FILE)
                try:
                    product_price = int(input("ENTER PRICE: "))
                    product_qty = int(input("ENTER PRODUCT QTY: ")) 

                except ValueError:
                    print("INVALID ENTRY RETRY!")
                    continue
                # USE PROVIDED PRODUCT DETAIL TO CREATE USER INSTANCE AND CALL ADD PRODUCT TO SAVE TO FILE
                product = Product(product_name,product_price,product_qty,product_id)
                product.add_product() 

            elif admin_option == 2:
                Product.display_product()

            elif admin_option == 3:
                Product.make_sale(transaction_inst,user_logged_in)

            elif admin_option == 4:
                transaction_inst.transaction_summary()

            elif admin_option == 5:
                user_logged_in.change_password()    

            elif admin_option == 6:
                print("LOGGED OUT..") 
                break                                
   