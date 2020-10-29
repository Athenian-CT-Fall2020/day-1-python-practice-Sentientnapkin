# This is an example of a comment that Python ignores. Use these to make notes as you write your code. You will also fill out the top comment with any help or resources you use.
# Collaborators:               (fill this is on every assignment, even if the answer is "none")

# print ("hello world")
# I just left a note :)
# x = int(input("What is your first number: "))
# y = int(input("What is your second number: "))
# a = x*y
# print("Yeah your answer is" ,a )
# print("I am going into a deep slumber for another 1000 years, wake me up later thank you.")


num = 0


def next_a(num):
    x = int(input("What is your next value? "))
    num += x
    print(num)
    another_a(num)


def another_a(num):
    y = input("Another? ")
    if y == "yes":
        next_a(num)
    if y == "no":
        print(num)


def next_s(num):
    x = int(input("What is your next value? "))
    num -= x
    print(num)
    another_s(num)


def another_s(num):
    y = input("Another? ")
    if y == "yes":
        next_s(num)
    if y == "no":
        print(num)


def next_m(num):
    x = int(input("What is your next value? "))
    num *= x
    print(num)
    another_m(num)


def another_m(num):
    y = input("Another? ")
    if y == "yes":
        next_m(num)
    if y == "no":
        print(num)


def next_d(num):
    x = int(input("What is your next value? "))
    num /= x
    print(num)
    another_d(num)


def another_d(num):
    y = input("Another? ")
    if y == "yes":
        next_d(num)
    if y == "no":
        print(num)


inp = input("What function requires my presence? ")
if inp == "addition":
    num = int(input("What is your first value? "))
    next_a(num)
if inp == "subtraction":
    num = int(input("What is your first value? "))
    next_s(num)
if inp == "multiplication":
    num = int(input("What is your first value? "))
    next_m(num)
if inp == "division":
    num = int(input("What is your first value? "))
    next_d(num)
