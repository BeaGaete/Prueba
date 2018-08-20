import svgwrite
from svgwrite import shapes as sh

WIDTH = 1300
HEIGHT = 800
ORIGIN_X = 50
ORIGIN_Y = HEIGHT-50

class Chart:
    def __init__(self, data, filename):
        self.data = data
        self.dwg = svgwrite.Drawing(filename)
        self.shape = sh

    # Draw the x and y axes for the graph
    def draw_axes(self):
        line = self.dwg.line(start=(ORIGIN_X, ORIGIN_Y),
                 end=(WIDTH, ORIGIN_Y),
                 stroke='black',
                 stroke_width=5)
        self.dwg.add(line)
        line = self.dwg.line(start=(ORIGIN_X, ORIGIN_Y),
                 end=(ORIGIN_X, 0),
                 stroke='black',
                 stroke_width=5)
        self.dwg.add(line)

    def draw_line(self, nota):
        line = self.dwg.line(start=(ORIGIN_X, nota - 19),
                             end=(WIDTH, nota - 19), stroke='gray',
                             stroke_width=1)
        self.dwg.add(line)

    def draw_points(self):
        for i in range(len(self.data)):
            circle = self.dwg.shapes.Circle(center=(self.data[0], i), r=1)
            self.dwg.add(circle)

    def draw_variance(self, start, end):
            var = self.dwg.line(start=start,
                 end=end,
                 stroke='blue',
                 stroke_width=3)
            self.dwg.add(var)

    def draw_circles(self, x, y):
        cir = self.shape.Circle((x, y), r=5, color='red')
        self.dwg.add(cir)

if __name__ == "__main__":
    c = Chart([1, 2, 3], "chart.svg")
    c.dwg.viewbox(width=WIDTH, height=HEIGHT)
    c.draw_axes()
    c.dwg.save()
