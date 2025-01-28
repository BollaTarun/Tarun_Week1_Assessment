
import math
# Collects the range until the input is valid
def get_input():
    while True:
        L=int(input("Enter the lower Limit:\n"))
        R=int(input("Enter the Upper Limit:\n"))
        if L<0 or R<L:
            print("Enter a Valid Range!!")
        else:
            return L,R
        
# Checks if given number is prime or not
def is_prime(N):
    if N==2:
        return True
    elif N%2==0 or N<=1:
        return False
    else:
        for i in range(3,int(math.sqrt(N))+1,2):
            if N%i==0:
                return False
        return True

# Identifies and prints the prime numbers in range
def prime_number_in_range(L,R):
    print(f"Prime Number in the range of [{L},{R}]:")
    for L in range(R+1):
        if is_prime(L)==True:
            print(L,end=" ")

# Main Function
def main():
    L,R=get_input()
    prime_number_in_range(L,R)
main()

