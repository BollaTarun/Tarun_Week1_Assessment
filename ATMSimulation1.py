
# Provides the options to the user
def options():
    amount=0
    print("\t\t ATM MACHINE")
    print("Enter 1 to Check Balance")
    print("Enter 2 to Deposit Money")
    print("Enter 3 to Withdraw Money")
    print("Enter 4 to Exit")
    while True:
        N=int(input("Enter your choice: \n"))
        if(N>4):
            print("Enter Valid Choice!!!")
        elif N==1:
            check_balance(amount)
        elif N==2:
            amount+=deposit()
        elif N==3:
            amount=withdraw(amount)
        else:
            print("Thank You for your trust!")
            return
        
# Prints the amount balanace based on availability
def check_balance(amount):
    if amount==0:
        print("Your Bank Balance is NILL!!")
    else:
        print(f"Your Bank Balance is Rs.{amount} rupees.")

# Adds the deposit money to amount in account
def deposit():
    while True:
        deposit=float(input("Enter the amount you want to deposit:\n"))
        if deposit<=0:
            print("Enter a Valid Amount!!")
        else:
            print("DEPOSIED SUCCESSFULLY!!!")
            return deposit

# Withdrawal of money is done based on available balance.
def withdraw(amount):
    if amount==0:
        print("Your Bank Balance is NILL.\nNo amount can be withdrawn.")
        return 0
    while True:
        withdraw=float(input("Enter the amount you want to withdraw:\n"))
        if withdraw<=0:
            print("Enter a Valid Amount")
        else:
            break
    if withdraw<amount:
        amount-=withdraw
        print(f"Your amount of Rs.{withdraw} is withdrawed.")
        return amount
    else:
        print("WITHDRAWAL UNSUCCESSFUL!\n Your bank amount doesn't have that much money.")
        return amount

def main():
    options()
main()