import random


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
        print(float(first_num) + float(second_num))
    elif "-" in calculator:
        first_num, second_num = calculator.split("-")
        print(float(first_num) - float(second_num))
    elif "*" in calculator:
        first_num, second_num = calculator.split("*")
        print(float(first_num) * float(second_num))
    else:
        first_num, second_num = calculator.split("/")
        print(float(first_num) / float(second_num))


# Odd or Even
# Ask the user for a number
# Print whether it’s odd or even
def odd_or_even():
    num = input("Give me a number: ")
    if int(num) % 2 == 0:
        print(num + " is even.")
    else:
        print(num + " is odd.")


# Multiplication Table
# Ask for a number n
# Print its multiplication table up to 10
def multiplication_table():
    n = input("Give me a number: ")
    multiple = 0
    while multiple != 10:
        multiple += 1
        print(n + "*" + str(multiple) + "=" + str(int(n) * multiple))


# Guess the Number
# Generate a random number between 1 and 20
# Let the user guess until they get it right
# Show how many attempts it took
def guess_the_number():
    rand = random.randint(1, 20)
    guess = int(input("Guess a number between 1 and 20: "))
    while guess != rand:
        if guess < rand:
            print("Too low!")
            guess = int(input("Guess again: "))
        else:
            print("Too high!")
            guess = int(input("Guess again: "))
    print("Correct!")


# List Processing
# Given a list of numbers: [5, 3, 8, 6, 7, 2]
# Find the maximum, minimum, and average
# Sort the list in descending order
def list_processing():
    list = [5, 3, 8, 6, 7, 2]
    max = list[0]
    min = list[0]
    sum = 0
    for i in range(len(list)):
        if list[i] > max:
            max = list[i]
        if list[i] < min:
            min = list[i]
        sum += list[i]
    print(list)
    print("max=" + str(max) + ", min=" + str(min) + ", average=" + str(sum / len(list)))
    list.sort(reverse=True)
    print(list)

    # Student Scores Dictionary
    # Create a dictionary storing student names and their scores
    # Add at least 3 students
    # Print the student with the highest score


    # Word Count in a Sentence
    # Ask for a sentence
    # Count how many times each word appears

    # Temperature Converter Function
    # Write two functions:
    # celsius_to_fahrenheit(c)
    # fahrenheit_to_celsius(f)

    # Read and Count Words from File
    # Write a text file manually (data.txt)
    # Write a script to open the file, read the content, and count how many words it has

    # Contact Book
    # Allow user to:
    # Add contact (name, phone)
    # Search for contact
    # List all contacts
    # Save the data to a text file (one contact per line)


def main():
    # hello_and_age()
    # calculator()
    # odd_or_even()
    # multiplication_table()
    # guess_the_number()
    list_processing()


if __name__ == "__main__":
    main()
