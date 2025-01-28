
# Takes User Input of String:
def get_input():
    str=input("Enter the Input String:\n")
    return str

# String Analysis of Consonants, Vowels and Digits and Special Characters
def string_analyzer(s):
    str=s.lower()
    vowels='aeiou'
    D=0
    V=0
    C=0
    SC=0
    for i in range(len(str)):
        if str[i].isdigit():
            D+=1
        elif str[i].isalpha():
            if str[i] in vowels:
                V+=1
            else:
                C+=1
        else:
            SC+=1
    return D,V,C,SC

# Displays the Analysis performed on String     
def display(str,D,V,C,SC):
    print("\t\t\tSTRING ANALYSIS\nGiven String : ",str)
    print("Number of Vowels : ",V)
    print("Number of Consonants : ",V)
    print("Number of Digits : ",D)
    print("Number of Special Characters : ",SC)

# Main Function
def main():
    str=get_input()
    D,V,C,SC=string_analyzer(str)
    display(str,D,V,C,SC)
main()