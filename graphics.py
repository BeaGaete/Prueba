import svgwrite
from svgwrite import shapes as sh
from svgwrite import path, text

WIDTH = 1300
HEIGHT = 800
ORIGIN_X = 50
ORIGIN_Y = HEIGHT-50

class Chart:
    def __init__(self, filename, data1=None, data2=None):
        self.data1 = data1
        self.data2 = data2
        self.dwg = svgwrite.Drawing(filename)
        self.text = svgwrite.text
        self.shape = sh
        self.path = path

    # Draw the x and y axes for the graph
    def draw_axes(self):
        line = self.dwg.line(start=(ORIGIN_X, ORIGIN_Y),
                 end=(WIDTH, ORIGIN_Y),
                 stroke='black',
                 stroke_width=5)
        self.dwg.add(line)
        line = self.dwg.line(start=(ORIGIN_X, ORIGIN_Y),
                 end=(ORIGIN_X, 25),
                 stroke='black',
                 stroke_width=5)
        self.dwg.add(line)

    def draw_line_h(self, nota):
        line = self.dwg.line(start=(ORIGIN_X, nota),
                             end=(WIDTH, nota), stroke='white',
                             stroke_width=1)
        self.dwg.add(line)

    def draw_line_v(self, nota):
        line = self.dwg.line(start=(nota, 25), end=(nota, 750), stroke='white',
                             stroke_width=1)
        self.dwg.add(line)


    def draw_points(self, color):
        for i in range(len(self.data1)):
            circle = self.dwg.shapes.Circle(center=(
                self.data1[0], i), r=1, fill=color)
            self.dwg.add(circle)

    def draw_variance(self, start, end, color):
            var = self.dwg.line(start=start,
                 end=end,
                 stroke=color,
                 stroke_width=6)
            self.dwg.add(var)

    def draw_circles(self, x, y, color):
        cir = self.shape.Circle((x, y), r=5, color=color)
        self.dwg.add(cir)

    def draw_rectangle(self): # 'gray' '#F1E4B3' '#B3C8BE'
        rect = self.shape.Rect(insert=(50, 25), size=(1250, 725), fill='#D9D9D9')
        self.dwg.add(rect)

    # recibe lista de tuplas con los puntos
    def draw_poly(self, start, end, color):
        polyline = self.shape.Line(start=start, end=end, stroke=color, stroke_width=3)
        self.dwg.add(polyline)

    def add_text(self, texto, insert):
        text = self.text.Text(texto, insert=insert, fill='#133046', text_anchor='middle', font_family='Verdana')
        self.dwg.add(text)

if __name__ == "__main__":
    c = Chart([1, 2, 3], "chart.svg")
    c.dwg.viewbox(width=WIDTH, height=HEIGHT)
    c.draw_axes()
    c.dwg.save()
