#write a program to find the sum of digits of a given number'


number = int(input("Enter any number to find sum of digits of the number:"))

number = abs(number)

sum_of_digits = 0

while number > 0:
    digit = number % 10     
    sum_of_digits += digit   
    number //= 10            

print(f"The sum of the digits is {sum_of_digits}")
