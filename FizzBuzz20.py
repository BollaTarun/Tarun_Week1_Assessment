
# Display Numbers based on the given conditions.
def display():
    for i in range(1,101):
        if i%15==0:     # Multiples of 15 (3 and 5)
            print("FizzBuzz")
        elif i%5==0:
            print("Buzz")
        elif i%3==0:
            print("Fizz")
        else:
            print(i)


# Main Function
def main():
    display()
main()