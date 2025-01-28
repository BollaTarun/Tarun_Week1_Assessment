
# user Input
def get_input():
    while True:
        weight=float(input("Enter the Weight of the Person in terms of kilogram :\n"))
        height=float(input("Enter the Height of the Person in terms of meters :\n"))
        if weight<=0 or height<=0 :
            print("Invalid Information.")
        else:
            return weight,height

# Calculates the BMI value and provides the required message.
def BMI_status_report(W,H):
    bmi_value=(W/(H*H))
    print(f"Your Body Mass Index : {round(bmi_value,2)}")
    if bmi_value<18.5 :
        print("You are Under Weight based on requirement.\nImprove your diet and exercise regularly.")
    elif bmi_value>=18.5 and bmi_value<=24.9:
        print("You are Normal based on requirement.\n")
    elif bmi_value>=25.0 and bmi_value<=29.9:
        print("You are Over Weight compared to requirement levels.\nImprove your diet and exercise reqularly.")
    else:
        print("You are Obesed compared to requirement levels.\nConsult a doctor for precautionary measures.")

def main():
    W,H=get_input()
    BMI_status_report(W,H)
main()