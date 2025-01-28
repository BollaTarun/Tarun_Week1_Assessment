
# User Input of Personal Details
def get_input():
    age=int(input("Enter the Age of Person:\n"))
    salary=float(input("Enter the Salary of Person:\n"))
    credit_score=int(input("Enter the Credit Score of the Person:\n"))
    return age,salary,credit_score

# Checks the
def loan_eligibility_checker(age,salary,credit_score):
    if credit_score<800:
        print("Your Loan is Rejected.\nReason : Minimum Credit Score for Loan Qualification is 800.")
    elif salary<40000:
        print("Your Loan is Rejected.\nReason : Minimum Salary needed for Loan Qualification is Rs.40,000.")
    elif age<=20:
        print("Your Loan is Rejected.\nReason : Minimum Age Limit for Loan Qualification is 21 Years.")
    else : 
        print("Your Loan is Approved as all requirements are satisfied.")

# Main Function
def main():
    A,S,CS=get_input()
    loan_eligibility_checker(A,S,CS)

main()