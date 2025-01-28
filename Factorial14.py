
# User Input:
def get_input():
    while True:
        N=int(input("Enter the Number :\n"))
        if(N<0):
            print("Factorial of Negative Numbers doesn't exist.\nTRY AGAIN!!")
        else:
            break
    return N

# Factorial Calculator
def calculate(N):
    Factorial=1
    if N<=1 :
        return Factorial
    for i in range(2,N+1):
        Factorial*=i
    return Factorial

#Displays the output
def display(N,Factorial):
    print(f"Factorial of {N} : {Factorial}")

# Main Function
def main():
    N=get_input()
    fact=calculate(N)
    display(N,fact)
main()