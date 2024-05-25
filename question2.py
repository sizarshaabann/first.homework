binary = input("Enter a binary number: ")
try:
    decimal = int(binary,2)
    print("the decimal of", binary,"is",decimal)
except ValueError:
    print("Invalid input: the number must be a binary number")