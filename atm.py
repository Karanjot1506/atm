# Step 1: Define user account

user = [{"username":"karan","pincode": "123", "balance":1000},
        {"username":"mankiran","pincode": "123", "balance":1000}
        ]

username = input("Enter username: ").strip()
pincode = input("Enter pincode: ").strip()
found=-1
for i in range(len(user)):
    # print("Testing user ",i)
    if user[i]["username"] == username and user[i]["pincode"] == pincode:
        found = i
        break

if found ==-1:
    print("Invalid details")
else:
    print("Welcome "+user[i]["username"])
