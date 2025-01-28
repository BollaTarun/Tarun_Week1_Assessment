
# User Input of Temperature and it's type of Degree
def get_input():
    temp_type=0
    print("\n\t\t\t\tTEMPERATURE CONVERTER")
    print("Please mention the Temperature Degree Type of your Input:")
    print("Enter 1 for Celsius")
    print("Enter 2 for Fahrenheit")
    print("Enter 3 for Kelvin")
    while True:
        temp_type=int(input())
        if temp_type>=4:
            print("Enter a Valid Choice !!")
        else:
            break
    temperature=float(input("Enter the Temperature :\n"))
    return temperature,temp_type

# Converts the given temperature into other degrees :
def conversions(temp_type,temp):
    C=0
    F=0
    K=0
    if temp_type==1:
        C=temp
        F=to_fahrenheit(C,1)
        K=to_kelvin(C,1)
    if temp_type==2:
        F=temp
        C=to_celsius(F,2)
        K=to_kelvin(F,2)
    if temp_type==3:
        K=temp
        C=to_celsius(K,3)
        F=to_fahrenheit(K,3)

    return round(C,2),round(F,2),round(K,2)
    

# Converts the given temp into celsius:
def to_celsius(temperature,N):
    if N==2:
        value=(5*(temperature-32))/9
    else:
        value=temperature-273.15
    return value

# Converts the given temp into celsius:
def to_fahrenheit(temperature,N):
    if N==3:
        temperature-=273.15
    value=((9*temperature)/5)+32
    return value

# Converts the given temp into celsius:
def to_kelvin(temperature,N):
    if N==1:
        value=273.15+temperature
    else:
        print(temperature-32)
        value=(((temperature-32)*5)/9)+273.15
        print("F to K:",value)
    return value

# Displays the other degrees of temperature based on the given input
def display(temp_type,C,F,K):
    if temp_type!=1:
        print(f"Temperature in Celsius : {C} C")
    if temp_type!=2:
        print(f"Temperature in Fahrenheit : {F} F")
    if temp_type!=3:
        print(f"Temperature in Kelvin : {K} K")

def main():
    temp,temp_type=get_input()
    C,F,K=conversions(temp_type,temp)
    display(temp_type,C,F,K)
main()