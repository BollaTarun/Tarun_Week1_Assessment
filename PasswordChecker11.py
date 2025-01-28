
# User Input of Password
def get_input():
    password=input("Enter your Password to test it's strength:\n")
    return password

# Checks the Strength of the Password
def strength_checker(P):
    lower=False
    upper=False
    digits=False
    special_char=False
    L=len(P)
    for i in range(L):
        if P[i].isdigit():
            digits=True
        elif P[i].islower():
            lower=True
        elif P[i].isupper():
            upper=True
        else:
            special_char=True
    if L>=8 and lower==True and upper==True and digits==True and special_char==True :
        return True
    else:
        return False

# Displays the Strength of the Password
def display(ans):
    if ans==True:
        print("Your Password is Strong and Hard to Hack.")
    else:
        print("Your Password is Weak and Easy to Hack.")

# Main Function
def main():
    P=get_input()
    ans=strength_checker(P)
    display(ans)
main()
