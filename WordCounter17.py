
# User Input of Sentence 
def get_input():
    S=input("Enter the Sentence as an input :\n")
    return S

def word_counter(S):
    counter={}
    S=S.lower()
    list=S.split()
    for word in list:
        if word in counter:
            counter[word]+=1
        else:
            counter[word]=1
    return counter

def display(counter):
    print(" Word\tCounter")
    for key,value in counter.items():
        print(" ",key,"\t",value)

def main():
    S=get_input()
    W=word_counter(S)
    display(W)
main()