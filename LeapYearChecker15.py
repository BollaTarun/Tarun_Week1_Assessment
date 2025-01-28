
# Takes User Input untile the input is valid
def get_input():
    while True:
        year=int(input("Enter the Year you want to check:\n"))
        Y=year
        a=0
        while Y>0:
            Y=int(Y/10)
            a+=1
        if a==4:
            return year
        else :
            print("Given Year is Invalid!!")

# Checks if it is a Leap Year or not
def leap_year_checker(Y):
    if Y%4==0:
        if Y%100!=0: 
            return True
        elif Y%400==0:
            return True
        else:
            return False
    else:
        return False
    

# Displays whether given year is Leap year or Not :
def display(Y,ans):
    if ans==True:
        print(f"{Y} is a Leap Year.")
    else:
        print(f"{Y} is not a Leap Year.")

# Main Function
def main():
    Y=get_input()
    ans=leap_year_checker(Y)
    display(Y,ans)
main()
