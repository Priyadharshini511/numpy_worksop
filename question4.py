#write a program to find the sum of digits of a given number'
def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))
number = int(input("Enter a number: "))
print(f"The sum of the digits of {number} is {sum_of_digits(number)}.")
