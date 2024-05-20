# find if the given number is a palindrome or not?

def is_palindrome(number):
    # Convert the number to a string
    number_str = str(number)
    
    # Reverse the string
    reversed_str = number_str[::-1]
    
    # Compare the original string with the reversed string
    if number_str == reversed_str:
        return True
    else:
        return False

# Example usage
number = int(input("Enter a number to find palindrome or not:"))
if is_palindrome(number):
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")
