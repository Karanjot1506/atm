from pymongo import MongoClient

# DB connectivity functions
class DBHelper:
    # setters
    def set_dbuser(self,username):
        self.db_user =username

    def set_dbpassword(self,password):
        self.db_password =password

    def set_dbserver(self,server):
        self.db_server =server

    def set_dbport(self,port):
        self.db_port =port

    def __init__(self):
        # No default attribute is set while object creation
        self.db_port ="121"
        self.db_server = "localhost"
        self.db_user = "root"
        self.set_dbpassword("local")

    # this client is required to query database
    def get_client(self):
        self.client = MongoClient('mongodb://'+self.db_user+':'+self.db_password+'@'+self.db_server+':'+self.db_port)
        return self.client


    # It is used to connect/select the database
    # It accepts client instance of mongodb and name of database
    # return database instance
    def get_db(self,dbname):
        self.db = self.client[dbname]
        return self.db

    def get_collection(self,collection_name):
        self.collection = self.db[collection_name]
        return self.collection

    #crud functions

    def insert_one(self,data):
        inserted_id=self.collection.insert_one(data).inserted_id
        return inserted_id


    def insert_many(self,data):
        inserted_ids=self.collection.insert_many(data).inserted_ids
        return inserted_ids


    def find_one(self,filter,projection):
        if len(projection) > 0:
            record = self.collection.find_one(filter, projection)
        else:
            record = self.collection.find_one(filter)

        return record


    def find_many(self,filter,projection):
        if len(projection) >0:
            records = self.collection.find(filter,projection)
        else:
            records = self.collection.find(filter)
        return records


    def delete_one(self,filter):
        deleted_count=self.collection.delete_one(filter).deleted_count
        return deleted_count


    def delete_many(self,filter):
        deleted_count = self.collection.delete_many(filter).deleted_count
        return deleted_count


    def update_one(self,filter,data):
        result=self.collection.update_one(filter,{'$set':data})
        return [result.matched_count,result.modified_count]


    def update_many(self,filter,data):
        result = self.collection.update_many(filter,{'$set':data})
        return [result.matched_count,result.modified_count]


# Customer class represents a customer entity in the bank
class Customer:
    collection_name = "customers"

    def __init__(self, account_number, pincode, balance,dbhelper):
        self.account_number = int(account_number)
        self.pincode = int(pincode)
        self.balance = balance
        self.withdrawls = []
        self.dbhelper=dbhelper
        self.collection=self.dbhelper.get_collection(self.collection_name)
        #print(self.collection)

    def check_balance(self):
        print("Balance: ", self.balance)

    def transaction(self, amount):
        balance = self.balance
        if balance <= 0:
            print("insuffecient balance:")
        elif balance < amount:
            print("enter amount less than balance")
        elif amount != 100 == 0:
            print("enter amount multiple of 100")
        else:
            self.balance -= amount
            filter = {'account_number': self.account_number}
            self.dbhelper.update_one(filter, {'balance': self.balance})
            self.withdrawls.append({"withdrawal_amt": amount, "Balance": self.balance})


        self.check_balance()

    def withdraw(self):
        amount = int(input("Enter amount to withdraw"))
        self.transaction(amount)

    def fast_withdraw(self):
        choice = 0
        while choice != 4:
            print('''
                Choose an option:
                1. 100
                2. 500
                3. 1000
                4. Exit
                ''')
            choice = int(input(""))
            if choice == 1:
                self.transaction(100)
            elif choice == 2:
                self.transaction(500)
            elif choice == 3:
                self.transaction(1000)
            elif choice == 4:
                pass
            else:
                print("Invalid choice")

    def view_transactions(self):
        print(self.withdrawls)

    def mainMenu(self):
        choice = 0
        while choice != 5:
            print('''
            Choose an option:
            1. Check Balance
            2. Withdraw
            3. Fast Withdraw
            4. Transactions

            5. Exit
            ''')
            choice = int(input(""))
            if choice == 1:
                self.check_balance()
            elif choice == 2:
                self.withdraw()
            elif choice == 3:
                self.fast_withdraw()
            elif choice == 4:
                self.view_transactions()
            elif choice == 5:
                print("Thanks for using the program.")
                break
            else:
                print("Invalid choice")

    def check_login(self):
        filter = {'account_number': self.account_number, 'pincode': self.pincode}
        # Fetch matching document in the  collection
        document = self.dbhelper.find_one(filter, {})
        if document is not None:
            # if record exists
            self.balance=document['balance']
        return document is not None

db = DBHelper()
db.set_dbuser("root")
db.set_dbpassword("local")
db.set_dbserver("localhost")
db.set_dbport("27017")
db.get_client()
db.get_db("atm")

account_number = input("Enter account number: ")
pincode = input("Enter pincode: ")
c = Customer(account_number,pincode,0,db)
success_status=c.check_login()
print(success_status)
if success_status == False:
    print("Invalid account")
else:
    c.mainMenu()


