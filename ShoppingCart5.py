

# Provides the options to the user
def options():
    items=[]
    cost=[]
    print("\n\t\t\t\tSHOPPING CART")
    print("Enter 1 to Add Items")
    print("Enter 2 to View Cart Items")
    print("Enter 3 to Check Total Price")
    print("Enter 4 to Exit")
    while True:
        N=int(input("Enter your choice: \n"))
        if(N>4):
            print("Enter Valid Choice!!!")
        elif N==1:
            item_name,rate=add_items()
            items.append(item_name)
            cost.append(rate)
        elif N==2:
            view_items(items,cost)
        elif N==3:
            total_price(cost)
        else:
            print("Thank You for Shopping!")
            return
        
# Adds the items to the cart
def add_items():
    item_name=input("Enter the Name of the Item:\n")
    while True:
        rate=float(input("Enter the Cost of the Item:\n"))
        if rate<=0:
            print("Enter the Vaild Price!!")
        else:
            print(f"Your Item {item_name} is added successfully to the cart!!")
            return item_name,rate

# Views the List of Items present in the cart
def view_items(items,cost):
    if len(items)==0:
        print("Your Shopping Cart is Empty!!")
    else:
        print(" Items\tCost")
        for i in range(len(items)):
            print(f" {items[i]}\t{cost[i]}")
            

# Calculates the Total Amount of all items:
def total_price(cost):
    if len(cost)==0:
        print("Your Shopping Cart is Empty!!")
    else:
        sum=0
        for i in range(len(cost)):
            sum+=cost[i]
        print(f"Your Total Amount is Rs.{sum}")

# Main Function
def main():
    options()
main()