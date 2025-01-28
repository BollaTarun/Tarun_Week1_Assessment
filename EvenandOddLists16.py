
# User Input of List Size and List of Elements
def get_input():
    list=[]
    N=int(input("Enter the Size of the List:\n"))
    for i in range(N):
        V=int(input(f"Enter the Element {i+1} :\n"))
        list.append(V)
    return list,N

# Creates 2 lists based on divisibility of number :
def even_odd_separator(list,N):
    even_list=[]
    odd_list=[]
    
    for i in range(N):
        if list[i]%2==0:
            even_list.append(list[i])
        else:
            odd_list.append(list[i])
    return even_list,odd_list

# Displays the output:
def display(even,odd):
    if even==[]:
        print("Even List is Empty.")
    else : 
        print("Even List :",even)
    if odd==[]:
        print("Odd List is Empty.")
    else : 
        print("Odd List :",odd)

# Main Function :
def main():
    list,N=get_input()
    even,odd=even_odd_separator(list,N)
    display(even,odd)

main()