number_input = input("Enter a number: ")

if number_input.isdigit():
    num = int(number_input)
    if num % 2 == 0:
        print("The number is Even")
    else:
        print("The number is Odd")
else:
    print("Invalid input. Please input numbers only.")