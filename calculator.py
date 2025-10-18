name = input('What is your name? ')
reason = input(f'Hi {name}! Do you want to give me a maths question?: ')
if reason == 'yes':
    print('Ok')

    first_number = int(input('What is your first number: '))
    second_number = int(input('What is your second number: '))
    answer = input('What operation do you want to do? ')
    if answer == 'addition':
        addition = (first_number + second_number)
        print(f'The sum of {first_number} and {second_number} is {addition}') 

# Subtraction
    if answer == 'subtraction':
        subtraction = (first_number - second_number)
        print(f'The difference of {first_number} and {second_number} is {subtraction}')

# Multiplication
    if answer == 'multiplication':
        multiplication = (first_number * second_number)
        print(f'The product of {first_number} and {second_number} is {multiplication}')

# Division
    if answer == 'division':
        division = (first_number / second_number)
        print(f'The quotient of {first_number} and {second_number} is {division}')

# Floor Division
    if answer == 'floor division':
        floor_divison = (first_number // second_number)
        print(f'The floor division of {first_number} and {second_number} is {floor_divison}')

# Exponentiation
    if answer == 'exponentiation':
        exponentiation = (first_number ** second_number)
        print(f'The exponentatial of {first_number} and {second_number} is {exponentiation}')
else:
    print('Sorry I am not of use. Maybe when you are ready to calculate')