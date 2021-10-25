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