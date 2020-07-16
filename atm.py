
customers = {}
customers.update({100:{"account_number":100,"balance":1000,"pincode":123,"transactions":[]}})
customers.update({101:{"account_number":101,"balance":2000,"pincode":123,"transactions":[]}})
customers.update({102:{"account_number":102,"balance":3000,"pincode":123,"transactions":[]}})
customers.update({103:{"account_number":103,"balance":4000,"pincode":123,"transactions":[]}})
customers.update({104:{"account_number":104,"balance":5000,"pincode":123,"transactions":[]}})


while True:
    print("do you want to end the program(y/n)")
    choice = input("")
    if choice.lower() not in ['y','n']:
        print("Invalid choice")
        continue
    if choice.lower() == 'y':
        break

    acc = int(input("account_number"))
    if acc in customers:
        customer = customers[acc]
        print(customer)
        pin = int(input("pincode :"))
        if (pin == customers[acc]["pincode"]):
            print("login successful")
            c=0
            while c != 4:
                print("enter 1 for balance")
                print("enter 2 for quick withdrawal ")
                print("enter 3 for withdrawal")
                print("enter 4 to exit the program")
                c = int(input("enter the number :"))
                if(c==4):
                    print(customers[acc])
                    print("Thanks!")
                    break
                if (c == 1):
                    print("balance :", customers[acc]["balance"])
                elif (c == 2):
                    print("1 : 500")
                    print("2 : 1000")
                    print("3 : 2000")
                    print("4 : 5000")

                    d = int(input("enter the number:"))
                    if (d == 1):
                        customers[acc]["balance"] = withdraw(customers[acc]["transactions"],customers[acc]["balance"], 500)

                    elif (d == 2):
                        customers[acc]["balance"] = withdraw(customers[acc]["transactions"],customers[acc]["balance"], 1000)

                    elif (d == 3):
                        customers[acc]["balance"] = withdraw(customers[acc]["transactions"],customers[acc]["balance"], 2000)

                    elif (d == 4):
                        customers[acc]["balance"] = withdraw(customers[acc]["transactions"],customers[acc]["balance"], 5000)

                    elif (d > 4 or d < 1):
                        print("invalid choice")

                elif (c == 3):
                    m = int(input("enter the amount to be withdrawn : "))
                    customers[acc]["balance"] = withdraw(customers[acc]["transactions"],customers[acc]["balance"], m)
            continue
        else:
            print("incorrect pin.try again")

    else:
        print("Account does not exists")