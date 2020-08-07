class Customer:

    def __init__(self,name,pincode,balance):
        self.customer_name = name
        self.pincode=pincode
        self.balance=balance
        self.withdrawls= []

    def check_balance(self):
        print("Balance: ",self.balance)

    def transaction(self,amount):
        balance = self.balance
        if balance <= 0:
            print("insuffecient balance:")
        elif balance < amount:
            print("enter amount less than balance")
        elif amount != 100 == 0:
            print("enter amount multiple of 100")
        else:
            self.balance -= amount
            self.withdrawls.append({"withdrawal_amt":amount,"Balance":self.balance})
        self.check_balance()


    def withdraw(self):
        amount = int(input("Enter amount to withdraw"))
        self.transaction( amount)



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
        choice=0
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

c =Customer("Karan","1234",10000)
c.mainMenu()

