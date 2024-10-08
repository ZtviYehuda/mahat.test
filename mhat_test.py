num1 = int(input("הכנס מספר 1:     "))
num2 = int(input("הכנס מספר 2:     "))
numbers_count = 0
positive_numbers = 0
equal_numbers = 0

while num2 != -num1:
    if num1 == num2:
        equal_numbers += 1

    if num1 > 0:
        positive_numbers += 1

    if num2 > 0:
        positive_numbers += 1

    num1 = int(input("הכנס מספר 1:     "))
    num2 = int(input("הכנס מספר 2:     "))

print(f"equal = {equal_numbers} positive = {positive_numbers} count = {numbers_count}")







