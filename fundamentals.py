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

# List Processing
# Given a list of numbers: [5, 3, 8, 6, 7, 2]
# Find the maximum, minimum, and average
# Sort the list in descending order

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
    multiplication_table()


if __name__ == "__main__":
    main()
