# Task 1.1
def task_1_1():
    numbers = [4, 8, 15, 16, 23, 42]
    output = ' '.join(map(str, numbers))
    print(output)

# Task 1.2
def task_1_2():
    numbers = [4, 8, 15, 16, 23, 42]
    for num in numbers:
        print(num)

# Task 1.3
def task_1_3():
    try:
        num = int(input("Please enter a number: "))
        for i in range(num, num+3):
            print(i)
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Task 1.4
def task_1_4():
    try:
        num1 = int(input("Please enter the first number: "))
        num2 = int(input("Please enter the second number: "))
        num3 = int(input("Please enter the third number: "))
        total = num1 + num2 + num3
        print(total)
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Task 1.5
def task_1_5():
    try:
        edge_length = int(input("Please enter the edge length of the cube: "))
        volume = edge_length**3
        surface_area = 6 * (edge_length**2)
        print(f"Volume = {volume}\nTotal surface area = {surface_area}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Task 2.1
def task_2_1():
    try:
        N = int(input("Number of schoolchildren: "))
        K = int(input("Number of tangerines: "))
        whole_tangerines = K // N
        remaining_tangerines = K % N
        print(f"Each student gets {whole_tangerines} whole tangerine(s) and {remaining_tangerines} remain in the basket.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Task 2.2
def task_2_2():
    try:
        num = int(input("Please enter a four-digit number: "))
        thousands = num // 1000
        hundreds = (num % 1000) // 100
        tens = (num % 100) // 10
        units = num % 10
        print(f"The digit in the thousands position is {thousands}")
        print(f"The digit in the hundreds position is {hundreds}")
        print(f"The digit in the tens position is {tens}")
        print(f"The digit in the position of units is {units}")
    except ValueError:
        print("Invalid input. Please enter a valid four-digit number.")

# Task 2.3
def task_2_3():
    try:
        population = int(input("Please enter the population of the universe: "))
        survivors = population // 2 if population % 2 == 0 else (population // 2) + 1
        print(f"The number of survivors is {survivors}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Task 2.4
def task_2_4():
    try:
        num = int(input("Please enter a number: "))
        result = num << 1
        if result == 0:
            print("Warning: Result is zero.")
        else:
            print(f"The result of << is {result}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Task 2.5
def task_2_5():
    try:
        num1 = float(input("Please enter the first number: "))
        num2 = float(input("Please enter the second number: "))
        operation = input("Please choose the operation (+, -, *, /): ")

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            result = num1 / num2
        else:
            print("Invalid operation. Please choose from +, -, *, /")
            return

        print(f"{num1} {operation} {num2} = {result}")
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
    except ZeroDivisionError:
        print("Error: Division by zero.")

# Magic Button :D
task_1_1()
task_1_2()
task_1_3()
task_1_4()
task_1_5()

task_2_1()
task_2_2()
task_2_3()
task_2_4()
task_2_5()