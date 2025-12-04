def main():
    #demo1()
    #demo2()
    #demo3()
    #demo4()
    #demo5()
    #demo6()
    #demo7()
    demo8()

def demo8():
    # Initialize an accumulator.
    total = 0.0

    try:
        # Open the sales_data.txt file.
        with open('sales_data.txt', 'r') as infile:
            # Read the values from the file and accumulate them.
            for line in infile:
                amount = float(line)
                total += amount
            print(f'{total:,.2f}')

    except Exception as e:
        print("An error occured.")
        print(e)
    finally:
        print("try is done")


def demo7():
    filename = input("Enter filename to open: ")
    search = input('Enter a description to search for: ')

    # Open the coffee.txt file.
    try:
        with open(filename, 'r') as coffee_file:
            # Read the first record's description field.
            descr = coffee_file.readline()
            found = False
            # Read the rest of the file.
            while descr != '' and not found:
                # Read the quantity field.
                # qty = float(coffee_file.readline())

                # Strip the \n from the description.
                descr = descr.split(',')

                descrip = descr[0]
                qty = descr[1].rstrip('\n')
                qty = int(qty)

            # Determine whether this record matches
            # the search value.
                if descrip == search:
                    # Display the record.
                    print(f'Description: {descrip}')
                    print(f'Quantity: {qty}')
                    print()
                    # Set the found flag to True.
                    found = True

                # Read the next description.
                descr = coffee_file.readline()

    # If the search value was not found in the file
    # display a message.
        if not found:
            print('That item was not found in the file.')
    except FileNotFoundError:
        print("File not found")
    except IOError:
        print("Error trying to read the file.")
    except ValueError as err:
        print(err)
        #print("Non-numeric data found in the file.")
    except:
        print("An error occured.")


def demo6():
    try:
        num1 = int(input("Enter a number: "))
        num2 = int(input("Enter another number: "))
        if num2 != 0:
            result = num1 / num2
            print(f'{num1} / {num2} is {result:.2f}')
        else:
            print("cannot divide by 0")
    except ValueError:
        print("ERROR: Enter only valid decimal numbers.")



def demo5():
    # num_emps = int(input("How many employees do you want to enter: "))
    # emp_file = open('employees.txt', 'w')
    # for i in range(1, num_emps + 1):
    #     print(f"Enter data for employee #{i}: ", end="")
    #     name = input("Enter name: ")
    #     id_num = input("Enter id: ")
    #     dept = input("Department: ")
    #     emp_file.write(name + '\n')
    #     emp_file.write(id_num + '\n')
    #     emp_file.write(dept + '\n')
    # emp_file.close()
    emp_file = open('employees.txt', 'r')
    for name in emp_file:
        name = name.rstrip('\n')
        id_num = emp_file.readline().rstrip('\n')
        dept = emp_file.readline().rstrip('\n')
        print(f"Name: {name}")
        print(f"ID: {id_num}")
        print(f"Dept: {dept}")
        print('--------')
    emp_file.close()





def demo4():
    sum = 0
    numbers_file = open("numbers.txt", 'r')
    for line in numbers_file:
        if line != '\n':
            sum += int(line)
    print(sum)

def demo3():
    sum = 0
    numbers_file = open("numbers.txt", 'r')
    num = numbers_file.readline()
    while num != '':
        if num != '\n':
            sum += int(num)
        num = numbers_file.readline()
    numbers_file.close()
    print(sum)


def demo2():
    num1 = int(input("Enter first number to add: "))
    num2 = int(input("Enter second number to add: "))
    sum = num1 + num2
    file_object = open("sums.txt", 'w')
    #file_object.write(sum)   write only writes strings
    file_object.write("Sum is " + str(sum) + "\n")
    file_object.write(f"{num1} +  {num2} = {num1 + num2}")
    file_object.close()
    print("----------------")
    file_object = open("numbers.txt", 'r')
    num1 = int(file_object.readline())
    num2 = int(file_object.readline())
    num3 = int(file_object.readline())
    print(f"{num1} = {num2 + num3}")


def demo1():
    # file_object = open(<name of the file>, 'w' or 'r' or 'a')
    file_object = open('names.txt', 'w')
    file_object.write("Avraham" + "\n")
    file_object.write("Yitzchak ")
    file_object.write("Yaakov\n")
    file_object.close()
    file_object = open('names.txt', 'r')
    file_contents = file_object.read()
    file_object.close()
    print(file_contents)
    print("-----------------")
    file_object = open('names.txt', 'r')
    file_contents = file_object.readline()
    print(file_contents, end="")
    file_contents = file_object.readline()
    print(file_contents, end="")
    file_object.close()
    print("----------------")
    file_object2 = open("holidays.txt", "r")
    file_contents = file_object2.readline()
    file_contents = file_contents.rstrip('\n')
    print(file_contents)
    file_contents = file_object2.readline()
    file_contents = file_contents.rstrip('\n')
    print(file_contents)
    file_contents = file_object2.readline()
    file_contents = file_contents.rstrip('\n')
    print(file_contents)
    file_contents = file_contents.rstrip('os')
    print(file_contents)
    print("---------------")
    file_object2.close()
    file_object = open("names.txt",'a')
    file_object.write("Sarah\n")
    file_object.write("Rivka\n")
    file_object.write("Leah\n")
    file_object.write("Rachel")
    file_object.close()


main()
