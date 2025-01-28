
# Collects user input based and stores in the list :
import math
def get_input():
    list=[]
    N=int(input("Enter the Size of the List:\n"))
    for i in range(N):
        list.append(float(input(f"Enter the Element {i+1} :\n")))
    return list,N

# Performs the comparisons to find the second largest number.
def second_max(list,N):
    max=-math.inf          # Minimum Value
    second_max=-math.inf
    for i in range(N):
        if list[i]>max:   # For 2nd Largest Non-Distinct Number : if list[i]>=max
            second_max=max
            max=list[i]
        elif list[i]>second_max and list[i]<max:  
            second_max=list[i]
    return second_max

# Displays the Second Maximum Number
def display(ans):
    if ans==-math.inf:
        print("Only 1st Largest Distinct Number Exists.")
    else:
        print(f"Second Largest Number : {ans}")
        
# Main Function calls the other functions to perform the task
def main():
    list,size=get_input()
    ans=second_max(list,size)
    display(ans)
main()