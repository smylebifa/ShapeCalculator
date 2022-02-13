import shapes
import unittest

class TestSquare(unittest.TestCase):

    def test_area(self):
        square = shapes.Square(5)
        result = square.area()                                        
        self.assertEqual(result, 25)
    
    def test_perimeter(self):
        square = shapes.Square(2)
        result = square.perimeter()                                        
        self.assertEqual(result, 8)


class TestCube(unittest.TestCase):

    def test_area(self):
        cube = shapes.Cube(5)
        result = cube.area()                                        
        self.assertEqual(result, 150)
    
    def test_perimeter(self):
        cube = shapes.Cube(2)
        result = cube.perimeter()                                        
        self.assertEqual(result, 24)


class TestRectangle(unittest.TestCase):

    def test_area(self):
        rectangle = shapes.Rectangle(5, 10)
        result = rectangle.area()                                        
        self.assertEqual(result, 50)
    
    def test_perimeter(self):
        rectangle = shapes.Rectangle(5, 10)
        result = rectangle.perimeter()                                        
        self.assertEqual(result, 30)


class TestTrapezoid(unittest.TestCase):

    def test_area(self):
        trapezoid = shapes.Trapezoid(5, 10, 7)
        result = trapezoid.area()                                        
        self.assertEqual(result, 52.5)


class TestRhombus(unittest.TestCase):

    def test_area(self):
        rhombus = shapes.Rhombus(5, 10)
        result = rhombus.area()                                        
        self.assertEqual(result, 50)
    
    def test_perimeter(self):
        rhombus = shapes.Rhombus(5, 10)
        result = rhombus.perimeter()                                        
        self.assertEqual(result, 30)


class TestTriangle(unittest.TestCase):

    def test_area(self):
        triangle = shapes.Triangle(5, 10)
        result = triangle.area()                                        
        self.assertEqual(result, 25)


class TestParallelepiped(unittest.TestCase):

    def test_area(self):
        parallelepiped = shapes.Parallelepiped(5, 10, 7)
        result = parallelepiped.area()                                        
        self.assertEqual(result, 350)
    

class TestPyramid(unittest.TestCase):

    def test_area(self):
        pyramid = shapes.Pyramid(6, 5)
        result = pyramid.area()                                        
        self.assertEqual(result, 84)
    
    def test_perimeter(self):
        pyramid = shapes.Pyramid(6, 5)
        result = pyramid.perimeter()                                        
        self.assertEqual(result, 44)


class TestCircle(unittest.TestCase):

    def test_area(self):
        circle = shapes.Circle(5)
        result = circle.area()                                        
        self.assertEqual(result, 78.5)

    def test_perimeter(self):
        circle = shapes.Circle(5)
        result = circle.perimeter()                                        
        self.assertEqual(result, 31.4)


class TestSphere(unittest.TestCase):

    def test_area(self):
        sphere = shapes.Sphere(5)
        result = sphere.area()                                        
        self.assertEqual(result, 314.0)


class TestCylinder(unittest.TestCase):

    def test_area(self):
        cylinder = shapes.Cylinder(5,10)
        result = cylinder.area()                                        
        self.assertEqual(result, 471.0)


class TestCone(unittest.TestCase):

    def test_area(self):
        cone = shapes.Cone(5, 10)
        result = cone.area()                                        
        self.assertEqual(result, 254.03134)