import json,os
import datetime
 
USER_DATA_FILE = "C:/Users/ELITEBOOK 840 G5/Desktop/CODING/BACKEND/PERSONAL-TESTS/PROJECTS/INVENTORY-SYSTEM/DATA/user_data_file.json"

class User:
    def __init__(self,username,password,role,user_id):
        self.username = username
        self.password = password
        self.role = role
        self.user_id = user_id
        
    def create_account(self):
        "CHECK IF THE FILE EXISTS"
        if os.path.exists(USER_DATA_FILE):
            # IF IT EXISTS LOAD ALL FILE TO USERDETAILS
            with open(USER_DATA_FILE) as all_user_data:
                user_details = json.load(all_user_data)

        else:
            # IF NOT, CREATE NEW DICTIONARY
            user_details = {}  

        # SAVE USER DETAILS, ID AS KEY OTHER INFOS AS VALUE
        creation_date = datetime.datetime.now().isoformat()
        user_details[self.user_id] = {
                "username"   : self.username,
                "password"   : self.password,
                "role"       : self.role,
                "created on" : creation_date
            }
        # SAVE USER DETAILS TO FILES,NEW OR EXISTING
        with open(USER_DATA_FILE, "w") as user_data:
            json.dump(user_details,user_data,indent=4)

        print("ACCOUNT CREATED SUCCESSFULLY!")    
    
    @classmethod
    def login(cls):
        "LOAD ALL DATA FROM FILE"
        with open(USER_DATA_FILE) as user_data:
            data = json.load(user_data)

        while True:
            # ASK USER FOR USERNAME
            login_username = input("ENTER YOUR USERNAME: ")  
            username_found = False
            # RUN A LOOP TO CHECK IF THE USERNAME MATCHES ANY IN DATABASE,TURN USERNAME_FOUND TO TRUE IF IT MATCHES 
            for user_id, user_info in data.items(): 
                if login_username == user_info["username"]:
                    username_found = True
                    login_password = input("ENTER PASSWORD: ") # ASK FOR PASSWORD AND CHECK IF IT MATCHES 
                    if login_password == user_info["password"]:
                        print("LOGIN SUCCESSFUL") # GRANT ACCESS IF PASSWORD MATCHES
                        # USE USER INFO TO CREATE A USER INSTANCE AND RETURN IT FOR FUTURE PURPOSES
                        current_user = cls(user_info["username"],user_info["password"],user_info["role"],user_id)
                        return current_user 

                    else:
                        print("INCORRECT PASSWORD RETRY!")
            
            if username_found is False:
                print("NO USERNAME MATCHES RETRY!")

    def change_password(self):
        with open(USER_DATA_FILE) as user_data:
                data = json.load(user_data)
        "ASK USER FOR CURRENT PASSWORD"
        current_password = input("CONFIRM OLD PASSWORD: ") 
        # CHECK IF CURRENT PASSWORD MATCHES
        if current_password == self.password:
            new_password = input("ENTER NEW PASSWORD: ") # ASK FOR NEW PASSWORD AND UPDATE OLD PASSWORD TO NEW PASSWORD
            self.password = new_password
            data[self.user_id]["password"] = new_password # UPDATE THE NEW PASSWORD TO FILE, SAVE THE UPDATED PASSWORD TO FILE
            
            with open(USER_DATA_FILE, "w") as user_data:
                json.dump(data,user_data,indent=4)

            print("PASSWORD UPDATED SUCCESSFULLY!") 

        else:
            print("INCORRECT PASSWORD RETRY!")       

