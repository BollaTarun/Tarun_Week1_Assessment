
# Takes User Input of Number of People, Total Amount and Tip Percentage until valid
def get_input():
    while True:
        N=int(input("Enter the Number of People:\n"))
        if N<=0:
            print("Enter a Valid Number of People!!")
        else:
            break

    while True:
        total=float(input("Enter the Total Amount:\n"))
        if total<=0:
            print("Enter a Valid Number of People!!")
        elif int(total/N)<1:
            print("Amount split is less than 1.\n Enter a Good Amount!!!")
        else:
            break

    while True:
        tip=float(input("Enter the Tip Percentage:\n"))
        if(tip<=0):
            print("Tip is Compulsory!\nPlease enter a valid Tip Percentage!!")
        elif tip>=100:
            print("Tip amount is Invalid.\nEnter a valid Tip Percentage less than 100%")
        else:
            break
    return N,total,tip

def tip_amount(N,total,tip):
    amount=total
    amount+=(tip*total/100)
    return amount/N

def display(person,N):
    print(f"Total Amount : {N*person}")
    print(f"Your Amount to be paid including Tip per Person: {person}")

def main():
    N,total,tip=get_input()
    person=tip_amount(N,total,tip)
    display(person,N)
main()

