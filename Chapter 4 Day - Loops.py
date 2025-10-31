from random import randint

import turtle

def main():
    #demo1()
    #demo2()
    #demo3()
    #demo4()
    #demo5()
    #demo6()
    #demo7()
    #demo8()
    #demo9()
    #demo10()
    #demo11()
    #demo12()
    #demo13()
    demo14()



def demo14():
        turt = turtle.Turtle()
        turt.speed(0)
        turt.ht()
        radius = 100
        angle = 10
        turt.penup()
        # turt.sety(-200)
        turt.pendown()
        for count in range(36):
            #color = randint(0,256)

            draw_circle(0, 0, "blue", radius, angle)
            angle += 10
            # radius += 6
            #turt.penup()
            # turt.sety(turt.ycor() - 6)
            #turt.left(10)
            #turt.pendown()
        demo13()
        demo12()
        turtle.done()

def draw_circle(x, y, color, radius, angle):
    turt = turtle.Turtle()
    turt.ht()
    turt.penup()
    turt.speed(0)
    turt.left(angle)
    turt.goto(x, y)
    turt.pendown()
    turt.fillcolor(color)
    turt.begin_fill()
    turt.circle(radius)
    turt.end_fill()


def demo13():
        turt = turtle.Turtle()
        turt.speed(0)
        turt.ht()
        radius = 100
        turt.penup()
        # turt.sety(-200)
        turt.pendown()
        for count in range(36):
            turt.circle(radius)
            #radius += 6
            turt.penup()
            #turt.sety(turt.ycor() - 6)
            turt.left(10)
            turt.pendown()
        #turtle.done()


def demo12():
    turt = turtle.Turtle()
    turt.speed(0)
    turt.ht()
    radius = 5
    turt.penup()
    #turt.sety(-200)
    turt.pendown()
    for count in range(50):
        turt.circle(radius)
        radius += 6
        turt.penup()
        turt.sety(turt.ycor() - 6)
        turt.pendown()





    #turtle.done()



def demo11():
    for num1 in range(1, 8):
        for num2 in range(num1):
            print("*", end= "  ")
        print()

    for num1 in range(1, 9):
        for num2 in range(9, num1, -1):
            print("*", end= "  ")
        print()

    
def demo10():
    for minutes in range(60):
        for seconds in range(60):
            print(f"{minutes}:{seconds}")

    for num1 in range(13):
        for num2 in range(11):
            print(f"{num1 * num2:3}", end= "  ")
        print()

def demo9():
    print("I will average for you test grades.")
    nums = int(input("How many would you like to enter? "))
    total_num = 0
    for i in range(nums):
        # user_num = int(input("Enter a number #" + str(i + 1) + ": "))
        user_num = int(input(f"Enter test grade #{i + 1} (grades must be between 30 and 100): "))
        while user_num < 30 or user_num > 100:
            user_num = int(input(f"INVALID GRADE!! Enter test grade #{i + 1} (grades must be between 30 and 100): "))
        total_num = total_num + user_num
    print(f"The average is {total_num / nums:.2f}.")


def demo6():
    print("You can enter numbers to me and I will add them up.")
    nums = int(input("How many would you like to enter? "))
    total_num = 0
    for i in range(nums):
        #user_num = int(input("Enter a number #" + str(i + 1) + ": "))
        user_num = int(input(f"Enter a number #{i + 1}: "))
        total_num = total_num + user_num
    print(f"The sum is {total_num}.")

def demo7():
    print("You can enter numbers to me and I will add them up.")
    num = int(input("Enter your numbers (enter X when you are done): "))
    total_num = 0
    i = 2
    while num != 'X':
        #total_num = total_num + num
        total_num += num
        # user_num = int(input("Enter a number #" + str(i + 1) + ": "))
        num = input(f"Enter another number #{i}: ")
        if num != 'X':
            num = int(num)
        i += 1
    print(f"The sum is {total_num}.")

def demo8():
    print("You can enter numbers to me and I will add them up.")
    num = int(input("Enter your numbers (enter -99 when you are done): "))
    total_num = 0
    i = 2
    while num != -99:
        total_num = total_num + num
        # user_num = int(input("Enter a number #" + str(i + 1) + ": "))
        num = int(input(f"Enter another number #{i}: "))
        i = i + 1
    print(f"The sum is {total_num}.")

def demo5():
    for i in range(0, 101, 10):
        print(i)

    for i in range(1, 30, -1):
        print(i)
    print("---------------")
    for i in range(30, 1, -5):
        print(i)

def demo4():
    for num in range(5):
        print("Hello", num)
    print("==========")
    for num in range(1, 5):
        print("Hello", num)
    print("============")
    for num in range(5, 10):
        print("Hello", num)
    print("num = ", num)
    for num in range(5, 10):
        num = num + 1
        print("Hello", num)
    print("-------------")
    print("Number\tSquare")
    for num in range(1, 11):
        square = num ** 2
        print(f"{num}\t{square}")


def demo3():
    for i in [1, 2, 3, 4, 5]:
        print("hello", i)

    for i in ["Yossel", "Shmerel", "Berel", 1, 2, 3]:
        print("hello", i)

def demo2():
    MAX_TEMP = 102.5
    temp = float(input("Enter the temperature: "))
    while temp > MAX_TEMP:
        print("Temperature is too high. Lower the thermostat and wait five minutes.")
        temp = float(input("Enter the temperature: "))
    #infinite loop
    # while temp > MAX_TEMP:
    #    print("Temperature is too high. Lower the thermostat and wait five minutes.")
    #    float(input("Enter the temperature: "))

    print("The temperature is now acceptable.")



def demo1():
    keep_going = 'y'
    while keep_going == 'y' or keep_going == "Y":
        sales = float(input("Enter amount of sales: "))
        comm_rate = float(input("Enter commission: "))
        commision = sales * comm_rate
        print(f"You have earned {commision:.2f} in sales commsion.")
        keep_going = input("Do you want to calculate another commission (y for yes): ")

main()