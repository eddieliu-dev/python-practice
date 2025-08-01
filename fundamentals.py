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
def student_scores_dictionary():
    student_dic = {
        "student1": {
            "name": "Bob",
            "score": 93
        },
        "student2": {
            "name": "Jack",
            "score": 88
        },
        "student3": {
            "name": "John",
            "score": 100
        }
    }
    highest_student = student_dic["student1"]
    for stu in student_dic.values():
        if stu["score"] > highest_student["score"]:
            highest_student = stu
    highest_score = highest_student["score"]
    print("Student with the highest score is: " + highest_student["name"] + " with the score of " + str(highest_score))


# Word Count in a Sentence
# Ask for a sentence
# Count how many times each word appears
def word_count():
    sentence = input("Please enter a sentence: ")
    words = sentence.split()
    word_dict = dict()
    for w in words:
        word_dict[w] = 0
    for w in words:
        for d in word_dict:
            if w == d:
                word_dict[d] += 1
    print(word_dict)

# Temperature Converter Function
# Write two functions:
# celsius_to_fahrenheit(c)
# fahrenheit_to_celsius(f)
def celsius_to_fahrenheit(c):
    print(c * 9/5 +32)
def fahrenheit_to_celsius(f):
    print((f-32) * 5/9)

# Read and Count Words from File
# Write a text file manually (data.txt)
# Write a script to open the file, read the content, and count how many words it has
def read_and_count_words_from_file(f):
    count = 0
    with open(f) as file:
        for line in file:
            words = line.split()
            count += len(words)
            # print(line)
    print(count)

# Contact Book
# Allow user to:
# Add contact (name, phone)
# Search for contact
# List all contacts
# Save the data to a text file (one contact per line)
def contact_book():
    contact_dict = {
        "John Doe": "99999999999"
    }
    print("Manual: to be written. Enter \"I'm done\" to end the session.")
    print("-------------------------------------------------------------")
    user_command = input("What do you want to do today? ")
    while user_command != "I'm done":
        if "add" in user_command.lower():
            user_command = input("Please enter the name: ")
            name = user_command
            user_command = input("Please enter the phone number: ")
            phone_number = user_command
            contact_dict[name] = phone_number
            # print(contact_dict)
            print("Add complete!")
            print("-------------------------------------------------------------")
            user_command = input("Anything else? ")
        elif "search" in user_command.lower():
            user_command = input("Please enter the name: ")
            for cont in contact_dict:
                if cont == user_command:
                    print(contact_dict[user_command])
                else:
                    print("Cannot find " + user_command)
            print("-------------------------------------------------------------")
            user_command = input("Anything else? ")
        elif "list" in user_command.lower():
            with open("contact_book.txt") as book:
                print(book.read())
            print("-------------------------------------------------------------")
            user_command = input("Anything else? ")
        elif "save" in user_command.lower():
            with open("contact_book.txt", "w") as book:
                for cont in contact_dict:
                    book.write(cont + ": " + contact_dict[cont] + "\n")
            print("Save complete!")
            print("-------------------------------------------------------------")
            user_command = input("Anything else? ")
        else:
            print("-------------------------------------------------------------")
            user_command = input("Please enter a valid command: ")


def main():
    # hello_and_age()
    # calculator()
    # odd_or_even()
    # multiplication_table()
    # guess_the_number()
    # list_processing()
    # student_scores_dictionary()
    # word_count()
    # celsius_to_fahrenheit(35)
    # fahrenheit_to_celsius(100)
    # read_and_count_words_from_file("data.txt")
    contact_book()


if __name__ == "__main__":
    main()
