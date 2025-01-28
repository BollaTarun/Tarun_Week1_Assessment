
# User Input
def info():
    N=int(input("Enter the Value to create the Multiplication Table:\n"))
    while True:
        L=int(input("Enter the Lower Limit:\n"))
        R=int(input("Enter the Upper Limit:\n"))
        if L>=0 and L<R:
            return N,L,R
        else:
            print("Enter a Valid Range")

# Generates the Multiplication Table of N from limit L to R.
def table_generator(N,L,R):
    print(f"Multiplication Table of {N} from {L} to {R} :")
    for L in range(R+1):
        print(f"{N} * {L} = {N*L}")

# Main Function :
def main():
    N,lower_limit,upper_limit=info()
    table_generator(N,lower_limit,upper_limit)
main()
