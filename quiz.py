#1
def print_rectangle(height, width):
    for i in range(height):
        for j in range(width):
            print('&', end = ' ')
        print()
while True:
    choice = str(input("Do you want to print a Rectangle? "))

    if choice == 'yes':
        height = 5
        width = 10
        symbol = '&'
        print_rectangle(height, width)
    break

#2
def valid_input(option1):
    MENU_1 = 'Menu Options 1...'
    MENU_2 = 'Menu Options 2 ...'
    if option1 == 1:
        option2 = input()
        while option2 not in '#@!*':
            print('Invalid Entry - try again')
            print(MENU_1)
            option2 = input()
    elif option1 == 2:
        option2 = input()
        while option2 not in '123':
            print('Invalid Entry - try again')
            print(MENU_2)
            option2 = input()
option1 = int(input("Enter option1 (1 or 2): "))
valid_input(option1)


#3
def half_pyramid(rows):
    for i in range(1, rows + 1):
        print("$" * i)

while True:
    choice = str(input("Do you want to print a half pyramid? "))

    if choice == 'yes':
        height = 3
        symbol = '$'
        half_pyramid(height)
    break

        

            
            
        

