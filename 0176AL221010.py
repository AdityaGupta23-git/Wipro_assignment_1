        #    Name = Aditya Gupta
        #    Enrollment = 0176AL221010
        #    college = LNCTE
        #    Branch = CSE-AIML
        #    Semester = 7th 

#EXERCISES:
    
# Q1. Check if a given number is Positive, Negative or Zero
num = float(input("Enter a number: "))
if num > 0:
print("Positive")
elif num < 0:
print("Negative")
else:
print("Zero")

# Q2. Check if a given number is odd or even
num = int(input("Enter a number: "))
if num % 2 == 0:
print("Even")
else:
print("Odd")

# Q3. Check if two numbers have the same last digit
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if num1 % 10 == num2 % 10:
print("True")
else:
print("False")

# Q4. Print numbers from 1 to 10 in a single row with one tab space
for i in range(1, 11):
print(i, end='\t')
print()

# Q5. Print even numbers between 23 and 57 (each in separate row)
for num in range(24, 58, 2):
print(num)

# Q6. Check if a given number is prime or not
num = int(input("Enter a number: "))
if num > 1:
for i in range(2, int(num**0.5) + 1):
if num % i == 0:
print("Not prime")
break
else:
print("Prime")
else:
print("Not prime")

# Q7. Print prime numbers between 10 and 99
for num in range(10, 100):
if num > 1:
for i in range(2, int(num**0.5) + 1):
if num % i == 0:
break
else:
print(num)

# Q8. Print the sum of all digits of a given number
num = input("Enter a number: ")
digit_sum = sum(int(digit) for digit in num)
print("Sum of digits:", digit_sum)

# Q9. Reverse a given number and print
num = input("Enter a number: ")
reversed_num = num[::-1]
print("Reversed number:", reversed_num)

# Q10. Check if the given number is a palindrome
num = input("Enter a number: ")
if num == num[::-1]:
print("Palindrome")
else:
print("Not a palindrome")

"---------------------------------------------------------------------------------------------------------"

#MINI PROJECTS:
    
# 1.	create a python program that asks the user how far they want to travel. if they want to travel less than three miles tell them to ride Bicycle. if they want to travel more than three miles, but less than three hundred miles, tell them to ride Motor-cycle. if they want to travel three hundred miles or more tell them to driver Super-Car.
# Sample Output:
# How far would you like to travel in miles? 2500
# I suggest Super-Car to your destination

distance = int(input("How far would you like to travel in miles? "))

if distance < 3:
    print("I suggest Bicycle to your destination")
elif 3 <= distance < 300:
    print("I suggest Motor-cycle to your destination")
else:
    print("I suggest Super-Car to your destination")


# 2.	Let's assume you are planning to use your python skills to build an App for Mobile.
# You decide to host your application on servers running in the cloud. you pick a hosting provider that charges $0.51 per hour. you will launch your services using one server and want to know how much it will cost to operate per day, per week, per month.
# Write a python program that displays the answers to the following questions:
# How much does it cost to operate one server per day?
# How much does it cost to operate one server per week?
# How much does it cost to operate one server per month?
# How much days can I operate one server with $918?

cost_per_hour = 0.51


cost_per_day = cost_per_hour * 24
cost_per_week = cost_per_day * 7
cost_per_month = cost_per_day * 30
days_with_918 = 918 / cost_per_day

print(f"Cost to operate one server per day: ${cost_per_day:.2f}")
print(f"Cost to operate one server per week: ${cost_per_week:.2f}")
print(f"Cost to operate one server per month: ${cost_per_month:.2f}")
print(f"Days you can operate one server with $918: {int(days_with_918)} days")
