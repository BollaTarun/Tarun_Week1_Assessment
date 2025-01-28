
# User Input:
def get_input():
    while True:
        N=int(input("Enter the Size of Pattern :\n"))
        if(N<=0):
            print("Size can't be negative.\n TRY AGAIN!!!")
        else:
            break
    return N

# Generates and Prints the Pattern
def pattern_generator(N,order):
    for i in range(N):
        for j in range(N):
            if order==False:
                if(j<=i):
                    print("*",end=" ")
                else:
                    print("  ",end="")
            else:
                if(j>=i):
                    print("*",end=" ")
                else:
                    print("  ",end="")
        print()
    
# Provides option to user whether to print the pattern in Reverse Order:
def option():
    v=input("Do you want to print the Reverse Order of Pattern?\n If yes please press Y,else press any value\n")
    if v=="Y" or v=='y':
        return True
    else:
        return False

# Main Function
def main():
    N=get_input()
    reverse_order=False
    print(f"Pattern of Order {N}:")
    pattern_generator(N,reverse_order)
    reverse_order=option()
    if reverse_order==True:
        print(f"\nReverse Pattern of Order {N}:")
        pattern_generator(N,reverse_order)
main()