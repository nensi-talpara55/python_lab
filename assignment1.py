#1. print message
print("hello world")

#2. add two numbers
num1 = float(input("enter a value:"))
num2 = float(input("enter a value:"))
sum = num1+num2
print(f"the sum of{num1} and {num2} is {sum}")

#3. even or odd
num = int(input("enter number:"))
if num % 2 ==0:
     print(f"this number is even")
     
else:
     print(f"this number is odd")
     
#4. check leap year
year = int(input("enter a year:"))
   
if (year % 4 == 0 and year % 100):
     print(f"{year} is a leap % 100")
else:
     print(f"{year} is not a leap year.")
     
#5. print pi value
import math

print("The value of pi is:", math.pi)
          
#6. store and print constant value
# Store a constant value
PI = 3.141592653589793  # conventionally, constants are written in all caps

# Print the constant value
print("The value of PI is:", PI)

#7. square of a number
# Store a number
number = 5

# Calculate the square
square = number ** 2  # or you can use number * number

# Print the result
print("The square of", number, "is:", square)

#8. area of circle
import math

# Store the radius
radius = 5

# Calculate the area
area = math.pi * radius ** 2

# Print the result
print("The area of the circle with radius", radius, "is:", area)

#check data type
# Store a value
my_var = 42

#9. Check the data type
print("The data type of my_var is:", type(my_var))

#10. use math functions
import math

num = 7

print("Square root:", math.sqrt(num))
print("Absolute value:", abs(-num))
print("Power of 2:", num ** 2)
print("Ceiling:", math.ceil(3.4))
print("Floor:", math.floor(3.4))

#11. find power
# Base and exponent
base = 5
exponent = 3

# Calculate power
result = base ** exponent  # or you can use pow(base, exponent)

# Print result
print(base, "raised to the power", exponent, "is:", result)

#12. check positive or negative
# Store a number
num = -7


if num >= 0:
    print(num, "is positive")
else:
    print(num, "is negative")


   