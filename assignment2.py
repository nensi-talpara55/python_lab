#1. calculate simple interest
P = float(input("Principal: "))
R = float(input("Rate (%): "))
T = float(input("Time (years): "))

SI = P * R * T / 100
print("Simple Interest:", SI)


#2. find maximum of 2 numbers
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if a > b:
    print("Maximum:", a)
else:
    print("Maximum:", b)


#3. print number 1 to 5
for i in range(1, 6):
    print(i)


#4. find length of a string
text = input("Enter a string: ")
length = len(text)
print("Length of the string:", length)


#5. print a welcome message
print("Welcome!")


#6. print first character of a string
text = input("Enter a string: ")
print("First character:", text[0])


#7. print last character of a string
text = input("Enter a string: ")
print("Last character:", text[-1])


#8. check positive and negative numbers
num = float(input("Enter a number: "))

if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")


#9. add 3 numbers
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

sum = a + b + c
print("Sum:", sum)


#10. take a input from the years
years = int(input("Enter number of years: "))
print("You entered:", years)
