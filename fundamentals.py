# Hello and Age
# Asks the user for their name and age
# Prints: "Hello [name], you will be [age + 1] next year!"
def hello_and_age():
    name = input("What is your name? ")
    age = input("What is your age? ")
    print("Hello " + name + ", you will be " + str(int(age) + 1) + " next year!")

# Calculator
# Takes two numbers and an operator (+, -, *, /) as input
# Prints the result
def calculator():
    calculator = input("Calculator initiated:\n")
    if "+" in calculator:
        first_num, second_num = calculator.split("+")
        print(float(first_num)+float(second_num))
    elif "-" in calculator:
        first_num, second_num = calculator.split("-")
        print(float(first_num) - float(second_num))
    elif "*" in calculator:
        first_num, second_num = calculator.split("*")
        print(float(first_num) * float(second_num))
    else:
        first_num, second_num = calculator.split("/")
        print(float(first_num) / float(second_num))

def main():
    # hello_and_age()
    calculator()

if __name__ == "__main__":
    main()