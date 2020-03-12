import classFigure
class Rectangle(classFigure.Figure):
    """
    Класс прямоугольника
    """
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.get_perimeter()
        self.get_square()

    def get_perimeter(self):
        self.perimeter = (self.a + self.b) * 2

    def get_square(self):
        self.square = self.a * self.b
