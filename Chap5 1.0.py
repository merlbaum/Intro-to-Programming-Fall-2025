import turtle
import random
import math
import circle
import rectangle

DISCOUNT_PERCENTAGE = .20
my_value = 10

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
    #demo14()
    demo15()

def demo15():
    # Constants for the menu choices
    AREA_CIRCLE_CHOICE = 1
    CIRCUMFERENCE_CHOICE = 2
    AREA_RECTANGLE_CHOICE = 3
    PERIMETER_RECTANGLE_CHOICE = 4
    QUIT_CHOICE = 5
        # The choice variable controls the loop
        # and holds the user's menu choice.
    choice = 0

    while choice != QUIT_CHOICE:
            # display the menu.
            display_menu()

            # Get the user's choice.
            choice = int(input('Enter your choice: '))

            # Perform the selected action.
            if choice == AREA_CIRCLE_CHOICE:
                radius = float(input("Enter the circle's radius: "))
                print('The area is', circle.area(radius))
            elif choice == CIRCUMFERENCE_CHOICE:
                radius = float(input("Enter the circle's radius: "))
                print('The circumference is',
                      circle.circumference(radius))
            elif choice == AREA_RECTANGLE_CHOICE:
                width = float(input("Enter the rectangle's width: "))
                length = float(input("Enter the rectangle's length: "))
                print('The area is', rectangle.area(width, length))
            elif choice == PERIMETER_RECTANGLE_CHOICE:
                width = float(input("Enter the rectangle's width: "))
                length = float(input("Enter the rectangle's length: "))
                print('The perimeter is',
                      rectangle.perimeter(width, length))
            elif choice == QUIT_CHOICE:
                print('Exiting the program...')
            else:
                print('Error: invalid selection.')

    # The display_menu function displays a menu.
def display_menu():
        print('        MENU')
        print('1) Area of a circle')
        print('2) Circumference of a circle')
        print('3) Area of a rectangle')
        print('4) Perimeter of a rectangle')
        print('5) Quit')


def demo14():
    result = math.sqrt(25)
    print(result)
    side1 = 10
    side2 = 10
    print(f"Hypotenuse is {math.hypot(side1, side2)}")
    print(math.pi, math.e)
    radius = int(input("Enter radius: "))
    print(f"Area is {circle.area(radius):.2f}")
    print(f"Circumference is {circle.circumference(radius):.2f}")


def demo13():
    #fname, lname  = get_name2()
    #print(fname)
    #print(lname)
    turt = turtle.Turtle()
    turt.goto(random.randint(1, 100), random.randint(1,100))
    x, y = get_turtle_coordinates(turt)
    print(x, y)
    z, p = (5, 10)
    print(z, p)

def get_name2():
    first = input("Enter your first name: ")
    last = input("Enter your last name: ")
    #return first + " " + last
    return first, last

def get_turtle_coordinates(turt):
    x_pos = turt.xcor()
    y_pos = turt.ycor()
    return x_pos, y_pos


def is_even(num):
    return num % 2 == 0
    # if num % 2 == 0:
    #     return True
    # else:
    #     return False

def demo12():
    num = int(input("Enter number to check: "))
    if is_even(num):
        print("Your number is even.")
    else:
        print("Your number is odd")



    name = get_name()
    print(f"Hello {name}.")

def get_name():
    name = input("What is your name? ")
    return name

def demo11():
    # Get the item's regular price.
    reg_price = get_regular_price()

    # Calculate the sale price.
    sale_price = reg_price - discount(reg_price)

    # Display the sale price.
    print(f'The sale price is ${sale_price:,.2f}.')

    # The get_regular_price function prompts the
    # user to enter an item's regular price and it
    # returns that value.

def get_regular_price():
    price = float(input("Enter the item's regular price: "))
    return price

    # The discount function accepts an item's price
    # as an argument and returns the amount of the
    # discount, specified by DISCOUNT_PERCENTAGE.


def discount(price):
    return price * DISCOUNT_PERCENTAGE


def demo10():
    value1 = int(input("Enter first value to add: "))
    value2 = int(input("Enter second value to add: "))
    sum_nums = sum(value1, value2)
    print(f"The sum of your numbers is {sum_nums}.")
    product_nums = multiply(value1, value2)
    print(f"The product of your numbers is {product_nums}.")


def sum(num1, num2):
    result = num1 + num2
    return result

def multiply(num1, num2):
    return num1 * num2

def demo9():
    for i in range(5):
        number = random.randint(1, 50)
        print(f"Random number is {number}")
    for i in range(3):
        die1 = random.randint(1,6)
        die2 = random.randint(1, 6)
        print(f"Dice Roll: {die1} and {die2}")
    print("------------")
    for i in range(4):
        print(random.randrange(10)) # 1 number 0 - 9
        print(random.randrange(5, 10)) # 1 number 5 - 9
        print(random.randrange(0, 101, 10)) # 1 number : 0, 10, 20, 30 ... 90, 100
        print('-----')
    for i in range(2):
        print(random.random())
        print(random.uniform(1.0, 10.0))
    print("-------------")
    random.seed(10)
    for i in range(5):
        print(random.randint(1, 100))


def demo7():
    global my_value
    my_value = my_value * 2
    print(my_value)
    my_value = 10

def demo8():
    print(my_value)


def demo6():
    n1 = 5
    n2 = 10
    show_product(n1, n2)
    show_product(n1)
    show_product(num2= 5, num1= 3)
    show_interest(1000, 10, 3)
    show_interest(3, 1000, 10)
    show_interest(rate= 10, principal= 1000, periods= 3)
    # print(rate) no good


def show_interest(principal, rate, periods):
    interest = principal * (((1 + (rate/100)) ** periods) - 1)

    print(f"The simple interest will be {interest:.2f} dollars.")

def show_product(num1, num2= 1):
    result = num1 * num2
    print(result)

def demo5():
    num = 10
    change_me(num)
    print(num)

def change_me(num):
    num *= 2
    print(num)

def demo4():
    num1 = int(input("Enter first number to sum up: "))
    num2 = int(input("Enter second number to sum up: "))
    print(f"The sum of {num1} and {num2} is ", end="")
    show_sum(num1, num2)

    first_name = "Yankel"
    last_name = "Jones"
    show_sum(first_name, last_name)


def show_sum(n1, n2):
    result = n1 + n2
    print(result)



def demo3():
    # display the intro screen.
    intro()
    # Get the number of cups.
    cups_needed = int(input('Enter the number of cups: '))
    # Convert the cups to ounces.
    cups_to_ounces(cups_needed)

    # The intro function displays an introductory screen.


def intro():
    print('This program converts measurements')
    print('in cups to fluid ounces. For your')
    print('reference the formula is:')
    print('    1 cup = 8 fluid ounces')
    print()

    # The cups_to_ounces function accepts a number of
    # cups and displays the equivalent number of ounces.


def cups_to_ounces(cups):
    ounces = cups * 8
    print(f'That converts to {ounces} ounces.')


def demo2():
    value = 5
    show_double(value)
    show_triple(value)
    # print(number)  not in scope
    if value >= 5:
        value2 = value * 2
    print(value)
    print(value2)

def show_triple(value):
    value *= 3
    print(value)

def show_double(number):
    number *= 2
    print(number)


def demo1():
    print("hello from demo1")
    name = input("What is your name? ")
    texas()
    california()
    texas()
    message()
    print("goodbye from demo1")


def texas():
    birds = 5000
    print("texas has", birds, 'birds.')

def california():
    birds = 8000
    print("California has", birds, "birds.")

def message():
    print('hello from message')
    message2()
    print("goodbye from message")

def message2():
    print('hello from message2')
    print("goodbye from message2")


main()