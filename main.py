import Shapes

def get_side_from_user(side_name:str):
  side = 0
  while not isinstance(side, float):
      try:
          side = float(input(f"Enter {side_name} \n"))
      except ValueError:
          print('Incorrect value. Please, try again.')
          print()
  return side


def asking_for_enter_side_or_radius(param:str):
    if (param == 'Circle' or param == 'Sphere'):
        return get_side_from_user('radius')
    
    elif (param == 'Square' or param == 'Cube'):
        return get_side_from_user('side')
    
    elif (param == 'Rectangle'):
        side_a = get_side_from_user('side 1')
        side_b = get_side_from_user('side 2')        
        return [side_a, side_b]
    
    elif (param == 'Triangle' or param == 'Rhombus'):
        height = get_side_from_user('height')
        base = get_side_from_user('base edge')
        return [height, base]

    elif (param == 'Trapezoid'):
        top_base = get_side_from_user('top base')
        bottom_base = get_side_from_user('bottom base')
        height = get_side_from_user('height')
        return [top_base, bottom_base, height]

    elif (param == 'Parallelepiped'):
        side_a = get_side_from_user('first edge')
        side_b = get_side_from_user('second edge')
        height = get_side_from_user('height')
        return [side_a, side_b, height]

    elif (param == 'Pyramid'):
        base_edge = get_side_from_user('base edge')
        side_edge = get_side_from_user('side edge')
        return [base_edge, side_edge]

    elif (param == 'Cylinder' or param == 'Cone'):
        radius = get_side_from_user('radius')
        height = get_side_from_user('height')
        return [radius, height]


def define_shape(shape:str):
    if (shape == 'Square'):
        side = asking_for_enter_side_or_radius('Square')    
        square = Shapes.Square(side)
        return square
      
    elif (shape == 'Cube'):
        side = asking_for_enter_side_or_radius('Cube')
        cube = Shapes.Cube(side)
        return cube

    elif (shape == 'Circle'):
        radius = asking_for_enter_side_or_radius('Circle')
        circle = Shapes.Circle(radius)
        return circle
    
    elif (shape == 'Sphere'):
        radius = asking_for_enter_side_or_radius('Sphere')
        sphere = Shapes.Sphere(radius)
        return sphere

    elif (shape == 'Rectangle'):
        [side_a, side_b]  = asking_for_enter_side_or_radius('Rectangle')
        rectangle = Shapes.Rectangle(side_a, side_b)
        return rectangle

    elif (shape == 'Triangle'):
        [hight, base] = asking_for_enter_side_or_radius('Triangle')
        triangle = Shapes.Triangle(hight, base)
        return triangle
    
    elif (shape == 'Rhombus'):
        hight, base = asking_for_enter_side_or_radius('Rhombus')
        rhombus = Shapes.Rhombus(hight, base)
        return rhombus
    
    elif (shape == 'Trapezoid'):
        [side_a, side_b, hight] = asking_for_enter_side_or_radius('Rhombus')
        trapezoid = Shapes.Trapezoid(side_a, side_b, hight)
        return trapezoid

    elif (shape == 'Parallelepiped'):
        [side_a, side_b, hight] = asking_for_enter_side_or_radius('Parallelepiped')
        parallelepiped = Shapes.Parallelepiped(side_a, side_b, hight)
        return parallelepiped
    
    elif (shape == 'Pyramid'):
        [base_edge, side_edge] = asking_for_enter_side_or_radius('Pyramid')
        pyramid = Shapes.Pyramid(base_edge, side_edge)
        return pyramid
    
    elif (shape == 'Cylinder'):
        [radius, height] = asking_for_enter_side_or_radius('Cylinder')
        cylinder = Shapes.Cylinder(radius, height)
        return cylinder
    
    elif (shape == 'Cone'):
        [radius, height] = asking_for_enter_side_or_radius('Cone')
        cone = Shapes.Cone(radius, height)
        return cone
    
    else:
        print("Not found shape")
        return 0


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
        shape = define_shape(shapes[shape_number])
        if (shape != 0):
            print(f"Area of {shapes[shape_number]} = {shape.area()}")
        
    else:
        shape = define_shape(shapes[shape_number])
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