
from pymongo import MongoClient

def get_client():
    client = MongoClient('mongodb://root:local@localhost:27017')
    return client

def get_db(client,dbname):
    db = client[dbname]
    return db

def get_collection(db,collection_name):
    collection = db[collection_name]
    return collection



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


def menu():
    print("a:add a joke")
    print("v:view list of jokes")
    print("d:delete a joke")
    print("r:review of the jokes")
    print("s:search the joke")
    print("q:quit")
    choice = input("enter choice").strip().lower()
    required_queries=["a","v","d","r","s","q"]
    if choice not in required_queries:
        print("Invalid choice")
        return menu()
    return  choice

def jokes():
    jokes = [
        {"joke": "abcd", "punchline": "lol", "laughs": 1, "groans": 23},
        {"joke": "ha", "punchline": "loll", "laughs": 1, "groans": 23},
        {"joke": "haha", "punchline": "lloll", "laughs": 1, "groans": 23},
        {"joke": "hahah", "punchline": "lolll", "laughs": 1, "groans": 23},
        {"joke": "hahahaha", "punchline": "looool", "laughs": 1, "groans": 23},
    ]
    return jokes


def setup(collection):
    document = find_one(collection,{},{})
    print(document)
    if document == None:
        data= jokes()
        print(data)
        insert_many(collection,data)

def commands(collection):
    while True:
        choice= menu()
        if choice == 'q':
            print("Goodbye!!!")
            break
        elif choice == 'a':
            add_joke(collection)
        elif choice == 'v':
            view_jokes(collection)
        elif choice == 's':
            search_joke(collection)
        elif choice == 'd':
            delete_joke(collection)
        elif choice == 'r':
            review_joke(collection)




def  add_joke(collection):
    x=input("joke:").lower()
    y=input("punchline:").lower()
    added_joke={"joke": x, "punchline": y, "laughs": 0, "groans": 0}
    insert_one(collection,added_joke)

def view_jokes(collection):
    b=find_many(collection,{},{"_id":0,"joke":1,"punchline":1})
    for b in b :
        print(b)
    if b == None:
        print("joke not found")

def delete_joke(collection):
    x = input("joke:").lower()
    y = input("punchline:").lower()
    delete_one(collection,{"joke":x,"punchline":y})

def review_joke(collection):
    x = input("joke:").lower()
    y = input("punchline:").lower()
    m=find_many(collection, {"joke":x,"punchline":y}, {"_id": 0, "laughs": 1, "groans": 1})
    if m == None:
        print("joke not found")
    else :
        print(m)



def search_joke(collection):
    x = input("joke:").lower()
    y = input("punchline:").lower()
    m=find_one(collection,{"joke":{'$regex':x},"punchline":{'$regex':y}},{"_id":0})
    if m == None:
        print("joke not found")
    else :
        print(m)

db_name="jokes"
collection_name="joke"
client=get_client()
db=get_db(client,db_name)
collection=get_collection(db,collection_name)
setup(collection)
commands(collection)