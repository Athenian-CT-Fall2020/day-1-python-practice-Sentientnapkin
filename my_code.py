# This is an example of a comment that Python ignores. Use these to make notes as you write your code. You will also fill out the top comment with any help or resources you use.
# Collaborators:               (fill this is on every assignment, even if the answer is "none")

#print ("hello world")
#I just left a note :)
#x = int(input("What is your first number: "))
#y = int(input("What is your second number: "))
#a = x*y
#print("Yeah your answer is" ,a )
#print("I am going into a deep slumber for another 1000 years, wake me up later thank you.")

f = input("What function requires my presence? ")
if f == "addition":
    b = int(input("What is your first value? "))
    c = int(input("What is your next value? "))
    z = input("Do you require another number? ")
    if z == "no":
        print(b+c)
    if z == "yes":
        d = int(input("What is your next value? "))
        z = input("Do you require another number? ")
        if z == "no":
            print(b + c + d)
        if z == "yes":
            a = int(input("What is your next value? "))
            print(a+b+c+d)
if f == "multiplication":
    b = int(input("What is your first value? "))
    c = int(input("What is your next value? "))
    z = input("Do you require another number? ")
    if z == "no":
        print(b*c)
    if z == "yes":
        d = int(input("What is your next value? "))
        z = input("Do you require another number? ")
        if z == "no":
            print(b * c * d)
        if z == "yes":
            a = int(input("What is your next value? "))
            print(a*b*c*d)
if f == "division":
    b = int(input("What is your first value? "))
    c = int(input("What is your next value? "))
    z = input("Do you require another number? ")
    if z == "no":
        print(b/c)
    if z == "yes":
        d = int(input("What is your next value? "))
        z = input("Do you require another number? ")
        if z == "no":
            print(b / c / d)
        if z == "yes":
            a = int(input("What is your next value? "))
            print(a/b/c/d)
if f == "subtraction":
    b = int(input("What is your first value? "))
    c = int(input("What is your next value? "))
    z = input("Do you require another number? ")
    if z == "no":
        print(b-c)
    if z == "yes":
        d = int(input("What is your next value? "))
        z = input("Do you require another number? ")
        if z == "no":
            print(b - c - d)
        if z == "yes":
            a = int(input("What is your next value? "))
            print(a-b-c-d)