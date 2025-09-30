def main():
    #demo4()
    #demo5()
    #demo6()
    #demo7()
    #demo8()
    #demo9()
    demo10()

def demo10():
    sales = 15000
    sales_quota = sales > 10000
    if sales_quota:
        print("Quota met")
    else:
        print("Quota not met")

def demo9():
    # numbers between 10 and 50
    num = int(input("Enter a number between 10 and 50: "))
    if num >= 10 and num <= 50:
        print("Good number")
    else:
        print("Wrong number")

    num = int(input("Enter a not between 10 and 50: "))
    if num < 10 or num > 50:
        print("Good number")
    else:
        print("Wrong number")
    # not(p and q) === not p or not q
    # not(p or q) === not p and not q

def demo8():
    #short circuit evaluation
    num1 = 10
    num2 = 5
    num3 = 0
    if num1 // num2 > 2 and num2 // num3 > 0:
        print("GOOD")
    else:
        print("NOT GOOD")


def demo7():
    x = 5
    y = 10
    a = 8
    b = 15
    if x > y or a < b and b < x :
        print("TRUE")
    else:
        print("FALSE")

def demo6():
    score = int(input("What score did he earn on exam? "))
    if score < 60:
        print("Grade is F")
    elif score < 70:
        print("Grade is D")
    elif score < 80:
        print("Grade is C")
    elif score < 90:
        print("Grade is B")
    else:
        print("Grade is A")

def demo5():
    score = int(input("What score did he earn on exam? "))
    if score > 60:
        if score > 70:
            if score > 80:
                if score > 90:
                    print("Grade is A")
                else:
                    print("Grade is B")
            else:
                print("Grade is C")
        else:
            print("Grade is D")
    else:
        print("Grade is F")




def demo4():
    MIN_SALARY = 35000
    MIN_YEARS = 3
    salary = float(input("Enter salary: "))
    year_working = int(input("Years at the job: "))
    # if salary > MIN_SALARY and year_working > MIN_YEARS:
    #     print("He receives the loan")
    # else:
    #     print("He does not receive the loan")
    # if salary > MIN_SALARY:
    #     if year_working > MIN_YEARS:
    #         print("He receives the loan.")
    #     else:
    #         print("He does not recieve the loan - too few years at the job.")
    # else:
    #     print(f"You must earn at least {MIN_SALARY} to qualify.")
    if salary < MIN_SALARY:
        print(f"You must earn at least {MIN_SALARY} to qualify.")
    elif year_working < MIN_YEARS:
        print("He does not receive the loan - too few years at the job.")
    else:
        print("He receives the loan.")

main()