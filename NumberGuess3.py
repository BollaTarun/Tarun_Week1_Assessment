
import random
# Takes User Input until it is Correct Answer :
def guess_checker():
    R=random.randint(1,100)
    a=0
    while True:
        N=int(input("Enter your Guessed Number :\n"))
        a+=1
        if(N<1 or N>100):
            print("Out of Range.")
        elif N<R:
            if abs(N-R)>10:
                print("Too Low")
            else :
                print("Lower")
        elif N>R:
            if abs(N-R)>10:
                print("Too High")
            else:
                print("Higher")
        else:
            print("Correct Answer")
            print(f"You have guessed the Right Answer in {a} Attempts")
            return
        
# Main Function:
def main():
    print("\n\t\t\t\tGUESS THE MISSING NUMBER\n")
    print("Guess the Random number generated from our system between 1 to 100 :")
    guess_checker()
main()