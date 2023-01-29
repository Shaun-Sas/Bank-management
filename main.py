import time

class Bank:
    def __init__(self):
        self.balance = 0

    def enquiry(self):
        print("Balance in the account is %f \n" % self.balance)


    def deposit(self):
        amount = float(input("Enter an amount you want to deposit"))
        self.balance = self.balance + amount
        current = print("The total balance is :%f  \n" % self.balance)
        return


    def withdraw(self):
        amount = float(input("Enter an amount to be withdrawn"))
        if amount < self.balance:
            self.balance = self.balance - amount
            print("The balance left is %f \n" % self.balance)
            return
        else:
            print("Balance nahi hai tere pass Gareeb")


    def menu(self):
        print("###############menu###################")
        self.user=input("Enter your name ")
        self.pin = input ("enter the pin please")
        print("Processing",end="")
        for i in range(6):
            time.sleep(1)
            print("." ,end="")
        run()







def run():
    print("\n 1:Check the balance of the account")
    print("2:Deposit an amount to the account")
    print("3.Withdraw an amount from the account  ")
    print("4:Exit \n")
    num = (input("Enter a value "))
    if num == "1":
        acc.enquiry()
        run()
    elif num == "2":
        acc.deposit()
        run()
    elif num == "3":
        acc.withdraw()
        run()
    else:
         exit()


acc = Bank()
acc.menu()




