
# Takes User Input of multiple words until user wish
def get_input():
    word=""
    while True:
        word=input("Enter the String you want to enter:\nTo exit, press N\n")
        if word=='N' or word.upper()=='N':
            break
        else:
            B=palindrome_checker(word)
            display(word,B)

# Checks if the given word is Palindrome or not :
def palindrome_checker(S):
    K=S.lower()
    reverse=K[::-1]
    if K==reverse:
        return True
    else:
        return False

# Display whether the input is palindrome or not
def display(S,ans):
    if ans==True:
        print(f"{S} is a Palindrome.")
    else:
        print(f"{S} is not a Palindrome.")

# Main Function
def main():
    S=get_input()
main()