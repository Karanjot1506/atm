
from pymongo import MongoClient

# DB connectivity functions
# return client instance of the mongodb
# this client is required to query database
def get_client():
    client = MongoClient('mongodb://root:local@localhost:27017')
    return client


# It is used to connect/select the database
# It accepts client instance of mongodb and name of database
# return database instance
def get_db(client,dbname):
    db = client[dbname]
    return db

def get_collection(db,collection_name):
    collection = db[collection_name]
    return collection

#crud functions

def insert_one(collection,data):
    inserted_id=collection.insert_one(data).inserted_id
    return inserted_id


def insert_many(collection,data):
    inserted_ids=collection.insert_many(data).inserted_ids
    return inserted_ids


def find_one(collection,filter,projection):
    if len(projection) > 0:
        record = collection.find_one(filter, projection)
    else:
        record = collection.find_one(filter)

    return record


def find_many(collection,filter,projection):
    if len(projection) >0:
        records = collection.find(filter,projection)
    else:
        records = collection.find(filter)
    return records


def delete_one(collection,filter):
    deleted_count=collection.delete_one(filter).deleted_count
    return deleted_count


def delete_many(collection,filter):
    deleted_count = collection.delete_many(filter).deleted_count
    return deleted_count


def update_one(collection,filter,data):
    result=collection.update_one(filter,{'$set':data})
    return [result.matched_count,result.modified_count]


def update_many(collection,filter,data):
    result = collection.update_many(filter,{'$set':data})
    return [result.matched_count,result.modified_count]


# This function returns dummy data
def defaultAccounts():
    customers = []
    customers.append({"account_number": 100, "balance": 1000, "pincode": 123, "transactions": []})
    customers.append({"account_number": 101, "balance": 2000, "pincode": 123, "transactions": []})
    customers.append({"account_number": 102, "balance": 3000, "pincode": 123, "transactions": []})
    customers.append({"account_number": 103, "balance": 4000, "pincode": 123, "transactions": []})
    customers.append({"account_number": 104, "balance": 5000, "pincode": 123, "transactions": []})
    return customers


# Populates collection with dummy records if no document exists in the collection
def setup(collection):
    # Fetch first document in the collection
    document = find_one(collection,{},{})
    if document==None:
        # If no document found then insert dummy data to the collection
        data= defaultAccounts()
        insert_many(collection,data)


def checkLogin(collection,account_number,pincode):
    filter={'account_number':int(account_number),'pincode':int(pincode)}
    # Fetch matching document in the  collection
    document = find_one(collection, filter,{})
    return document

def mainMenu(collection,customer):
    choice=0
    while choice != 4:
        print('''
        Choose an option:
        1. Check Balance
        2. Withdraw
        3. Fast Withdraw
        4. Exit
        ''')
        choice = int(input(""))
        if choice == 1:
            checkBalance(customer)
        elif choice == 2:
            withdraw(collection,customer)
        elif choice == 3:
            fastWithdrawMenu(collection,customer)
        elif choice == 4:
            print("Thanks for using the program.")
            break
        else:
            print("Invalid choice")



def fastWithdrawMenu(collection,customer):
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
            transaction(collection, customer, 100)
        elif choice == 2:
            transaction(collection, customer, 500)
        elif choice == 3:
            transaction(collection, customer, 1000)
        elif choice == 4:
            pass
        else:
            print("Invalid choice")


def checkBalance(customer):
    print("Your account balance = ",customer['balance'])

def withdraw(collection,customer):
    amount = int(input("Enter amount to withdraw"))
    transaction(collection, customer, amount)

def logTransaction():
    pass



def transaction(collection,customer,amount):
    balance = int(customer['balance'])
    if balance <= 0:
        print("insuffecient balance:")
    elif balance < amount:
        print("enter amount less than balance")
    elif amount != 100 == 0:
        print("enter amount multiple of 100")
    else:
        filter={'account_number':customer['account_number']}
        update_one(collection,filter,{'balance':balance - amount})
        customer=find_one(collection,filter,{})
        checkBalance(customer)


db_name="atm"
collection_name="customers"
client=get_client()
db=get_db(client,db_name)
collection=get_collection(db,collection_name)

setup(collection)


account_number = input("Enter account number: ")
pincode = input("Enter pincode: ")
customer=checkLogin(collection,account_number,pincode)
print(customer)
if customer == None:
    print("Invalid account")
else:
    mainMenu(collection,customer)