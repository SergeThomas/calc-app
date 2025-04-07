def mult_calc(num1, num2):
    return num1 * num2


def divide_calc(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        print("Cannot divide by zero")


num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))

mult_calc_result = mult_calc(num1, num2)
divide_calc_result = divide_calc(num1, num2)

print(f"Result of {num1} * {num2} is: {mult_calc_result}")
print(f"Result of {num1} / {num2} is: {divide_calc_result}")