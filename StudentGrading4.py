
# User Input:
def get_input():
    name=input("Enter the Student's Name :\n")
    marks_list=[]
    for i in range(5):
        while True:
            K=(int(input(f"Enter the Marks of Subject {i+1} : \n")))
            if K>=0 and K<=100:
                break
            else :
                print("Enter the Marks of Range from 1 to 100!!!")
        marks_list.append(K)
    return name,marks_list

# Allocates the grade based on their marks
def grade_allocator(marks):
    if marks>=85:
        return 'O'
    elif marks>=70 :
        return 'A'
    elif marks>=65 :
        return 'B'
    elif marks>=50 :
        return 'C'
    elif marks>=35:
        return "Pass"
    else:
        return "Fail"
    
# Makes required calculation to allocate grade
def grade_calculation(marks_list):
    sum=0
    Fail=False
    subject_grade=[]
    for i in range(5):
        sum+=marks_list[i]
        subject_grade.append(grade_allocator(marks_list[i]))
        if subject_grade[i]=="Fail":
            Fail=True
    Avg=int(sum/5)
    overall_grade=grade_allocator(Avg)
    return subject_grade,sum,overall_grade,Fail

# Displays the input with their allocated grade
def display(name,marks,sub_grade,total_marks,overall_grade,fail):
    print(f"Student Name : {name}")
    print(" Subject     Marks  Grade")
    for i in range(5):
        print(f"Subject {i+1} :   {marks[i]}      {sub_grade[i]}")
    print(f"\nOverall Marks : {total_marks}")

    if fail==True:
        print("Overall Grade : FAIL")
    else:
        print(f"Overall Grade : {overall_grade}")

# Main Function
def main():
    name,marks=get_input()
    sub_grade,total_marks,overall_grade,fail=grade_calculation(marks)
    display(name,marks,sub_grade,total_marks,overall_grade,fail)
main()