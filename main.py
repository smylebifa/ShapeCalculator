import shapes as my_shapes

shapes = {
    1 : 'Square', 
    2 : 'Cube', 
    3 : 'Circle',
    4 : 'Rectangle',
    5 : 'Triangle',
    6 : 'Trapezoid',
    7 : 'Rhombus',
    8 : 'Parallelepiped',
    9 : 'Pyramid',
    10 : 'Sphere',
    11 : 'Cylinder',
    12 : 'Cone',    
    }

while (True):

    # Display shapes for user
    print("Shapes:")
    for number, value in shapes.items():
        print(number, ' - ', value)
    print()


    # Getting figure from user
    shape_number = 0
    while shape_number not in shapes.keys():
        try:
            shape_number = int(input('Please enter shape number\n'))
        except ValueError:
            print('Incorrect value. Please, try again.')
            print()
    
    print('Your shape is', shapes[shape_number])
    print()

    # Getting from user type of calculation with shape(perimeter, area)
    type_of_calculation = 0

    while type_of_calculation not in (1, 2):
        try:
            type_of_calculation = int(input("Enter 1 for calculate perimeter "
                                             "and 2 for area\n"))
        except ValueError:
            print('Incorrect value. Please, try again.')
            print()

    # Calculate user need
    if (type_of_calculation == 2):
        shape = my_shapes.define_shape(shapes[shape_number])
        if (shape != 0):
            print(f"Area of {shapes[shape_number]} = {shape.area()}")
        
    else:
        shape = my_shapes.define_shape(shapes[shape_number])
        if (shape != 0):
            print(f"Perimeter of {shapes[shape_number]} = {shape.perimeter()}")

    print()

    is_continue = None
    while is_continue not in ('y', 'n'):
        try:
            is_continue = input("Do you wan't to continue? " 
                                        "To continue pres 'y' and to exit 'n'" 
                                        "\n").lower()
        except ValueError:
            print('Incorrect value. Please, try again.')
            print()

    if (is_continue == 'n'):
        break;

    print("\n" * 100)