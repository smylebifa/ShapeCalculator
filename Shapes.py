import math

# Shape
class Shape:
    title = 'Shape'
 
    def area(self):
        pass

    def perimeter(self):
       pass


# Square
class Square(Shape):
    title = 'Square'
 
    def __init__(self, x:float):
       super().__init__()
       self._x = x
 
    def area(self):
        return round(self._x ** 2, 5)

    def perimeter(self):
        return round(self._x * 4, 5) 


# Cube
class Cube(Square):
    title = 'Cube'
 
    def area(self):
        return super().area() * 6

    def perimeter(self):
       return self._x * 12 


# Rectangle 
class Rectangle(Square):
    title = 'Rectangle'
 
    def __init__(self, x:float, y:float):
        super().__init__(x)
        self._y = y
 
    def area(self):
        return self._x * self._y

    def perimeter(self):
       return (self._x * 2) + (self._y * 2)


# Trapezoid
class Trapezoid(Shape):
    title = 'Trapezoid'
 
    def __init__(self, x:float, y:float, h:float):
        self._x = x
        self._y = y
        self._h = h
 
    def area(self):
       return round(0.5 * (self._x + self._y) * self._h, 5) 
    
    def perimeter(self):
       return 0


# Rhombus
class Rhombus(Rectangle):
    title = 'Rhombus'
 
    def area(self):
        return super().area() 


# Triangle
class Triangle(Rectangle):
    title = 'Triangle'
 
    def area(self):
       return super().area() * 0.5
    
    def perimeter(self):
       return 0


# Parallelepiped
class Parallelepiped(Rectangle):
    title = 'Parallelepiped'
 
    def __init__(self, x:float, y:float, h:float):
        super().__init__(x, y)
        self._h = h
 
    def area(self):
        return self._x * self._y * self._h 
    
    def perimeter(self):
       return 0


# Pyramid
class Pyramid(Shape):
  title = 'Pyramid'
  
  # x - base edge, y - side edge
  def __init__(self, x, y):
    self._x = x
    self._y = y
    
  def area(self):
      return round(self._x**2 + 2*self._x * (math.sqrt((self._y**2) - (self._x**2 / 4))), 5)
  
  def perimeter(self):
       return round((self._x * 4) + (self._y * 4), 5)


# Circle
class Circle(Shape):
    title = 'Circle'
    pi = 3.14
 
    def __init__(self, r:float):
       super().__init__()
       self._r = r
 
    def area(self):
        return round(self._r ** 2 * Circle.pi, 5)

    def perimeter(self):
        return round(self._r * Circle.pi * 2, 5)


# Sphere
class Sphere(Circle):
    title = 'Sphere'
 
    def area(self):
        return super().area() * 4
    
    def perimeter(self):
        return 0


# Cylinder
class Cylinder (Circle):
    title = 'Cylinder'

    def __init__(self, r:float, h:float):
        super().__init__(r)
        self._h = h
    
    def area(self):
        return 2 * (self._r**2 * Cylinder.pi) + 2 * (self._r * Cylinder.pi * self._h)

    def perimeter(self):
        return 0


# Cone
class Cone (Cylinder):
    title = 'Cone'

    def __init__(self, r:float, h:float):
       super().__init__(r, h)

    def generating(self): 
        return math.sqrt(self._r ** 2 + self._h ** 2)
    
    def area(self):
        return round((self._r ** 2 * Cone.pi) + (self._r * Cone.pi * self.generating()), 5)
    
    def perimeter(self):
        return 0