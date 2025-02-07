#PRACTICAL 10
#AIM: A PROGRAM THAT CONVERTS A GIVEN NUMBER FROM ONE BASE TO ANOTHER
def decimal_others(value, choice):
    if choice == 1:
        return value
    elif choice == 2:
        return '{0:b}'.format(value)  # Decimal to Binary
    elif choice == 3:
        return '{0:o}'.format(value)  # Decimal to Octal
    elif choice == 4:
        return '{0:x}'.format(value)  # Decimal to Hexadecimal
    else:
        return 'Invalid choice'

def binary_others(value, choice):
    decimal_value = int(value, 2)  # Convert Binary to Decimal
    if choice == 1:
        return decimal_value
    elif choice == 2:
        return value
    elif choice == 3:
        return '{0:o}'.format(decimal_value)  # Binary to Octal
    elif choice == 4:
        return '{0:x}'.format(decimal_value)  # Binary to Hexadecimal
    else:
        return 'Invalid choice'

def octal_others(value, choice):
    decimal_value = int(value, 8)  # Convert Octal to Decimal
    if choice == 1:
        return decimal_value
    elif choice == 2:
        return '{0:b}'.format(decimal_value)  # Octal to Binary
    elif choice == 3:
        return value
    elif choice == 4:
        return '{0:x}'.format(decimal_value)  # Octal to Hexadecimal
    else:
        return 'Invalid choice'

def hexadecimal_others(value, choice):
    decimal_value = int(value, 16)  # Convert Hexadecimal to Decimal
    if choice == 1:
        return decimal_value
    elif choice == 2:
        return '{0:b}'.format(decimal_value)  # Hexadecimal to Binary
    elif choice == 3:
        return '{0:o}'.format(decimal_value)  # Hexadecimal to Octal
    elif choice == 4:
        return value
    else:
        return 'Invalid choice'

print("Convert from 1:Decimal, 2:Binary, 3:Octal, 4:Hexadecimal")
input_choice = int(input("Enter your choice: "))

if input_choice == 1:
    decimal_value = int(input("Enter Decimal value: "))
    print('Convert to 1:Decimal, 2:Binary, 3:Octal, 4:Hexadecimal')
    choice = int(input("Enter target conversion: "))
    print("Converted value:", decimal_others(decimal_value, choice))

elif input_choice == 2:
    binary_value = input("Enter Binary value: ")
    print('Convert to 1:Decimal, 2:Binary, 3:Octal, 4:Hexadecimal')
    choice = int(input("Enter target conversion: "))
    print("Converted value:", binary_others(binary_value, choice))

elif input_choice == 3:
    octal_value = input("Enter Octal value: ")
    print('Convert to 1:Decimal, 2:Binary, 3:Octal, 4:Hexadecimal')
    choice = int(input("Enter target conversion: "))
    print("Converted value:", octal_others(octal_value, choice))

elif input_choice == 4:
    hexadecimal_value = input("Enter Hexadecimal value: ")
    print('Convert to 1:Decimal, 2:Binary, 3:Octal, 4:Hexadecimal')
    choice = int(input("Enter target conversion: "))
    print("Converted value:", hexadecimal_others(hexadecimal_value, choice))

else:
    print("Invalid choice")
